//
//  main.swift
//  part2
//
//  Created by StudentF18 on 11/25/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation

func Odd_r_Even(number:Int , numberDefault:Int = 32) {
    let tester = number%2
    if (tester == 0) {
        print("The number \(number) is Even")
    }
    else {
        print("The number \(number) is Odd")
    }
}

if let input = readLine() {
    if let inputInt = Int(input) {
        if (inputInt >= 0) {
            Odd_r_Even(number: inputInt)
        }
    }
    else if let inputFlt = Float(input) {
        print("The number \(inputFlt) is odd")
    }
   
    else {
        print("invalid entry")
}
}
