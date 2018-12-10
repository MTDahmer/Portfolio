//: Playground - noun: a place where people can play

import UIKit
var coneDiameter:Double = 2.0
var coneRadius:Double = coneDiameter/2
var coneDoubledRadius:Double = coneRadius * coneRadius
var coneHeight:Double = 6.5
var coneSlant:Double = sqrt((coneHeight * coneHeight) + coneDoubledRadius)
let valueOfPi:Double = 3.1415926359
var coneVolume:Double = (1/3) * valueOfPi * coneDoubledRadius * coneHeight
var coneSurfaceArea:Double = (valueOfPi * coneRadius * coneSlant) + (valueOfPi * coneDoubledRadius)
print("The volume of the cone is \(coneVolume)")
print("The surface area of the cone is \(coneSurfaceArea)")
