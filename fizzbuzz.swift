//
//  fizzbuzz.swift
//  
//
//  Created by StudentF18 on 9/10/18.
//

import Foundation
var mN = 0
while mN<100 {
    let Fizz = mN%3
    let Buzz = mN%5
    
    if Fizz == 0 {
        print("Fizz")
        mN = mN + 1
    }
    else if Buzz == 0 {
        print("Buzz")
        mN = mN + 1
    }
        //if ((Buzz == 0),(Fizz == 0)) {
        //print("FizzBuzz")
        //}
    else {
        print(mN)
        mN = mN + 1
    }
    
}
