import requests
from assertpy import assert_that
import os

base_url = "https://internal-dev.api.service.nhs.uk/hello-world"

home_dir = os.environ.get("HOME")
cert_path = os.environ.get("CERT_PATH")
cert_path = cert_path or (home_dir + "/.mitmproxy/mitmproxy-ca-cert.pem")

mitmproxy_url = os.environ.get("MITMPROXY_URL") or "http://127.0.0.1:8080"
proxies = {
    "http": mitmproxy_url,
    "https": mitmproxy_url
}



def test_no_proxy():
    # Given
    expected_status_code = 200

    # When
    response = requests.get(
        proxies=proxies,
        url=base_url + "/hello/world",
        verify=cert_path,
        headers={
            'accept': 'application/json'
        }
    )

    # Then
    assert_that(response.status_code).is_equal_to(expected_status_code)


def test_proxy_returns_408():
    # Given
    expected_status_code = 408

    # When
    response = requests.get(
        proxies=proxies,
        url=base_url + "/hello/world",
        verify=cert_path,
        headers={
            'TestScenario': 'GetHelloWorld408',
            'accept': 'application/json'
        }
    )

    # Then
    assert_that(response.status_code).is_equal_to(expected_status_code)
