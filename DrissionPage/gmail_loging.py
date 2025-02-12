from time import sleep
from DrissionPage import ChromiumPage,ChromiumOptions,errors
from random import randint
from mahdix import clear,search_as_re
#VFS Global is 374348.
clear()

_gmail_name='' # your gmail numer or gmail name
_gmail_pass='' # gmail pasword

op=ChromiumOptions()
# op.set_paths(local_port=randint(2550,9999))
driver=ChromiumPage(addr_or_opts=op)
driver.clear_cache()

def working(name_path=None,input_text=None,timeout=2):
    try:
        return driver(name_path,timeout=timeout).input(input_text) if name_path and input_text else driver(name_path,timeout=timeout).click()
    except Exception as e :
        pass
        return e


driver.get('https://accounts.google.com')
driver._wait_loaded()
working('@id=identifierId',_gmail_name)
working('text=Next',timeout=5)
driver._wait_loaded()
working('@name=Passwd',_gmail_pass)
driver.wait(2)
working('text=Next',timeout=5)
driver._wait_loaded()
working('এখন না')
working('বাতিল করুন',timeout=2)
working('এখন না',timeout=1)
