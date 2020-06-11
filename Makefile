all: project
.PHONY: project

dependencies:
	brew update
	brew list node || brew install node
	brew list carthage || brew install carthage
	brew tap tmspzz/tap || brew install tmspzz/tap/rome

project:
	./utils/xcodegen/xcodegen -s "project.yml"
	bundle install
	bundle exec pod install
	./utils/carthage/carthage.py . download

rome-upload:
	./utils/carthage/carthage.py . upload