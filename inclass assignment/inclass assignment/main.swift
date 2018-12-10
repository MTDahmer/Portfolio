//
//  main.swift
//  inclass assignment
//
//  Created by StudentF18 on 11/12/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

var number = 0
var intTest = 0
var tester : Int = 1
var count : Int = 0
var repeatFlag : Bool = true
while (repeatFlag) {
    //var numberFlag : Bool = true
    //while (numberFlag) {
    print("Please enter a number: ")
    if let number = readLine(){
        if let intTest = Int(number){
            //print("Entered input is \(int) of the type:\(type(of: int))")
            //numberFlag = false
            break
        }
        else{
            print("invalid entry")
            
        }
        
    }
    //}
    
    
    
    
    while (count <= 100) {
        
        let multiple = tester % intTest
        if (multiple == 0) {
            print(tester)
            count += 1
            tester += 1
        }
        else {
            tester += 1
        }
    }
    print("Would you like to enter another number (Y- Yes or N - No) :")
    let repeatChoice = readLine()
    if (repeatChoice == "N") {
        repeatFlag = false
        
    }
}
print("Goodbye!")


