from flet import *


def main(page:Page):

    page.add(Text(f"initila {page.route}"))

    def onchn():
        page.add(Text(f"final {page.route}"))
        page.update()

    def go_to():
        page.route = "/Shop"
        page.update()

    page.on_route_change = onchn
    page.add(TextButton(text="nenda",on_click=go_to))

app(target=main)