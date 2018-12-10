//
//  main.swift
//  Mitchell_Dahmer_Loops
//
//  Created by StudentF18 on 11/11/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation
var input : String = ""
var number : Int = 0
var count : Int = 0
var repeatFlag : Bool = true
var finished : String = ""
repeat {
    print("Please enter a number")
    if let input = readLine() {
        if let inputInt = Int(input) {
            number = inputInt
        }
        else {
            print("invalid entry")
        }
    var modified : Int = number
    while (count <= 100) {
            
            let multiple = modified % number
            if (multiple == 0) {
                if (count == 0) {
                    finished = finished + " " + "\(modified)"
                    count += 1
                    modified += 1
                }
                else if (count % 10 == 0) {
                    finished = finished + " " + "\(modified)" + "\n"
                    count += 1
                    modified += 1
                }
                else {
                    finished = finished + " " + "\(modified)"
                    count += 1
                    modified += 1
                }
                
                
            }
            else {
                modified += 1
            }
    }
    print(finished)
    print("Would you like to use another number: Y for Yes  |  N for No")
    if let rpeat = readLine() {
        if (rpeat == "N" || rpeat == "n") {
            repeatFlag = false
        }
        else {
            print("Repreating Program")
            count = 0
            modified = 0
            
            
        }
    }
}
} while (repeatFlag)
print("Goodbye")
