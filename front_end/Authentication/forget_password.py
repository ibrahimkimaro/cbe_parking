from flet import *
import requests


class reset_password(Column):
    def __init__(self):
        super().__init__(visible=True)
        self.password = TextField(
            width=400,
            label="PASSWORD",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            password=True,
            filled=True,
            can_reveal_password=True,
        )
        self.re_password = TextField(
            width=400,
            label="PASSWORD",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            password=True,
            filled=True,
            can_reveal_password=True,
        )
        self.btn_submit = FilledTonalButton(
            text="Submit",
            on_click=lambda e: self.submit(e)
        )
        self.resetPassword = Column(
            controls=[
                Container(
                    margin=margin.only(left=100),
                    content=Text(
                        color=colors.BLUE,
                        value="CHANGE PASSWORD",
                        size=20,
                        weight="bold"
                    )
                ),
                Text(value="Enter New Password:"),
                self.password,
                Text(value="Re Confirm Password:"),
                self.re_password,
                self.btn_submit
            ]
        )

    def submit(self, e):
        if self.password:
            self.passwrd = self.password.value
            if not self.passwrd:
                self.password.error_text = "Password must be strong"
                self.password.update()
            else:
                self.password.error_text = self.password.clean()
                self.password.update()
                print("password it is provises")
        response = requests.post(url='http://127.0.0.1:8000/auth/users/reset_password_confirm/',
                                 data={"new password": self.passwrd})
        self.page.go('/login')

    def build(self):
        return self.resetPassword


# Class ya kuhandle uid (user identification) na authentication token
class uid_token(Row):
    def __init__(self):
        super().__init__()
        self.uuid = TextField(
            visible=True,
            width=400,
            label="UUD",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            keyboard_type=KeyboardType.TEXT
        )
        self.auth_toke = TextField(
            visible=True,
            width=400,
            label="Authentication Token",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            keyboard_type=KeyboardType.TEXT
        )
        self.send_auth = ElevatedButton(
            text="Check",
            on_click=lambda e: self.check_auth(e),
        )

        self.auth = Column(
            controls=[
                Text(value="Enter UID from your email:"),
                self.uuid,
                Text(value="Enter auth_token from your email:"),
                self.auth_toke,
                self.send_auth
            ]
        )

    def check_auth(self, e):
        if self.auth_toke:
            self.auth_toke_validate = self.auth_toke.value
            if self.auth_toke_validate:
                print(self.auth_toke_validate)
            else:
                print("wo dont no about that token")
        if self.uuid:
            self.uuid_validate = self.uuid.value
            if self.uuid_validate:
                print(self.uuid_validate)
            else:
                print("wo dont no about that token")
        response = requests.post(url='http://127.0.0.1:8000/auth/users/reset_password_confirm/',
                                 data={"uid": self.uuid_validate})
        if response.status_code == 200:
            print("The Email is veryfied by this Token")
            self.send_auth.url('http://127.0.0.1:8000/auth/token_verify/')
            self.send_auth.update()
        else:
            print(f"Error: {response.status_code} Code" + "Token has expired")

    def build(self):
        return self.auth


def forgetPassword(page: Page):
    new_passwrd = reset_password()

    def check_email(e):
        if email:
            email_check = email.value
            if email_check:
                print(email_check)
            else:
                print("hujaandika email")
        response = requests.post(url='http://127.0.0.1:8000/auth/users/reset_password/', data={"email": email_check})
        if response.status_code == 204:
            page.snack_bar = SnackBar(open=True,
                                      content=Text(
                                          value="Congrates!! Token have been sent to your email",
                                          color=colors.BLACK,
                                          weight="bold",
                                          size=25),
                                      bgcolor="blue",
                                      padding=padding.only(left=450),
                                      )
            page.update()
            print(response.status_code)
        else:
            page.snack_bar = SnackBar(open=True,
                                      content=Text(
                                          value="Token do not sent:Please provide Email or Check the connection",
                                          color=colors.BLACK,
                                          weight="bold",
                                          size=25),
                                      bgcolor="red",
                                      padding=padding.only(left=450),
                                      )
            page.update()
            print(response.status_code)

    email = TextField(
        width=400,
        label="Email",
        label_style=TextStyle(size=15, italic=True),
        border_radius=border_radius.all(12),
        keyboard_type=KeyboardType.EMAIL
    )
    send_email = ElevatedButton(
        text="Send",
        on_click=lambda e: check_email(e),
    )

    # if email == reg.email:
    #     print("sawa")
    # else:
    #     print("angalia code")

    return View(
        horizontal_alignment="center",
        appbar=AppBar(
            title=Text("FORGET PASSWORD"),
            center_title=True,
        ),
        controls=[
            Column(
                controls=[
                    Text(value="Please Enter your email:"),
                    email,
                    Container(
                        margin=margin.only(left=300),
                        content=send_email),
                    uid_token()
                ]
            ),
            Container(height=30),
            new_passwrd
        ]

    )
