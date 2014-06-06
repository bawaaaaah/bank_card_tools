#! /usr/bin/env python
# -*- coding:utf-8 -*-
from random import SystemRandom


class bankCard:

    @staticmethod
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

    @staticmethod
    def checkCardNumber(cardNumber):
        return ((bankCard.luhn(cardNumber) % 10) == 0)

    @staticmethod
    def genCardNumber(start="", length=16):
        start = str(start)
        for n in range(len(start), length-1):
            start += str(SystemRandom().randint(0, 9))
        tmp = (bankCard.luhn(start+"0") % 10)
        if tmp == 0:
            start += "0"
        else:
            start += str(10 - tmp)
        return start

    @staticmethod
    def MASTER_CARD():
        return (SystemRandom().randint(50, 55), 16)

    @staticmethod
    def AMERICAN_EXPRESS():
        return (34, 15) if SystemRandom().randint(0, 1) else (37, 15)

    @staticmethod
    def VISA():
        return (4, 13) if SystemRandom().randint(0, 1) else (4, 16)


if __name__ == "__main__":
    """
    to see Issuer identification number go to
    http://en.wikipedia.org/wiki/Credit_card_number#Issuer_identification_number_.28IIN.29
    """
    print("Master Card " + bankCard.genCardNumber(51))  # master card
    print("American Express " + bankCard.genCardNumber(37, 15))  # american express
    print("Master Card " + bankCard.genCardNumber(*bankCard.MASTER_CARD()))
    print("American Express " + bankCard.genCardNumber(*bankCard.AMERICAN_EXPRESS()))
    print("Visa " + bankCard.genCardNumber(*bankCard.VISA()))
    print(bankCard.luhn("4417123456789113"))
