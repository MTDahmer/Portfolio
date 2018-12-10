//
//  main.swift
//  part3
//
//  Created by StudentF18 on 11/25/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation

func inputDivide (numbers:Int...) -> Double {
    var returnValue:Double = 0.0
    if (numbers[1] == 0) {
        return -1
    }
    else {
        returnValue = numbers[0] / numbers [1]
        return returnValue
    }
}
print("Enter two numbers and i will divide the first number by the second number:")





