function checkCardNumber(cardNumber){
    // example of use checkCardNumber("0000000000000000");
    cardNumber.toString();
    var tmp = (cardNumber.length%2 == 1), result = 0;
    for (var n in cardNumber){
        if(n = parseInt(cardNumber[n]), (tmp = !tmp))
            result += n*2 - ((n<5)?0:9);
        else
            result += n;
    }
    return((result%10) == 0) 
}
