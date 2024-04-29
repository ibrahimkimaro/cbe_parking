import base64
import time

from flet import *
import requests
import uuid


def home(page: Page):
    email = page.client_storage.get("email")
    print(email)
    if email:
        user_id_get = requests.post(url='http://127.0.0.1:8000/userprofile/verify_email/', data={"email": email})
        if user_id_get.status_code == 200:
            id_data = user_id_get.json()
            user_id = id_data['id']
            page.client_storage.set("user_id", user_id)
            print(user_id)

        else:
            print(user_id_get.status_code)

    page.horizontal_alignment = "center"
    page.update()
    # page.client_storage.clear()
    # dialog inayo to angalizo na kuuliza kipindi unaaka kuondoka kwenye application
    dalog = AlertDialog(
        title=Text("Hellow please.."),
        modal=True,
        on_dismiss=lambda e: close_dialog(e),
        content=Text("Do you really want to exit to this App? "),
        actions=[
            TextButton(text="Yes", on_click=lambda e: exit_app(e)),
            TextButton(text="No", on_click=lambda e: close_dialog(e)),
        ]
    )

    def backregister(e):
        page.go('/register')

    # Funtion ya kufunga dialog ukibonyeza  "No"
    def close_dialog(e):
        dalog.open = False
        dalog.update()

    # Funtion ya kuruhusu application ijifunge ukibonyeza "Yes"
    def exit_app(e):
        page.window_close()
        print('*****APPLICATION IS QUITED...******?')

    def change(e):
        chs = e.control.selected_index
        print(chs)
        # condition ya kufungua VIEW ya Account
        if chs == 0:
            page.go('/account')
        # condition ya kufungua VIEW ya kuomba kibali za parking
        elif chs == 1:
            page.go('/kibali')
        # condition ya kufungua VIEW ya settings
        elif chs == 2:
            page.go("/settings")
        # condition ya kufungua dialogy ukibonyeza "EXIT "
        elif chs == 5:
            dalog.open = True
            dalog.update()

    # function ya kuhandle ukishaclick button ya kutuma request kwa mlizni ukitak kuingia
    def send_in(e):
        send_request_url = 'http://127.0.0.1:8000/parking_record/user-parking-request/'
        send_request = requests.post(url=send_request_url, data={"user_id": user_id})
        if send_request.status_code == 201:
            page.bottom_sheet = BottomSheet(
                open=True,
                enable_drag=True,
                show_drag_handle=True,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(value="REQUST SENT"),
                        Row(
                            controls=[
                                Text(value="mesage:"),
                                Text(value="Please wait your response")
                            ]
                        )
                    ]
                )
            )
            page.update()
            sign_out_btn.disabled = False
            sign_out_btn.update()
        else:
            print(f" Request do not sent:{send_request.status_code}")

    def send_out(e):

        out_req_url = 'http://127.0.0.1:8000/parking_record/sign-out/'
        out_req = requests.post(url=out_req_url, data={"user_id": user_id})
        if out_req.status_code == 200:
            print("mambo mengi natak kutoka mimi")
            page.dialog = CupertinoAlertDialog(
                open=True,
                title=Text(value="SIGHN-OUT REQUEst"),
                content=Column(
                    controls=[
                        Divider(height=12),
                        Text("You have sight-out"),
                        Text("Safe journey ")
                    ]
                )
            )

            #sign_out_btn.update()
            page.update()
            sign_out_btn.disabled = True
            sign_out_btn.update()
            time.sleep(5)
            sign_out_btn.disabled = False
            sign_out_btn.update()
        else:
            print(f"you are not in our parking list: {out_req.status_code}")

    # resposce_url = f'http://127.0.0.1:8000/parking_record/user-response/{user_id}/'
    # response = requests.get(url=resposce_url)
    #
    # if response.status_code == 200:
    #     message = response.json()
    #     print(message)
    #     page.dialog = CupertinoAlertDialog(
    #         open=True,
    #         title=Text(value="Response Reveiced:", color="blue"),
    #         content=Text(value=message['message'])
    #     )
    #     page.update()
    # if response.status_code == 202:
    #     message = response.json()
    #     page.dialog = CupertinoAlertDialog(
    #         open=True,
    #         title=Text(value="Response Reveiced:", color="blue"),
    #         content=Text(value=message['message'])
    #     )
    #     page.update()

    # if response.status_code == 401:
    #     message = response.json()
    #     print(message['message'])
    #     page.dialog = CupertinoAlertDialog(
    #         open=True,
    #         title=Text(value="Response Reveiced:", color="blue"),
    #         content=Text(value=message['message'])
    #     )
    #     page.update()
    #
    # else:
    #     print(response.status_code)

    # wee = Column()
    # lists = requests.get(f'http://127.0.0.1:8000/parking_record/details/{user_id}/')
    # for i in lists.json()['user_data']:
    #     f_name = lists.json()['first_name']
    #     l_name = lists.json()['last_name']
    #     reportTime = i['reportTime']
    #     departTime = i['departureTime']
    #     #
    #     # print(f_name)
    #     # print(l_name)
    #     # print(not reportTime)
    #     # print(departTime)
    #     wee.controls.append(
    #
    #         Container(
    #             bgcolor=colors.BLUE_GREY,
    #             height=30,
    #             content=Row(
    #             controls=[
    #                 Divider(height=20,color=colors.BLUE),
    #                 Text(value=f_name),
    #                 VerticalDivider(width=20,thickness=5,color=colors.WHITE),
    #                 Text(value=l_name),
    #                 VerticalDivider(width=20, thickness=5, color=colors.WHITE),
    #                 Text(value=reportTime),
    #                 VerticalDivider(width=20, thickness=5, color=colors.WHITE),
    #                 Text(value=departTime),
    #             ]),
    #
    #         )
    #     )
    #
    # # print(f_name)
    # # print(l_name)
    # print(reportTime)
    # print(departTime)

    image = 'assets/images/splash_dark_android.png'

    with open(image, "rb+") as image_file:
        image_data = image_file.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")
        # print(encoded_image)

    sign_out_btn = FilledButton(
        #disabled=True,
        text="sign-out",
        on_click=lambda e: send_out(e)
    )
    return View(
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        appbar=AppBar(
            toolbar_height=100,
            bgcolor=colors.BLUE,
            title=Text(
                value="CBE PARKING",
                size=35,
                weight=FontWeight.BOLD),
            center_title=True,
            color=colors.BLACK
        ),
        # Widget ya drawer inayofungukia pembeni
        drawer=NavigationDrawer(
            shadow_color="orange",
            indicator_color=colors.BLACK12,
            on_change=change,
            selected_index=-1,
            controls=[
                Container(
                    height=150,
                    bgcolor=colors.BLUE_GREY,
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Container(
                                width=100,
                                height=100,
                                border_radius=border_radius.all(50),
                                content=Image(
                                    fit=ImageFit.COVER,
                                    src_base64=encoded_image,
                                )

                            ),
                            Text(value="COLLAGE OF BUSSINESS EDUCATION",
                                 color=colors.BLACK,
                                 size=15,
                                 weight=FontWeight.BOLD
                                 )
                        ]
                    )

                ),
                NavigationDrawerDestination(
                    icon_content=Row(controls=[Icon(icons.ACCOUNT_CIRCLE), Text(value="Account")])),
                Divider(height=1),
                NavigationDrawerDestination(
                    icon_content=Row(controls=[Icon(icons.REQUEST_PAGE_OUTLINED), Text(value="Permit Application")])),
                Divider(height=1),
                NavigationDrawerDestination(icon_content=Row(controls=[Icon(icons.SETTINGS), Text(value="setting")])),
                Divider(height=1),
                NavigationDrawerDestination(icon_content=Row(controls=[Icon(icons.COMMENT), Text(value="Contents")])),
                Divider(height=1),
                NavigationDrawerDestination(
                    icon_content=Row(controls=[Icon(icons.INFO_ROUNDED), Text(value="About Us")])),
                Divider(height=30),
                NavigationDrawerDestination(icon_content=Row(controls=[Icon(icons.EXIT_TO_APP), Text(value="EXIT")])),
            ]
        ),
        controls=[
            Container(
                height=page.height / 1.3,
                width=page.width,
                #bgcolor=colors.AMBER,
                content=Column(
                    controls=[
                        Text(value="acha mapepe wewe Dogo", visible=True),
                        dalog,
                        TextButton(text="go back", on_click=lambda e: backregister(e)),
                        #wee
                    ]
                )
            ),
            Row(
                alignment=MainAxisAlignment.CENTER,
                spacing=50,
                controls=[
                    FilledButton(
                        # Button ya kusend request kwa mlinzi unatka kuingia
                        text="sign-in",
                        on_click=lambda e: send_in(e)
                    ),
                    sign_out_btn

                ]
            )

        ]
    )
