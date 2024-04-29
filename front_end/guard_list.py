import requests
from flet import *
import uuid
url = 'http://127.0.0.1:8000/parking_record/guardinList/'

def guard_login(page: Page):
    names = Column(
        on_scroll=ScrollMode.AUTO
    )

    def submit(e):
        url_login = 'http://127.0.0.1:8000/authtoken/token/login/'

        data = {
            "email": datas['email'],
            "password": password_login.value
        }
        request = requests.post(url=url_login, data=data)
        if request.status_code == 200:
            page.go('/home_guard')
        else:
            print(request.status_code)

    password_login = TextField(
        password=True,
        can_reveal_password=True
    )

    def password(e, user_id):
        rg = requests.get(url=f"http://127.0.0.1:8000/parking_record/user/{user_id}/")
        global datas
        datas = rg.json()
        page.client_storage.set("security_user_id", user_id)
        page.dialog = CupertinoAlertDialog(
            open=True,
            content=Column(
                controls=[
                    Text(value=f"{datas['first_name']} {datas['last_name']}"),
                    Text(value="Please Enter Password:"),
                    password_login,
                    TextButton(
                        text="submit",
                        on_click=lambda e: submit(e),
                    )
                ]
            )
        )
        page.update()

    response = requests.get(url=url)
    for i in response.json():
        names.controls.append(
            Container(
                bgcolor=colors.PINK,
                width=300,
                height=50,
                content=Container(
                    bgcolor=colors.BLUE_GREY,
                    border_radius=border_radius.all(18),
                    width=50,
                    content=TextButton(
                        content=Text(
                            value=f"{i['first_name']} {i['last_name']}",
                            color=colors.BLACK,
                            size=20,
                            font_family="Georgia"
                        ),
                        on_click=lambda e, user_id=i['id']: password(e, user_id)
                    )
                )

            )
        )

    return View(
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        scroll=ScrollMode.ADAPTIVE,
        appbar=AppBar(
            bgcolor=colors.BLUE,
            title=Text(value="PLEASE LOGIN", weight=FontWeight.BOLD, color="black"),
            center_title=True

        ),
        controls=[
            Text(value="Please choose your name and provide your password to login"),
            names,
            IconButton(icon=icons.BACKUP, on_click=lambda _: page.go('/register')),
        ]

    )
