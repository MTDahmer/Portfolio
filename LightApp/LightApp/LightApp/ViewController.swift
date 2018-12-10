//
//  ViewController.swift
//  LightApp
//
//  Created by StudentF18 on 10/1/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var lightOn = true
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        print("Button Pressed")
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func buttonLight(_ sender: Any) {
        print("Button Pressed")
        lightOn = !lightOn
        UpdateUI()
    }
    func UpdateUI()
    {
        if lightOn
        {view.backgroundColor = UIColor.white
        }
        else {
            view.backgroundColor = UIColor.black
        }
    }
    
}

