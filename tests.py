import requests
from assertpy import assert_that

base_url = "https://internal-dev.api.service.nhs.uk/hello-world"

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "https://127.0.0.1:8080"
}


def test_no_proxy():
    # Given
    expected_status_code = 200

    # When
    response = requests.get(
        # proxies=proxies,
        url=base_url + "/hello/world",
        verify=False,
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
        # proxies=proxies,
        verify=False,
        url=base_url + "/hello/world",
        headers={
            'TestScenario': 'GetHelloWorld408',
            'accept': 'application/json'
        }
    )

    # Then
    assert_that(response.status_code).is_equal_to(expected_status_code)
