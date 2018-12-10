//
//  ViewController.swift
//  StudentListApp
//
//  Created by StudentF18 on 11/1/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var studentList:String=""
    @IBOutlet weak var textFieldName: UITextField!
    @IBOutlet weak var textViewNameList: UITextView!
    @IBAction func buttonAdd(_ sender: Any) {
        
        if textFieldName.text==""
        {
            return
        }
        studentList += textFieldName.text!+"\n"
        textViewNameList.text=studentList
        textFieldName.text=""
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

