//
//  main.swift
//  arrays
//
//  Created by StudentF18 on 12/3/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation
func keyboardInput(_ name : inout String ,_ number : inout String) {
    print("Please enter your name");
    name = readLine()!;
    print("Please enter your phone number:");
    number = readLine()!;
    
}
var contacts = [String : String]();
contacts["Ron Weasley"] = "(713)775-8765";
contacts["Harry Poter"] = "(212)444-2323";
contacts["Lord Voldemort"] = "(666)666-0000";
contacts["Ron Weasley"] =  "(832)775-8765";
var name:String = "";
var number:String = "";
keyboardInput(&name , &number);
contacts[name] = number;
contacts["Harry Poter"] = nil;
keyboardInput(&name , &number);
contacts[name] = number;
let areaCodeFind = readLine()!
var phoneNumber = contacts[areaCodeFind]
let areaCodeEnder = phoneNumber!.firstIndex(of:")")  ?? phoneNumber!.endIndex
var areaCode = phoneNumber[...areaCodeEnder]
if (areaCode == "666") {
    print("\(areaCodeFind) is in area code \(areaCode)")
    
    
}





