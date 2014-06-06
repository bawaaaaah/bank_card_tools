#! /usr/bin/env python
# -*- coding:utf-8 -*-
from random import SystemRandom


def luhn(cardNumber):
    result = 0
    cardNumber = str(cardNumber)
    tmp = (len(cardNumber) % 2 == 1)
    for n in cardNumber:
        n = int(n)
        tmp = not tmp
        if(tmp):
            result += n*2 - (0 if n < 5 else 9)
        else:
            result += n
    return result


def checkCardNumber(cardNumber):
    return ((luhn(cardNumber) % 10) == 0)


def genCardNumber(start="", length=16):
    start = str(start)
    for n in range(len(start), length-1):
        start += str(SystemRandom().randint(0, 9))
    tmp = (luhn(start+"0") % 10)
    if tmp == 0:
        start += "0"
    else:
        start += str(10 - tmp)
    return start


if __name__ == "__main__":
    """
    to see Issuer identification number go to
    http://en.wikipedia.org/wiki/Credit_card_number#Issuer_identification_number_.28IIN.29
    """
    print(genCardNumber(51)) # master card
    print(genCardNumber(37, 15)) # american express
    print(luhn("4417123456789113"))
