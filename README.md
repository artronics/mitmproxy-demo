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

#### Running Solution Assurance (SA) Tests
NHSD API producer team will provide a proxy script similar to `remote_control_proxyscript.py` file. You can use this file
to configure and **control** proxy. We've chosen this method so, we can decouple the logic of intercepting the http requests
from proxy configuration. In order to perform a given SA scenario you need to send a GET request to `http://mitm.it/cmd/scenario.<your-scenario-id>`.
This requests will be intercepted by mitmproxy and as a result it will put the mitmproxy into `<your-scenario-id>` state. 
Using this file mitmproxy by default is in a pass-through state, i.e. it doesn't intercept your calls. After sending that GET 
request, the next request to the proxy will be intercepted, and you'll get a http response as per SA requirement.
As an example say you want to perform test scenario id: `SA-042`:
* Send a `GET http://mitm.it/cmd/scenario.SA-042` request
* Perform your test
  * You should receive a response as per SA documentation

**Note:** You don't need to change the state of the proxy to pass-through after executing a test. Upon receiving a requst
that matches, this script will put the state of the proxy to pass-through.

**Note**: The `http://mitm.it/cmd` has chosen arbitrary. If you study the source code you'll notice the request never leaves 
the proxy. We only use this URL to intercept a request and change the state of the proxy.

**Note**: When you send a GET requests make sure you put the correct scenario ID. ID is case-sensitive. If you misspell it,
then there won't be any matching scenario and, proxy will act as pass-through.

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
