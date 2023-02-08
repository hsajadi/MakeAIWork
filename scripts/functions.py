#!/usr/local/bin/python3

def sum(param1, param2):
    """
    Deze functie berekent de som van twee getallen:
    param1 + param2
    """
    print(param1, " plus ", param2, " = ", param1+param2)

    return param1+param2

print(sum.__doc__)
sum(15,12)



# def mal(param1, param2):
#     """
#     deze functie berekent de mal van twee getallen:
#     param1 * param2
#     """
#     print(param1, "mal", param2, " = ", param1*param2)

#     return param1*param2

# print(mal.__doc__)
# mal(15,12)



from math import sqrt

print(sqrt(4))
