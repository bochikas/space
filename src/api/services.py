from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(*, username: str, password: str, email: str = '', first_name: str = '', last_name: str = '') -> User:
    """Создание пользователя."""

    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    return user


def update_user(*, user: User, first_name: str = '', last_name: str = '',
                email: str = '', dob: str = None, gender: str = None) -> None:
    """Изменение данных пользователя."""

    fields_to_update = {'first_name': first_name, 'last_name': last_name, 'email': email, 'dob': dob, 'gender': gender}

    for field, value in fields_to_update.items():
        if value:
            setattr(user, field, value)
    user.save()


def soft_delete_user(user: User):
    """'Мягкое' удаление пользователя."""

    user.deleted = True
    user.save()
