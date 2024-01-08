.PHONY: generate

deps:
	sudo apt install pandoc jq
generate:
	python3 generate.py
