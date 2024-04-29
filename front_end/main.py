from flet import *
import time
from Route import Routing
import asyncio


#from datetime import timezone,timedelta

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.platform = PagePlatform.ANDROID
    page.title = "CBE PARKING"

   # page.client_storage.clear()


    # page.splash = Container(
    #     alignment=alignment.center,
    #     content=Icon(icons.HOUSE, color=colors.BLUE, size=50)
    # )
    #
    # page.update()
    # time.sleep(0.5)
    # page.splash = None
    # page.update()


    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            Routing(page)[route.route]
        )

        page.update()

    def on_view(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = on_view



    # client_storage.contains_key("user_session_token"): HII imesetiwa kwenye registration,
    # Kama user aki register isaeve hivi taarifa ili akiingia tena ilimpeleke kwenye ergister page iend direct kwenye home page

    user_data = page.client_storage.get("user_identification_register")
    user_data2 = page.client_storage.get("user_identification_login")

    #
    # if page.client_storage.contains_key("home"):
    #     page.go('/home')
    # if page.client_storage.contains_key("guard_login"):
    #     page.go('/guard_login')

    #if user_data:

    # if user_data2:
    #     print("****** Imekubali AME LOGIN *****")
    #     page.go('/home')
    #     print(user_data2)
    #     page.client_storage.remove("user_identification_register")
    # else:
    #
    #     pas
    if user_data:

        print(user_data)
        if user_data == "Gurdian":

            print("****** Imekubali MImi ni mlinzi*****")
            page.go('/home_guard')
        else:
            pass
        if user_data == "Student" or user_data == "Staff":
            print("****** Imekubali Huyu ni student au Staff *****")
            page.go('/home')
    elif user_data2:
        print("****** Imekubali Huyu ni Amelogin *****")
        print(user_data2)
        page.go('/account')
    else:

        page.go('/step1')



app(target=main,
    assets_dir="assets",
    upload_dir="uploads",
    use_color_emoji=True
    )



