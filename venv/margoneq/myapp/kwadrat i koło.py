import math
kw = 200
ok_x = 100
ok_y = 100
try:
    punkt_x,punkt_y = input("podaj x y punktu ").split(" ")
    punkt_x = int(punkt_x)
    punkt_y = int(punkt_y)
    def sprawdzobw(punkt_x,punkt_y,ok_x = 100,ok_y = 100):
        if math.sqrt((ok_x-punkt_x)**2 + (ok_y-punkt_y)**2) == 100:
            return True
    def sprawdzok(punkt_x,punkt_y,ok_x = 100,ok_y = 100):
        if math.sqrt((ok_x-punkt_x)**2 + (ok_y-punkt_y)**2) < 100:
            return True
    def sprawdzkw(punkt_x,punkt_y,kw_a=200):
        if punkt_x > 0 and punkt_x < 200 and punkt_y > 0 and punkt_y < 200:
            return True
    def sprawdzkwobw(punkt_x, punkt_y, kw_a=200):
        if punkt_x == 200 and punkt_y <= 200 or punkt_y == 200 and punkt_x <= 200:
            return True
    if sprawdzok(punkt_x,punkt_y):
        print("Punkt mieści się w okręgu opisanym na kwadracie")
    elif sprawdzobw(punkt_x,punkt_y):
        print("Punkt mieści się na obwodzie okręgu opisanego na kwadracie")
    elif sprawdzkw(punkt_x,punkt_y):
        print("Punkt mieści się w kwadracie, ale nie jest położony na okręgu")
    elif sprawdzkwobw(punkt_x,punkt_y):
        print("Punkt mieście się na obowdzie kwadratu")
    else:
        print("Punkt jest hen hen daleko")

except:
    print("Błędny input")