from db.models import User


def create_user(username: str, password: str, **kwargs) -> User:
    user = User.objects.create_user(
        username=username,
        password=password
    )
    for key, value in kwargs.items():
        if value is not None:
            setattr(user, key, value)
    user.save()
    return user


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(user_id: int, **kwargs) -> None:
    user = User.objects.get(id=user_id)
    if "password" in kwargs:
        user.set_password(kwargs["password"])
    for key, value in kwargs.items():
        if key == "password":
            continue
        if value is not None:
            setattr(user, key, value)
    user.save()
