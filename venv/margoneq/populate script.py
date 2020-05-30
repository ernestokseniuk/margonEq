import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','margoneq.settings')

import django
django.setup()


## FAKE POP SCRIPT

import  random
from myapp.models import verifyCodes


chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','V','T','Z','1','2','3','4','5','6','7','8','9','0']
def populate(N=5):

    for entery in range(N):
        genCode = ""
        for i in range(32):
            genCode += chars[random.randint(0,len(chars)-1)]

        codeQuery = verifyCodes.objects.get_or_create(code= genCode, inUse = False)
        print(genCode)

if __name__ == "__main__":
    populate(1000)