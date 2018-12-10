//
//  main.swift
//  part4
//
//  Created by StudentF18 on 11/25/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation
func getNumber( number: inout Int) {
    print("Please enter a number between 1 and 100")
    if let numberInput = readLine() {
        if let numberInt: Int = Int(numberInput) {
            if (1 <= numberInt) && (numberInt <= 100) {
                number = numberInt
            }
            else {
                print("Number out of range")
            }
        }
        else {
            print("Entered Input is not a number")
        }
    }
}
var input:Int = 0
getNumber(number: &input)
print("The number is \(input)")
