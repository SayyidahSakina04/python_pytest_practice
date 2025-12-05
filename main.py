# def get_temperature(temp):
#     if temp > 20:
#         return "hot"
#     else:
#         return "cold"

def add(temp1, temp2):
    return temp1 + temp2

def divide(temp1, temp2):
    if temp2 == 0:
        raise ValueError("Can not divide by ZERO")
    return temp1 / temp2