//
//  main.swift
//  Lab 4
//  Mitchell Dahmer
//  Created by StudentF18 on 10/1/18.
//  Copyright © 2018 MitchellD. All rights reserved.
//  A program to calculate the amount of fees owed based on the number of checks cashed

import Foundation

var numberOfChecks:Double = 40.00
var checkFee:Double = 0.00
if (numberOfChecks < 20) {
    checkFee = 0.10
}
else if ((numberOfChecks >= 20) && (numberOfChecks <= 39)) {
    checkFee = 0.08
}
else if ((numberOfChecks >= 40) && (numberOfChecks <= 59)) {
    checkFee = 0.06
}
else  {
    checkFee = 0.04
}
var totalFeeCost:Double = (numberOfChecks * checkFee) + 10.00

print("Bank's fee for this month = $\(totalFeeCost)")

