from flet import *
from Authentication.Registration import register
from Authentication.login import login
from Authentication.forget_password import forgetPassword
from home_page import home
from Account import my_account
from Setting import settings
from Kibali_page1 import kibali_page1
from onBoarding_pages.step1 import _step1
from onBoarding_pages.step2 import _step2
from guard_list import guard_login
from guard_home import home_guard

def Routing(page):
    return {
        '/register': register(page),
        '/login': login(page),
        '/forget_password': forgetPassword(page),
        '/home': home(page),
        '/account': my_account(page),
        '/settings': settings(page),
        '/kibali': kibali_page1(page),
        '/step1': _step1(page),
        '/step2': _step2(page),
        '/guard_login': guard_login(page),
        '/home_guard': home_guard(page)
    }
