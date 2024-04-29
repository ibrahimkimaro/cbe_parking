import requests
from flet import *

url_user_request = 'http://127.0.0.1:8000/parking_record/mlinziview/'

user_request = requests.get(url=url_user_request)


def home_guard(page: Page):
    global get_user_info
    user_id = page.client_storage.get("security_user_id")

    names = Text(italic=True)
    if user_id:
        response = requests.get(url=f"http://127.0.0.1:8000/parking_record/user/{user_id}/")
        data = response.json()
        names.value = f"{data['first_name']} {data['last_name']}"

    # kama kweli ita leta hizo taarifa kutoka kwenye database za muusika else: ita hide maswali
    f_name = Row(controls=[Text("first name:", color="blue"),])
    l_name = Row(controls=[Text("last name:", color="blue"),])
    ph_number = Row(controls=[Text("phone number:", color="blue"),])
    status = Row(controls=[Text("status:", color="blue"),])
    p_no = Row(controls=[Text("plate number: ", color="blue"),])

    confirm_btn = TextButton(text="Confirm", on_click=lambda e: Prove_Request(e))
    reject_btn = TextButton(text="Reject", style=ButtonStyle(color=colors.RED), on_click=lambda e: Reject_Request(e))

    if user_request.status_code == 200:
        request = user_request.json()
        get_id = request['user']
        get_user = requests.get(url=f'http://127.0.0.1:8000/parking_record/specific-user/{get_id}/')
        if get_user.status_code == 200:
            get_user_info = get_user.json()
            f_name.controls.append(Text(value=get_user_info['first_name']))
            l_name.controls.append(Text(value=get_user_info['last_name']))
            ph_number.controls.append(Text(value=get_user_info['phone_number']))
            status.controls.append(Text(value=get_user_info['status']))
            p_no.controls.append(Text(value=get_user_info['plate_number']))

        else:
            f_name.visible = False
            l_name.visible = False
            ph_number.visible = False
            status.visible = False

            p_no.visible = False
            confirm_btn.visible = False
            reject_btn.visible = False
    else:
        pass




    def Prove_Request(e):
        url = f'http://127.0.0.1:8000/parking_record/mlinziApproveUser/{get_id}/'
        confirm = requests.get(url=url)
        if confirm.status_code == 200:
            print("You have Approved")
            page.dialog.open = False
            page.update()

        else:
            print(confirm.status_code)

    def Reject_Request(e):
        url = f'http://127.0.0.1:8000/parking_record/mlinziReject/{get_id}/'
        reject = requests.get(url=url)
        if reject.status_code == 200:
            print("Already Reject")
            page.dialog.open = False

            page.update()

        else:
            print(reject.status_code)



    def lists(e):
        if True:
            page.dialog = CupertinoAlertDialog(
                open=True,
                title=Text(value="user request:"),
                content=Column(
                    controls=[
                        f_name,
                        l_name,
                        ph_number,
                        status,
                        p_no,
                    ]
                ),
                actions=[
                    # This is button to approve user request
                    confirm_btn,
                    reject_btn
                ]
            )
            page.update()


    return View(
        appbar=AppBar(
            title=Text(value="GUARDIAN REQUEST"),
            center_title=True,
            bgcolor=colors.BLUE
        ),
        controls=[
            Row(
                controls=[
                    Text(value="The Guardian Shift:"),
                    names,
                ]
            ),
            IconButton(icon=icons.BACKUP, on_click=lambda _: page.go('/guard_login')),
            OutlinedButton(text="see the user requests", on_click=lambda e: lists(e))

        ]
    )
