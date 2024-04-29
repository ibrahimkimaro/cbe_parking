from flet import *

def _step1(page:Page):
    def on_skip(e):
        page.go('/register')


    return View(
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            Card(
                width=300,
                height=300,
                color=colors.BLUE,
                content=Column(
                   controls=[
                       Container(
                           margin=margin.only(left=40,top=10),
                           content=Text(
                               value="CBE PARKING ",
                           overflow=TextOverflow.FADE,
                               style=TextStyle(
                                   size=20,
                                   weight="bold",
                                   color=colors.BLACK,
                               ),
                           )
                       ),
                       Divider(height=12)
                   ]
                )
            ),
            TextButton(text="Skip..",on_click=lambda e:on_skip(e)),
            TextButton(text="Next..",on_click=lambda e:page.go('/step2'))
        ]
    )
