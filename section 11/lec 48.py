
custom exception handling
class Error(Exception):
    pass

class dobException(Error):
    pass



year=int(input("enter the year"))
age=2026-year
try:
    if age<=30 and age>=20:
        print("okay registered")

    else:
        raise dobException
    
except dobException:
    print("sorry your age is not according to our preference")


year=2020
o/p-
sorry your age is not according to our preference


