from freezegun import freeze_time
from rest_framework.test import APIClient
from django.test import TestCase

from . import helpers


class PostTestCase(TestCase):
    def setUp(self):
        self.user = helpers.create_user(username="my_user")
        self.client = APIClient()
        self.client.force_login(user=self.user)

        self.admin = helpers.create_user(username="my_admin", is_superuser=True)
        self.admin_client = APIClient()
        self.admin_client.force_login(user=self.admin)

    def test_get_posts(self):
        # given
        author = helpers.create_user()
        post = helpers.create_post(author=author)

        # action / when
        response = self.client.get("/api/v1/posts/")

        # then
        assert response.status_code == 200, response.data
        assert len(response.data["results"]) == 1, response.data
        assert response.data["results"][0]["title"] == post.title

    def test_not_admin_cannot_delete_post(self):
        author = helpers.create_user()
        post = helpers.create_post(author=author)

        response = self.client.delete(f"/api/v1/posts/{post.id}/")

        assert response.status_code == 403, response.data

    def test_author_deletes_post(self):
        author = helpers.create_user()
        post = helpers.create_post(author=author)
        client = APIClient()
        client.force_login(user=author)

        response = client.delete(f"/api/v1/posts/{post.id}/")

        assert response.status_code == 204, response.data

    @freeze_time("2020-01-01 00:00:05")
    def test_create_post(self):
        # given
        data = {
            "title": "Some title",
            "body": "Some body",
            "author": f"http://testserver/api/v1/users/{self.admin.id}/",
            "tags": [],
            "pub_date": "2020-01-01T00:00:05Z",
        }

        # when
        response = self.admin_client.post(f"/api/v1/posts/", data=data)

        # then
        assert response.status_code == 201, response.data
        del response.data["id"]
        del response.data["url"]
        assert response.data == data, response.data
