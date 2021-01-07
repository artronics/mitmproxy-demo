import json

from mitmproxy import http


class GetHelloWorld408:
    def request(self, flow: http.HTTPFlow):
        # if flow.request.query.get('patient') == '123':
        if flow.request.headers.get('TestScenario') == 'GetHelloWorld408':
            print("[+] Test GetHelloWorld408 scenario")
            # flow.kill() # This will kill the TCP socket. it's not suitable for timeout scenario
            flow.response = http.HTTPResponse.make(
                status_code=408,
                headers={"Connection": "closed"}
            )


class PostHelloWorld409:
    def request(self, flow: http.HTTPFlow):
        if flow.request.headers.get('TestScenario') == 'PostHelloWorld409':
            print("[+] Test PostHelloWorld409 scenario")
            flow.response = http.HTTPResponse.make(
                status_code=409,
                content=json.dumps({"error": "DUPLICATED ENTITY"}),
            )


addons = [
    GetHelloWorld408(),
    PostHelloWorld409(),
]
