platform :ios, '12.0'

source 'https://github.com/CocoaPods/Specs.git'
install! 'cocoapods', :disable_input_output_paths => true

inhibit_all_warnings!

def core_framework_pods
  pod 'SwiftLint'
end

target 'TestProject' do
  use_frameworks!

  core_framework_pods
end