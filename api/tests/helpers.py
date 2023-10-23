import typing

from .. import models


def create_user(
    username: str = "username",
    password: str = "password",
    is_superuser: bool = False,
    **kwargs: typing.Any,
) -> models.User:
    return models.User.objects.create_user(
        username=username, password=password, is_superuser=is_superuser, **kwargs
    )


def create_post(
    author: models.User,
    title: str = "username",
    body: str = "password",
    tags: typing.Sequence[models.Tag] = (),
    **kwargs: typing.Any,
) -> models.Post:
    post = models.Post.objects.create(
        author=author, title=title, body=body, **kwargs
    )
    post.tags.set(tags)
    return post
