#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, subprocess

# Runs Carthage's consumer workflow at `path`
def run_consumer_workflow(path):
    swift_version = get_swift_version()
    subprocess.call("cd " + path + " && bundle exec rome download --platform iOS --concurrently --cache-prefix " + swift_version, shell=True)
    subprocess.call("cd " + path + " && bundle exec rome list --missing --platform iOS --cache-prefix " + swift_version + " | awk \'{print $1}\' | xargs carthage update --platform iOS --cache-builds", shell=True)


# Runs Carthage's producer workflow at `path`
def run_producer_workflow(path):
    swift_version = get_swift_version()
    subprocess.call("cd " + path + " && bundle exec rome list --missing --platform iOS --cache-prefix " + swift_version + " | awk \'{print $1}\' | xargs -I {} rome upload \"{}\" --platform iOS --concurrently --cache-prefix " + swift_version, shell=True)

# Gets swift version
def get_swift_version():
    command = 'xcrun swift --version | head -1 | sed "s/.*((.*)).*/1/" | tr -d "()" | tr " " "-"'
    process = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.strip()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./carthage.py {path} {command}")
        exit(1)
        
    path = sys.argv[1]
    command = sys.argv[2]

    if command == "download":
        run_consumer_workflow(path)
    elif command == "upload":
        run_producer_workflow(path)
    else:
        print("Usage: ./carthage.py {path} {command}")
