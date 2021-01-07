run:
	mitmdump -s ./proxyscript.py

docker-build:
	docker build -t mitmproxy-demo .

tests:
	pytest -q tests.py
