### Instruction
#### Installing Certificates
You can install certificates system wide. For this demo we don't need to this since our python test script
`tests.py` uses `requests` dependencies and using this we can pass certificate file explicitly.
In order to install the certificate on your machine:
1. Run mitmproxy `mitmproxy`
2. Change your proxy settings on your browser to http://127.0.0.1:8080
3. Open this page https://mitm.it If your browser proxy config is working you should see a page where you can download certificate
4. Install the certificate using Mac keychain and trust this certificate

#### Running tests:
* Install mitmproxy: `brew install mitmproxy`
* Install certificate
  1- When you run `mitmproxy` for the first time it creates cert on `${HOME}/.mitmproxy`
* Cd to project directory
* Install virtualenv: `python -m venv venv`
* Activate virtualenv: `source ./venv/bin/activate`
* Install dependencies: `pip install -r requirement.txt`
* Run mitmdump: `mitmdump -s ./proxyscript.py`
* Run pytest: `pytest -q tests.py`


**Note:** The connection between client to mitmproxy is unsecured. When you set up proxy use http**s**_proxy as http://127.0.0.1:8080 

#### Using Docker
You can run the demo using docker-compose. Currently, you still need to install mitmproxy in order to generate certificates
on you local machine. You can also bring your own certificate which in this case there is no need to install mitmproxy locally.

0. make sure mitmproxy certificates exists. By default they're under this path: `${HOME}/.mitmproxy/`
1. cd to project's root directory
2. run `docker-compose build`
3. run `docker-compose up`
You should see this log line:
```log
my-service_1  | 2 passed in 0.52s
```
