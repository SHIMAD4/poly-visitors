from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):  # pylint: disable=function-redefined, too-many-ancestors
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "class": "form-input",
                "placeholder": "Введите логин",
                "maxLength": "50",
                "minLength": "6",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "required": "",
                "name": "email",
                "id": "email",
                "type": "text",
                "class": "form-input",
                "placeholder": "Введите email",
                "maxLength": "50",
                "minLength": "6",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "required": "",
                "name": "password1",
                "id": "password1",
                "type": "password",
                "class": "form-input",
                "placeholder": "Введите пароль",
                "maxLength": "22",
                "minLength": "8",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "required": "",
                "name": "password2",
                "id": "password2",
                "type": "password",
                "class": "form-input",
                "placeholder": "Подтвердите пароль",
                "maxLength": "22",
                "minLength": "8",
            }
        )

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ["username", "email", "password1", "password2"]
