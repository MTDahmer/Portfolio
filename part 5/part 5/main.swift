//
//  main.swift
//  part 5
//
//  Created by StudentF18 on 11/25/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import Foundation
func calculateRetail (percent: Double, wholesale: Double) -> Double {
    let percentOperator:Double = percent/100
    let outputPrice: Double = wholesale * percentOperator
    return outputPrice
}
print("What is the price of the item?")
if let price = readLine() {
    if let priceDouble: Double = Double(price){
        print("What is the discount applied?(Please write in whole integers)")
        if let discount = readLine() {
            if let discountDouble:Double = Double(discount) {
               
                print("The final price is \( calculateRetail(percent: priceDouble, wholesale: discountDouble))")
            }
        
        }
    }
}
