//
//  ViewController.swift
//  projectII
//
//  Created by StudentF18 on 12/7/18.
//  Copyright © 2018 HCCS. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    let meowSound = SimpleSound(named:"meow")
    let dogSound = SimpleSound(named:"woof")
    let mooSound = SimpleSound(named:"moo")
    let cowboySound = SimpleSound(named:"ahhhhhhh")
    @IBOutlet weak var labelAnimalSound: UILabel!
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func buttonDogTapped(_ sender: UIButton) {
        labelAnimalSound.text = "Woof!"
        dogSound.play()
        
    }
    
    @IBAction func buttonCowTapped(_ sender: UIButton) {
        labelAnimalSound.text = "Moo!"
        mooSound.play()
        
    }
    
    @IBAction func buttonYeehawTapped(_ sender: UIButton) {
        labelAnimalSound.text = "Yeehaw!"
        cowboySound.play()
    }
    
    @IBAction func buttonCatTapped(_ sender: UIButton) {
        labelAnimalSound.text = "Meow!"
        meowSound.play()
    }
}

