import uuid
import requests
from flet import *
import asyncio

post_url = 'http://127.0.0.1:8000/authent/login/'


class login_(Column):
    def __init__(self):
        super().__init__()
        self.login = TextButton(
            text="Log In",
            on_click=lambda e:asyncio.run(self.LOGIN(e)),
        )

    def register(self, e):
        self.page.go('/register')

## Function ya kuhandle  user akiwa anaclick button ya login
    async def LOGIN(self, e):
        if self.email:
            self.login_email = self.email.value
            if not self.login_email:
                self.email.error_text = "please enter the email"
                self.email.update()
            else:
                self.email.error_text = self.email.clean()
                self.email.update()

        if self.password:
            self.login_password = self.password.value
            if not self.login_password:
                self.password.error_text = "please enter the email"
                self.password.update()
            else:
                self.password.error_text = self.password.clean()
                self.password.update()

        data = {
            "email": self.login_email,
            "password": self.login_password
        }
        response = requests.post(url=post_url, data=data)
        if response.status_code == 200:
            self.page.snack_bar = SnackBar(open=True,
                                           margin=margin.only(left=12),
                                           content=Text(
                                               value="Welcome!! Successfully you have Login In",
                                               color=colors.BLACK,
                                               weight=FontWeight.BOLD,
                                           ),
                                           bgcolor=colors.BLUE)
            self.page.client_storage.set("email", self.login_email)
            self.page.client_storage.set("password", self.login_password)
            token = str(uuid.uuid4())
            self.page.client_storage.set("user_session_token", token)
            self.page.client_storage.set("user_identification_login",self.login_email)
            self.page.update()
            await asyncio.sleep(5)
            self.page.go('/home')

        else:
            self.email.error_text = "Please correct your email"
            self.password.error_text = "Please correct your password"
            self.email.update()
            self.password.update()
            self.page.update()
            print(f"Error:{response.status_code} Code")

    def email_change(self, e):
        if self.email.value:
            self.email.error_text = self.email.clean()
            self.email.update()

    def pass_change(self, e):
        if self.password.value:
            self.password.error_text = self.password.clean()
            self.password.update()

    def build(self):

        self.email = TextField(
            width=400,
            label="Email",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            keyboard_type=KeyboardType.EMAIL,
            on_change=lambda e: self.email_change(e)
        )
        self.password = TextField(
            width=400,
            label="PASSWORD",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            password=True,
            filled=True,
            can_reveal_password=True,
            on_change=lambda e: self.pass_change(e)
        )

        return [
            Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(value="LOGIN HERE",
                         size=40,
                         text_align=TextAlign.JUSTIFY,
                         style=TextStyle(decoration=TextDecoration.UNDERLINE),
                         weight=FontWeight.BOLD
                         ),
                    Divider(height=10),
                    self.email,
                    Container(height=10),
                    self.password,
                    self.login,
                    Container(
                        margin=margin.only(left=25),
                        content=TextButton(
                            text="Forget Password",
                            on_click=lambda e: self.page.go('/forget_password')
                        ),
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value="i don't have an account"),
                            TextButton(text="Sign Up", on_click=self.register)
                        ]
                    )

                ]
            )

        ]

def login(page:Page):

    return View(
        route='/login',
        controls=[
            login_()
        ]
    )