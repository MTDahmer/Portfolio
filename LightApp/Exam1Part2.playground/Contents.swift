//Problem 1 - Calculate the reward points
var memberType:Character = "S"
var monthlyPurchase:Double = 500
var rewardAmount = 0.0
if (memberType == "S") {
    if (monthlyPurchase < 75) {
        rewardAmount = 0.05
    }
    else if((monthlyPurchase >= 75) && (monthlyPurchase <= 150)) {
        rewardAmount = 0.075
    }
    else{
        rewardAmount = 0.1
    }
}
else if (memberType == "P") {
    if (monthlyPurchase < 200) {
        rewardAmount = 0.04
    }
    else {
        rewardAmount = 0.15
    }
}
print(rewardAmount)
//Problem Two - Currenct Conversion
let cad = 1.30
let euro = 0.89
let yen = 119.91
let peso = 16.66
let pond = 0.66
var usDollars:Double = 100
var convertedAmount:Double = 0
var currencyType:Int = 4
switch(currencyType) {
case 1:
    convertedAmount = cad * usDollars
    break
case 2:
    convertedAmount = euro * usDollars
    break
case 3:
    convertedAmount = yen * usDollars
    break
case 4:
    convertedAmount = peso * usDollars
    break
case 5:
    convertedAmount = pond * usDollars
    break
default:
    print("Invalid Currency")
}
print("Amount in US Dollars = \(usDollars). Converted amount = \(convertedAmount)")
