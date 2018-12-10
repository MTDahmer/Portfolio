//
//  ViewController.swift
//  inclassfunctionassign
//
//  Created by StudentF18 on 11/26/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    func EvenNumber() -> String {
        var indexString:String = ""
        for index in 1...10 {
            let tester = index%2
            if tester == 0 {
                indexString += String(index) + "\n"
            }
            
        }
        return indexString
    }
    
    
    
    
    @IBOutlet weak var textbox: UITextView!
    @IBAction func EvenNumbers(_ sender: Any) {
        
        textbox.text = (EvenNumber())
        
    }


    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


    

}
