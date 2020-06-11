//
//  TestViewController.swift
//  TestProject
//
//  Created by Marcen, Rafael on 11/06/2020.
//  Copyright © 2020 TestProject. All rights reserved.
//

import Foundation
import UIKit
import Lottie

class TestViewController: UIViewController {
    
    private let label: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "This is a test"
        return label
    }()
    
    override func loadView() {
        super.loadView()
        
        view.addSubview(label)
        NSLayoutConstraint.activate([
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }
}
