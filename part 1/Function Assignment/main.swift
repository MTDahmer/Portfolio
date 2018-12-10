//
//  main.swift
//  Function Assignment
//
//  Created by StudentF18 on 11/25/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation

func parse(digit:String) -> Int {
    switch (digit) {
    case "0" , "1" , "2" , "3", "4", "5", "6", "7", "8", "9":
        let digit1: Int = Int(digit)!
        return digit1
    default:
        return -1
}
}
var input:String = ""
input = readLine()!
print(parse(digit:input))

