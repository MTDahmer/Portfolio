//: Playground - noun: a place where people can play

import UIKit

import Foundation
var mN = 1
while mN<100 {
    let Fizz = mN%3
    let Buzz = mN%5
    if ((Buzz == 0) && (Fizz == 0)) {
        print("FizzBuzz")
        mN += 1
    }
    else if Fizz == 0 {
        print("Fizz")
        mN += 1
    }
    else if Buzz == 0 {
        print("Buzz")
        mN += 1
    }
    else {
        print(mN)
        mN += 1
    }
}
print("But can this be smaller?")

