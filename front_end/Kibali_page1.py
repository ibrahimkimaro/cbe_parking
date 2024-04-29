from flet import *

def kibali_page1(page: Page):
    _con = Container(
        width=100,
        height=80,
        bgcolor="balck"
    )

    def file_result(e: FilePickerResultEvent):
        if e.files:
            print("ubwabwa")
            for file in e.files:
                print(file)
                _con.image_src = (", ".join(map(lambda f: f.name, e.files)))
                _con.update()

    file_pick = FilePicker(on_result=lambda e: file_result(e))

    def choose_image(e):
        print("Unahitajikaku uplode passport ako")
        file_pick.pick_files(dialog_title="choose Image", file_type=FilePickerFileType.ANY)

    # funtion ya kutriger button kutudi home_page
    def back_home(e):
        page.go('/home')

    def see(e):
        muss = e.control.value
        if muss == "male":
            print("mimi ni mwanaume bana")
        elif muss == "female":
            print("mimi ni msichicana")

    # View ya sehemu ya kuombea kibali cha kupaki usafiri BE
    return View(
        scroll=ScrollMode.HIDDEN,
        route='/kibali',
        appbar=AppBar(
            bgcolor=colors.BLUE,
            title=Text(
                weight=FontWeight.BOLD,
                overflow=TextOverflow.ELLIPSIS,
                value="MAOMBI YA KIBALI",
                size=30,
                color=colors.BLACK
            ),
            toolbar_height=80,
            center_title=True,
            actions=[
                IconButton(icon_color=colors.PINK, icon=icons.HOME, on_click=back_home, tooltip="HOME")
            ]
        ),
        controls=[
            file_pick,
            Column(

                # horizontal_alignment="center",
                controls=[
                    Text(
                        weight=FontWeight.BOLD,
                        overflow=TextOverflow.ELLIPSIS,
                        value="PERSON INFOMATION",
                        size=20
                    ),
                    Divider(height=15),
                        Column(
                            scroll=ScrollMode.AUTO,
                            controls=[
                                TextField(
                                    # content_padding=padding.only(),
                                    width=300,
                                    height=50,
                                    border_radius=border_radius.all(15),
                                    label="first name",
                                    label_style=TextStyle(size=15),
                                    cursor_height=20,
                                    text_style=TextStyle(font_family="Times new roman"),
                                    autocorrect=True,
                                    capitalization=TextCapitalization.CHARACTERS,
                                    filled=True,
                                    enable_suggestions=True,
                                    dense=True,
                                    visible=True,
                                    smart_quotes_type=True,
                                ),
                                Container(height=5),
                                TextField(
                                    width=300,
                                    height=50,
                                    text_style=TextStyle(size=15, font_family="Times new roman"),
                                    label="middle name",
                                    label_style=TextStyle(size=15),
                                    autocorrect=True,
                                    capitalization=TextCapitalization.CHARACTERS,
                                    filled=True,
                                    cursor_height=20,
                                    enable_suggestions=True,
                                    border_radius=15,
                                    dense=True,
                                    visible=True,
                                    smart_quotes_type=True,
                                ),
                                Container(height=10),
                                TextField(
                                    width=300,
                                    height=50,
                                    text_style=TextStyle(size=15, font_family="Times new roman",
                                                         weight=FontWeight.BOLD),
                                    label="last name",
                                    label_style=TextStyle(size=15),
                                    autocorrect=True,
                                    capitalization=TextCapitalization.CHARACTERS,
                                    filled=True,
                                    cursor_height=20,
                                    enable_suggestions=True,
                                    border_radius=15
                                ),
                                Container(height=10),
                                TextField(
                                    width=300,
                                    height=50,
                                    text_style=TextStyle(size=15, font_family="Times new roman",
                                                         weight=FontWeight.BOLD),
                                    label="phone number",
                                    label_style=TextStyle(size=15),
                                    autocorrect=True,
                                    capitalization=TextCapitalization.CHARACTERS,
                                    filled=True,
                                    cursor_height=20,
                                    enable_suggestions=True,
                                    border_radius=15
                                ),
                                Container(height=10),
                                TextField(
                                    width=300,
                                    height=50,
                                    text_style=TextStyle(size=15, font_family="Times new roman",
                                                         weight=FontWeight.BOLD),
                                    label="Registration number",
                                    label_style=TextStyle(size=15),
                                    autocorrect=True,
                                    capitalization=TextCapitalization.CHARACTERS,
                                    filled=True,
                                    cursor_height=20,
                                    enable_suggestions=True,
                                    border_radius=15
                                ),
                                Container(height=10),
                                Text(value="GENDER:"),
                                TextField(
                                    width=300,
                                    height=50,
                                   # text_style=TextStyle(size=15, font_family="Times new roman",
                                                       #  weight=FontWeight.BOLD),
                                    label="CORSE / DEPARTMENT",
                                   label_style=TextStyle(size=12),
                                   # autocorrect=True,
                                  #  capitalization=TextCapitalization.CHARACTERS,
                                   # filled=True,
                                    text_size=14,
                                    #cursor_height=20,
                                    border="underline"
                                    #border_radius=15
                                ),
                                RadioGroup(
                                    on_change=lambda e: see(e),
                                    content=Row(
                                        controls=[
                                            Radio(value="male", label="male"),
                                            Radio(value="female", label="female")
                                        ]
                                    )
                                ),
                                Text(value="PASSPORT SIZE", color=colors.BLACK, weight=FontWeight.BOLD),
                                _con,
                                Row(
                                    controls=[
                                        ElevatedButton(text="camera"),
                                        ElevatedButton(text="gallaey", on_click=lambda e: choose_image(e)),
                                    ]
                                ),
                                Text(value="LESSENCE PICTURE"),
                                Row(
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            width=400,
                                            height=200,
                                            bgcolor=colors.CYAN_700,
                                            content=Text(value="PICHA KWA YA LESENI UPANDE WA MBELE",
                                                         color=colors.BLACK, weight="bold")
                                        ),
                                        Container(
                                            alignment=alignment.center,
                                            width=400,
                                            height=200,
                                            bgcolor=colors.PINK,
                                            content=Text(value="PICHA YA LESENI KWA UPANDE WA nyuma",
                                                         color=colors.BLACK, weight="bold")
                                        )
                                    ]
                                ),
                            ]
                        )
                ]
            )
        ]
    )
