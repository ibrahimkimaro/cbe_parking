from flet import *


def _step2(page: Page):

    return View(
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            Text(value="this onBording of step 2 "),
            TextButton(text="Let's Go", on_click=lambda e:page.go('/register'))
        ]
    )
