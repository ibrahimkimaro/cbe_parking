import asyncio
from flet import *
import requests
import json
import hashlib
import os
import uuid

post_url = 'http://127.0.0.1:8000/authent/register/'

getData = requests.get('http://127.0.0.1:8000/authent/registeredData/')

auth_token_url_create = 'http://127.0.0.1:8000/authjwt/jwt/create/'
auth_token_url_refresh = 'http://127.0.0.1:8000/authjwt/jwt/refresh/'
auth_token_url_access = 'http://127.0.0.1:8000/authjwt/jwt/verify/'


class class_registration(Column):
    def __init__(self):
        super().__init__()
        #self.page.client_storage.clear()
        self.them = IconButton(icon=icons.LIGHT_MODE, on_click=self.changethem)
        self.registerBtn = FilledButton(
            text="Register",
            # 1:ya kutengeneza asyncio yet
            # Asynion inafanya dalay of time(millsecond/seccond) before take an action
            on_click=lambda e: asyncio.run(self.registerhere(self))
        )


        # PASSWORD 1 TEXTFIELS
        self.passwrd = TextField(
            width=400,
            label="PASSWORD",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            password=True,
            filled=True,
            can_reveal_password=True,
            suffix=Icon(icons.VERIFIED_SHARP, color=colors.BLUE, visible=False, size=20),
            on_change=lambda e: self.clear5(e)
        )
        # USERNAME TEXTFIELD
        self.first_name = TextField(
            width=400,
            label="FIRST NAME",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            keyboard_type=KeyboardType.NAME,
            suffix=Icon(icons.VERIFIED_SHARP, color=colors.BLUE, visible=False, size=20),
            on_change=lambda e: self.clear1(e)
        )
        self.last_name = TextField(
            width=400,
            label="LAST NAME",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            keyboard_type=KeyboardType.NAME,
            suffix=Icon(icons.VERIFIED_SHARP, color=colors.BLUE, visible=False, size=20),
            on_change=lambda e: self.clear2(e)
        )
        self.user_email = TextField(
            width=400,
            label="EMAIL",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            keyboard_type=KeyboardType.EMAIL,
            suffix=Icon(icons.VERIFIED_SHARP, color=colors.BLUE, visible=False, size=20),
            on_change=lambda e: self.clear3(e)
        )
        self.phoneNo = TextField(
            width=400,
            label="PHONE NUMBER",
            label_style=TextStyle(size=15, italic=True),
            border_radius=border_radius.all(12),
            input_filter=NumbersOnlyInputFilter(),
            prefix_text="+255 ",
            keyboard_type=KeyboardType.PHONE,
            max_length=9,
            suffix=Icon(icons.VERIFIED_SHARP, color=colors.BLUE, visible=False, size=20),
            on_change=lambda e: self.clear4(e)
        )
        self._icon = IconButton(
            icon=icons.EMOJI_EMOTIONS, icon_size=25,
            icon_color=colors.WHITE,
            # rotate=1,
            on_click=lambda e: self.anime(e),
            animate_rotation=animation.Animation(80, curve=AnimationCurve.BOUNCE_OUT)
        )
        self.happ = Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            #alignment="center",
            visible=False,
            controls=[
                Text(
                    weight=FontWeight.W_600,
                    value="YOU HAVE DONE SUCESSFULLY REGISTERED!!WELCOME",
                    color=colors.BLUE,
                ),
                self._icon
            ])

    def anime(self, e):
        if self._icon:
            # self._icon.rotate = Rotate(angle=2)
            # self._icon.update()
            while True:
                self._icon.rotate = Rotate(angle=1.3)
                self._icon.rotate = Rotate(angle=-1.3)
                self._icon.update()

    def clear1(self, e):
        if self.first_name.value:
            self.first_name.suffix.visible = False
            self.first_name.error_text = self.first_name.clean()
            self.first_name.update()

    def clear2(self, e):
        if self.last_name.value:
            self.last_name.suffix.visible = False
            self.last_name.error_text = self.last_name.clean()
            self.last_name.update()

    def clear3(self, e):
        if self.user_email.value:
            self.user_email.suffix.visible = False
            self.user_email.error_text = self.user_email.clean()
            self.user_email.update()

    def clear4(self, e):
        if self.phoneNo.value:
            self.phoneNo.suffix.visible = False
            self.phoneNo.error_text = self.phoneNo.clean()
            self.phoneNo.update()

    def clear5(self, e):
        if self.passwrd.value:
            self.passwrd.suffix.visible = False
            self.passwrd.can_reveal_password = True
            self.passwrd.error_text = self.passwrd.clean()
            self.passwrd.update()

    # Define baada ya ku click register btn yetu iende wap na ingaliw je data zimejazwa sahihi au
    async def registerhere(self, e):
        if True:
            if self.first_name:
                self.f_name = self.first_name.value
                if not self.f_name:
                    self.first_name.error_text = "Please fill and enter the Username"
                    self.first_name.suffix.visible = False
                    self.first_name.update()
                else:
                    await asyncio.sleep(0.5)
                    self.first_name.error_text = self.first_name.clean()
                    self.first_name.suffix.visible = True
                    print(f"First name: {self.f_name}")
                    self.first_name.update()
            if self.last_name:
                self.l_name = self.last_name.value
                if not self.l_name:
                    self.last_name.error_text = "Please fill and enter the Username"
                    self.last_name.suffix.visible = False
                    self.last_name.update()
                else:
                    await asyncio.sleep(0.5)
                    self.last_name.error_text = self.last_name.clean()
                    self.last_name.suffix.visible = True
                    print(f"last name: {self.l_name}")
                    self.last_name.update()
            if self.user_email:
                self.email = self.user_email.value
                if not self.email:
                    self.user_email.error_text = "Please fill and enter the Username"
                    self.user_email.suffix.visible = False
                    self.user_email.update()
                else:
                    await asyncio.sleep(0.5)
                    self.user_email.error_text = self.user_email.clean()
                    self.user_email.suffix.visible = True
                    print(f"Emai: {self.email}")
                    self.user_email.update()

            if self.phoneNo:
                self.user_phone = self.phoneNo.value
                if not self.user_phone:
                    self.phoneNo.error_text = "Please fill and enter your phone number"
                    self.phoneNo.suffix.visible = False
                    self.phoneNo.update()
                elif len(self.phoneNo.value) <= 8:
                    self.phoneNo.error_text = "Phone number must be 9 digits"
                    self.phoneNo.suffix.visible = False
                    self.phoneNo.update()
                else:
                    await asyncio.sleep(0.5)
                    self.phoneNo.error_text = self.phoneNo.clean()
                    self.phoneNo.suffix.visible = True
                    print(f"phone_number:{self.user_phone}")
                    self.phoneNo.update()

            if self.radio:
                if self.student.value == self.radio.value:
                    self.status = self.student.value
                    print(f"status: {self.status}")
                if self.Staff.value == self.radio.value:
                    self.status = self.Staff.value
                    print(f"status: {self.status}")
                if self.gurdian.value == self.radio.value:
                    self.status = self.gurdian.value
                    self.dropdownMenu.options = None
                    self.user_statOptn = "security"
                    self.dropdownMenu.update()
                    print(f"status:{self.status}")

            if self.dropdownMenu.options:
                self.user_statOptn = self.dropdownMenu.value
                if self.user_statOptn:
                    await asyncio.sleep(0.5)
                    self.dropdownMenu.error_text = self.dropdownMenu.clean()
                    self.dropdownMenu.suffix.visible = True
                    self.dropdownMenu.update()
                    print(f" THE STATUS TYPE IS: {self.user_statOptn}")
                else:
                    self.dropdownMenu.suffix.visible = False
                    self.dropdownMenu.update()

            if self.passwrd:
                self.user_password = self.passwrd.value
                if not self.user_password:
                    self.passwrd.error_text = "Please fill the Password field"
                    self.passwrd.suffix.value = False
                    self.passwrd.update()
                elif not any(char.isnumeric() for char in self.user_password):
                    self.passwrd.error_text = "Password must contain alphabet and number "
                    self.passwrd.suffix.visible = False
                    self.passwrd.update()
                else:
                    await asyncio.sleep(0.5)
                    self.passwrd.suffix.visible = True
                    self.passwrd.can_reveal_password = False
                    self.passwrd.error_text = self.passwrd.clean()
                    self.passwrd.update()
                    print(f"Your password : {self.user_password}")

            # hizi nd dictionary yetu inayounda JSON data zinazo pass kweyny django serilizers.py and model.py and kept in database
            # nime declare hapa hap ili kuungansha API_endpoint za files zote zije hapa nda niziweke kwny data ya response

            data = {
                "first_name": self.f_name,
                "last_name": self.l_name,
                "email": self.email,
                "phone_number": self.user_phone,
                "status": self.status,
                "status_type": self.user_statOptn,
                "password": self.user_password
            }
            # HII ndo main API point inayo unganisha na database/django backend
            # url= post_url ni ulr that i have been defined at top in my code and it help to direct the info on the django sever
            # DATA=data data hizi ni det of dictionary key and value tunazo weka kweny database expample {"username":"kimmy"}, huandika kawa double quotes

            response = requests.post(url=post_url, data=data)
            if response.status_code == 201:
                ## Here we implent if the requrst is true to register the condition belowe send  to create the JWT Token(access and refresh)
                # Data_create_token => this is json data user enail and password and use to create the authentication tokens
                # data_create_token={"email":self.email,
                #                    "password":self.user_password
                #                    }
                # req_auth_token = requests.post(url=auth_token_url_create,data=data_create_token)
                # if req_auth_token.status_code == 200:
                #     print("the token has been created already")
                #     self.response_token = req_auth_token.json()
                #     # we have reseve the refresh token and access token....next to implent the access authorization to user
                #     #if later we can implement manually the refrsh token to refresh the access token and the the access token work
                #     print(f"Refresh_token: {self.response_token['refresh']}" + "\n" f"Access_token: {self.response_token['access']}")
                #     headers = {"Authorization":f"Bearer {self.response_token['access']}"}
                #     data_access = {"token":self.response_token['access']}
                #     make_acces = requests.post(url=auth_token_url_access,data=data_access,headers=headers)
                #     if make_acces.status_code == 200:
                #         print("**********You have get an Access to your account**************")
                #     elif make_acces.status_code == 401:
                #         # Here you can implent reffesh oken to refresh new access token
                #         print("****** The Token has expired********")
                #     else:
                #         print(f"****{make_acces.status_code}...You dont have an access****")
                #
                # else:
                #     print(f"{req_auth_token.status_code}The token have not created")
                self.page.snack_bar = SnackBar(open=True,
                                               content=Text(
                                                   value="Welcome!! Successfully you have registerd",
                                                   color=colors.BLACK,
                                                   weight=FontWeight.BOLD),
                                               bgcolor=colors.BLUE)
                self.page.client_storage.set("email", self.email)
                self.page.client_storage.set("password", self.user_password)
                self.page.client_storage.set("user_identification_register", self.radio.value)
                # token = str(uuid.uuid4())

                #self.page.client_storage.set("access_token",self.response_token['access'])
                self.page.update()
                if self.radio.value == self.gurdian.value:
                    await asyncio.sleep(3)
                    self.page.go('/guard_login')
                    #self.page.client_storage.set("guard_login", self.gurdian.value)

                else:
                    await asyncio.sleep(3)
                    self.page.go('/home')
                    token2 = str(uuid.uuid4())
                    self.page.client_storage.set("home", token2)
                print("***********User registration sucessfully!***********")

            # hre we store the username and harsh password in client_storage in flet built-in
            # self.email in value whn user register and hashed_password = tumeita function ya kuencrypt password yetu
            else:
                self.page.snack_bar = SnackBar(open=True,
                                               content=Text(
                                                   value="The email does exist",
                                                   color=colors.BLACK,
                                                   weight=FontWeight.BOLD,
                                                   size=25),
                                               padding=padding.only(left=500),
                                               bgcolor=colors.RED)
                self.page.update()
                print("************User registration NOT sucessfully!*************")
                print(f"Error:{response.status_code} Code")
            # hashed_password = self.harsh_password()

    # hii ndo function inayo weza kuencrypt password etu
    # def harsh_password(self):
    #     if self.user_password:
    #         # Create a random salt
    #         salt = os.urandom(16)
    #         # Has the self.user_password with the salt
    #         hashed_password = hashlib.pbkdf2_hmac(hash_name='sha256',password=self.user_password.encode('utf-8'),salt=salt,iterations=2222)
    #         return salt + hashed_password
    def lognpage(self, e):
        self.page.go('/login')

    # Functuion inayoofanya kazi ya kubadilisha thems kwny page either light or dark
    def changethem(self, e):
        if self.page.theme_mode == "light":
            print("dark to light")
            self.them.icon = icons.LIGHT_MODE
            self.page.theme_mode = "dark"
            self.page.update()
            self.update()
        else:
            self.them.icon = icons.DARK_MODE
            self.page.theme_mode = "light"
            print("light to dark ")
            self.page.update()
            self.update()

    # Function inayo weka condtion kam mtu user akiwa n student au employee na kumletea machaguo yake
    def showStatus(self, e):
        # Hapa tunacheck kama radio value ni sawa sawa na student value..studnt value ni "student"
        if self.radio.value == self.student.value:
            # Hapa tukachange color ya radio ya student
            self.student.active_color = colors.PINK
            # HApa tuaicall dropdown meny wte ili tupass the optionns
            self.dropdownMenu.visible = True
            self.dropdownMenu.label = "CORSE"
            self.dropdownMenu.options = [dropdown.Option("INFORMATION AND COMMUNICATION TECHNOLOGY(ICT)"),
                                         dropdown.Option("METROLOGY AND STANDADIZATION"),
                                         dropdown.Option("BUSINESS ADMINISTARTON(BA)"),
                                         dropdown.Option("ACCOUNTANCY"),
                                         dropdown.Option("MARKETING"),
                                         dropdown.Option("HUMAN RESOURSES(HR)"),
                                         ]
            self.update()

        # Hapa tunacheck kama radio value ni sawa sawa na employee value..employee value ni "employee"
        if self.radio.value == self.Staff.value:
            # Hapa tukachange color ya radio ya student
            self.Staff.active_color = colors.GREEN
            # HApa tuaicall dropdown meny wte ili tupass the optionns
            self.dropdownMenu.visible = True
            self.dropdownMenu.label = "Department"
            self.dropdownMenu.options = [dropdown.Option("MATHEMATICS AND ICT"),
                                         dropdown.Option("DEPARTMENT OF ACCOUNTANTS"),
                                         dropdown.Option("DEPARTMENT OF MARKETING"),
                                         dropdown.Option("HUMAN RESOURES"),
                                         ]
            self.update()
        if self.radio.value == self.gurdian.value:
            self.gurdian.active_color = colors.GREEN
            self.dropdownMenu.visible = False
            self.update()

    # Hii ndo main function yetu inayo desplay kila kitu kweny page yetu

    def build(self):
        self.student = Radio(label="Student", value="Student")
        self.Staff = Radio(label="Staff", value="Staff")
        self.gurdian = Radio(label="Gurdian", value="Gurdian")
        # self.radio ndo control yetu inayo fanya radio change na ku holds the radios student and emplyee
        self.radio = RadioGroup(
            on_change=self.showStatus,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    self.student,
                    self.Staff,
                    self.gurdian
                ]
            )
        )

        # HII NDO MAIN DROPDown MENU ETU thte CURRENT WIDGET HERE
        self.dropdownMenu = Dropdown(
            suffix=Icon(icons.VERIFIED_SHARP, color=colors.BLUE, visible=False, size=20),
            width=400,
            visible=True,
            text_size=12,
            options=[
                # here we need to pass the options dropdown.Option('ICT')
                # so we hav ma eit empy and we call it in outer condion within the function sho_status()
                # AND SHOSTATUS()function is a on_chnage event within our radiogrop in self.Radio
                # ADN RADIOGROUP is a radiio buttn  let people select a single option from two or more choices.

            ]
        )

        return [
            self.them,
            Column(
                on_scroll="auto",
                scroll=ScrollMode.AUTO,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        value="REGISTER HERE",
                        size=40,
                        style=TextThemeStyle.TITLE_LARGE,
                        overflow=TextOverflow.FADE,
                        weight=FontWeight.BOLD
                    ),
                    Divider(height=20),
                    self.first_name,
                    self.last_name,
                    self.user_email,
                    self.phoneNo,
                    self.radio,
                    self.dropdownMenu,
                    self.passwrd,
                    self.registerBtn,
                    self.happ,
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value="I have already an account"),
                            TextButton(text="Log in ", on_click=self.lognpage)
                        ]
                    )
                ]
            )
        ]


def register(page: Page):
    return View(
        route='/register',
        controls=[
            class_registration()
        ]
    )
