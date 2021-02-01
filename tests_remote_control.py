import os

import requests
from assertpy import assert_that

base_url = "https://internal-dev.api.service.nhs.uk/hello-world"

home_dir = os.environ.get("HOME")
cert_path = os.environ.get("CERT_PATH")
cert_path = cert_path or (home_dir + "/.mitmproxy/mitmproxy-ca-cert.pem")

mitmproxy_url = os.environ.get("MITMPROXY_URL") or "http://127.0.0.1:8080"
proxies = {
    "http": mitmproxy_url,
    "https": mitmproxy_url
}


def switch_scenario(scenario: str):
    cmd_url = f'http://mitm.it/cmd/scenario.{scenario}'
    requests.get(
        proxies=proxies,
        url=cmd_url,
        verify=cert_path,
    )


def test_ra_api_cs_024():
    # Given
    switch_scenario("RA-API-CS-024")
    expected_status_code = 524

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


def test_ra_api_cs_025():
    # Given
    switch_scenario("RA-API-CS-025")
    expected_status_code = 525

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


def test_200():
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

