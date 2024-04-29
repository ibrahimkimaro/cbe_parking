import base64
import os.path
import uuid
from flet import *
import requests

def my_account(page: Page):
    user_id = page.client_storage.get("user_id")
    print(f"******{user_id}")

    # access_token = page.client_storage.get("access_token")
    # print(email)
    # print(f"THE ACCESS TOKEN: {access_token}")

    def backhome(e):
        page.go('/home')

    def add_account(e):
        print("i want to add an account")
        page.bottom_sheet = BottomSheet(
            maintain_bottom_view_insets_padding=True,
            open=True,
            use_safe_area=True,
            show_drag_handle=True,
            enable_drag=True,
            content=Column(
                controls=[
                    Container(
                        content=Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    Row(
                                        controls=[
                                            profile_picture2,
                                            Column(
                                                controls=[
                                                    Text(value=f"{data['first_name']} {data['last_name']}", size=15),
                                                    Text(value=f"{data['email']}", size=15),
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                Icon(icons.VERIFIED_ROUNDED, color=colors.PINK)
                            ]
                        )
                    ),
                    Divider(height=20),
                    Container(
                        on_click=lambda _: page.go('/register'),
                        content=Row(
                            controls=[
                                Icon(icons.ADD_CIRCLE_OUTLINE_ROUNDED),
                                Text(value="Add account", size=15)
                            ]
                        )
                    )
                ]
            )

        )
        page.update()

    def logout(e):
        request = requests.post(url='http://127.0.0.1:8000/authent/logout/')
        if request.status_code == 200:
            page.client_storage.remove("email")
            # page.update()
            # page.client_storage.remove("auth_token")
            page.go('/login')
            print("YOU HVAE LOG OUT")
        else:
            print(request.status_code)

    # names,email_,phone_no this is initialization and i pass all in page to display. i initializer here because
    #  BECAUSER => i want to pass the response data from database django and display here
    names = Text(
        style=TextStyle(
            size=15,
            color=colors.PINK,
            italic=True,
            weight=FontWeight.BOLD
        )
    )
    email_ = Text(
        style=TextStyle(
            size=15,
            color=colors.PINK,
            italic=True,
            weight=FontWeight.BOLD
        )
    )

    phone_no = Text(
        style=TextStyle(
            size=15,
            color=colors.PINK,
            italic=True,
            weight=FontWeight.BOLD
        )
    )
    # this is block that veryfy an email to django and returns the data like fitsnam_lstname_phon_numb,id etc

    # Hii ni Avatr ya profile picture NO #1
    profile_picture = Image(
        #color=colors.BLUE,
        border_radius=border_radius.all(120),
        aspect_ratio=1,
        expand_loose=False,
        expand=True,
        #max_radius=200,
        visible=True
    )
    # Hii ni Avatr ya profile picture NO #2 it founded in the function of add_account
    profile_picture2 = Image(
        width=50,height=50,
        border_radius=border_radius.all(10)
    )
    image = Image()
    if user_id:
        response = requests.get(url=f'http://127.0.0.1:8000/authent/registeredData/{user_id}/')
        if response.status_code == 200:
            data = response.json()
            names.value = data['first_name'] + " " + data['last_name']
            email_.value = data['email']
            phone_no.value = data['phone_number']
            user_id = data['id']
            imag = requests.get(url=f'http://127.0.0.1:8000/userprofile/userProfile_details/{user_id}',)
            if imag.status_code == 200:
                data_i = imag.json()['profile_pic']
                print(f"The realr path is: {os.path.abspath(data_i)}")
                # data_e = imag.json()['profile_pic']
                # mage_data = imag.content
                # base64_encoded_data = base64.b64encode(data_i)
                # base64_encoded_strin = base64_encoded_data.decode('utf-8')
                profile_picture2.src_base64 =  f"http://127.0.0.1:8000/{data_i}"
                url = 'images/profile_pic/20240105_205953_6bE1Cg7.jpg'
                #res = requests.get(url=url)
                with open(url, "rb+") as image_file:
                    image_data = image_file.read()
                    encoded_image = base64.b64encode(image_data).decode("utf-8")
                print(encoded_image)
                profile_picture.src_base64 = encoded_image

            else:
                image_url = 'http://127.0.0.1:8000/api/default-image/'
                #print(image_url)
                response = requests.get(image_url)
                image_data = response.content
                base64_encoded_data = base64.b64encode(image_data)
                base64_encoded_string = base64_encoded_data.decode('utf-8')
                #print(base64_encoded_string)
                profile_picture.src_base64 = base64_encoded_string
                profile_picture2.src_base64 = base64_encoded_string
        else:
            print(f"{response.status_code} Connection hakuna.")

    def image_file(e: FilePickerResultEvent):
        if e.files:
            file = e.files[0].path
            print(file)
            # wrt = open(file.name, "wb+")
            # print(wrt)

            print(file)
                # Update the database with the custom file name
            #try:
            file_path_2 = base64.b64encode(file.encode('utf-8'))
            file_path = file_path_2.decode('utf-8')
            print(file_path)
            image_upload = requests.patch(url=f'http://127.0.0.1:8000/userprofile/image/{user_id}/',
                                                  files={"profile_pic": file})
            if image_upload.status_code == 200:
                imag = requests.get(url=f'http://127.0.0.1:8000/userprofile/userProfile_details/{user_id}')
                if imag.status_code == 200:
                    data_i = imag.json()['profile_pic']
                    # hapa ita fanya image ijiupdate muda huo huo uliobdilisha picha
                    profile_picture2.src_base64 = f"http://127.0.0.1:8000/{data_i}"
                    profile_picture.src = f"http://127.0.0.1:8000/{data_i}"
                    profile_picture.update()
                else:
                    profile_picture.src_base64 = base64_encoded_string
                    profile_picture2.src_base64 = base64_encoded_string
                    print(imag.status_code)
                print("sucessfully uploading...")
            # else:
            #     pass
            # except FileNotFoundError:
            #     print(f"File not found at path: {file}")
            # except Exception as e:
            #     print(f"An error occurred: {e}")
            # with os.getcwd(file=file.path),file.path) as file_path:


            else:
                 print(image_upload.status_code)

    image_picker = FilePicker(
        on_result=image_file
    )
    page.overlay.append(image_picker)
    page.update()

    number_plate = TextField()

    def change_no(e):
        p_no_request = requests.patch(url=f"http://127.0.0.1:8000/userprofile/plate_number/{user_id}/",
                                      data={'plate_number': number_plate.value})
        if p_no_request.status_code == 200:
            response_plat_no = requests.get(url=f'http://127.0.0.1:8000/userprofile/userProfile_details/{user_id}')
            if response_plat_no.status_code == 200:
                no = response_plat_no.json()['plate_number']
                plate_numbers.value = no
                plate_numbers.update()
            else:
                plate_numbers.value = "Please Enter the plate number"
                plate_numbers.update()
            page.dialog.open = False
            page.update()
        else:
            print(f"namba haijakaa: {p_no_request.status_code}")

    def plate_number(e):
        page.dialog = CupertinoAlertDialog(
            open=True,
            title=Text(value="Update new plate Number"),
            content=number_plate,
            actions=[
                TextButton(text="Update", on_click=lambda e: change_no(e))
            ]
        )
        page.update()

    plate_numbers = Text(color=colors.ERROR, weight=FontWeight.BOLD)
    response_plat_no = requests.get(url=f'http://127.0.0.1:8000/userprofile/userProfile_details/{user_id}')
    if response_plat_no.status_code == 200:
        bu = response_plat_no.json()['plate_number']
        plate_numbers.value = bu
    else:
        pass

    return View(
        appbar=AppBar(
            title=Text("My Account"),
            center_title=True,
            bgcolor=colors.BLUE,
            toolbar_height=50,
            adaptive=True,
            actions=[IconButton(icon_color=colors.PINK, icon=icons.HOME, on_click=backhome)]
        ),
        route="/account",
        controls=[
            Container(
                alignment=alignment.center,
                #bgcolor=colors.AMBER,
                height=250,
                content=Column(
                    controls=[
                        profile_picture,
                        IconButton(icon=icons.IMAGE,
                                   on_click=lambda e: image_picker.pick_files(file_type=FilePickerFileType.IMAGE,
                                                                              dialog_title="Choose the profile picture"
                                                                              )),
                       # image
                    ]
                )
            ),
            Divider(height=12, opacity=0.2),
            Container(
                content=Row(
                    spacing=20,
                    controls=[
                        Icon(icons.PERSON),
                        Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                Text("Name"),
                                names
                            ]
                        )
                    ]
                )
            ),
            Divider(height=12, opacity=0.2),
            Container(
                content=Row(
                    spacing=20,
                    controls=[
                        Icon(icons.EMAIL),
                        Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                Text("Email"),
                                email_
                            ]
                        )
                    ]
                )
            ),
            Divider(height=12, opacity=0.2),
            Container(
                content=Row(
                    spacing=20,
                    controls=[
                        Icon(icons.PHONE),
                        Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                Text("phone"),
                                phone_no
                            ]
                        )
                    ]
                )
            ),
            Divider(height=12, opacity=0.2),
            Container(
                content=
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(

                            spacing=20,
                            controls=[
                                Icon(icons.CAR_CRASH),
                                Column(
                                    alignment=MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        Text("PLATE NUMBER", ),
                                        plate_numbers

                                    ]
                                )
                            ]
                        ),
                        TextButton("Change", on_click=lambda e: plate_number(e))
                    ]
                )
            ),
            Divider(height=12, opacity=0.2),
            Container(
                on_click=lambda e: add_account(e),
                content=Row(
                    controls=[
                        Icon(icons.SWITCH_ACCOUNT_SHARP),
                        Text(value="Add acccount")
                    ]
                )
            ),
            Container(height=6),
            Container(
                on_click=lambda e: logout(e),
                content=Row(
                    controls=[
                        Icon(icons.LOGOUT_ROUNDED),
                        Text(value="Log Out", color=colors.RED),
                    ]
                )
            )
        ]
    )
