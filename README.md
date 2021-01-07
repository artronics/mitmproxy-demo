###Instruction
* Install mitmproxy: `brew install mitmproxy`
* Install certificate:
  1. Run mitmproxy `mitmproxy`
  2. Change your proxy settings on your browser to http://127.0.0.1:8080 and https://127.0.0.1:8080
  3. Open this page https://mitm.it If your browser proxy config is working you should see a page where you can download certificate
  4. Install certificate using Mac keychain and trust this certificate
* Cd to project directory
* Install virtualenv: `python -m venv venv`
* Activate virtualenv: `source ./venv/bin/activate`
* Install dependencies: `pip install -r requirement.txt`
* Run mitmdump: `mitmdump -s ./proxyscript.py`
* Run pytest: `pytest -q tests.py`

Note: Don't use virtualenv local pytest since the system certificate won't work. 
Note: Docker is WIP, and it doesn't work yet.
