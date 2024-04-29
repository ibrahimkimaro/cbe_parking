from flet import *


def settings(page: Page):
    def backhome(e):
        page.go('/home')

    def change_them(e):
        vlm = e.control.value
        if vlm == "light_mode":
            page.theme_mode = "light"

            light_mode_radio.update()
            page.update()
            print("it a light mode button")

        elif vlm == "dark_mode":
            page.theme_mode = "dark"
            page.update()
            print("it is a dark mode radio")

    light_mode_radio = Radio(value="light_mode")
    dark_mode_radio = Radio(value="dark_mode")

    return View(
        route="settings",
        appbar=AppBar(
            bgcolor=colors.BLUE,
            leading=IconButton(icon=icons.ARROW_BACK, on_click=backhome, icon_color=colors.DEEP_ORANGE_200),
            title=Text(value="Settings"),
            actions=[
                IconButton(icon=icons.HOME, on_click=backhome, icon_color=colors.BROWN)
            ]
        ),
        controls=[
            Text(value="Them:"),
            Container(height=5),
            Container(
                content=RadioGroup(
                    on_change=lambda e: change_them(e),
                    content=Column(
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Row(
                                        controls=[
                                            Icon(icons.LIGHT_MODE),
                                            Text(value="Light"),
                                        ]
                                    ),
                                    light_mode_radio
                                ]
                            ),
                            Container(height=5),
                            Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Row(
                                        controls=[
                                            Icon(icons.DARK_MODE_OUTLINED),
                                            Text(value="Dark"),
                                        ]
                                    ),
                                    dark_mode_radio
                                ]
                            )
                        ]
                    )
                )
            ),
            Divider(height=5)

            # IconButton(icon=icons.LIGHT_MODE, tooltip="light", on_click=lambda e: light_them(e)),
            # IconButton(icon=icons.DARK_MODE, tooltip="dark", on_click=lambda e: dark_them(e))

        ]
    )
