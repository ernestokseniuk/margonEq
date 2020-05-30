import requests
from bs4 import BeautifulSoup
import time

import  random
chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','V','T','Z','1','2','3','4','5','6','7','8','9','0']
def generate():
    genCode = ""
    for i in range(32):
        genCode += chars[random.randint(0,len(chars)-1)]

    return (genCode)

def checkCode(verCode,profile):
    if "margonem" in profile:
        if "new" not in profile:
            if "#2" not in profile:
                profile = str(profile) + "#tab2"
        page = requests.get(profile)
        soup = BeautifulSoup(page.content,'html.parser')
        time.sleep(0.1)
        if verCode in soup.text:
            return True
        else:
            return False
    else:
        return False