from abc import abstractmethod

from mitmproxy import http


class ScenarioManager:
    current_scenario = ''

    base_cmd_url = "http://mitm.it/cmd"
    cmd_prefix = "scenario."

    def get_scenario_from_url(self, flow: http.HTTPFlow) -> str:
        if self.is_cmd_url(flow):
            url = flow.request.pretty_url
            seg = url.split('/')

            return seg[-1][len(self.cmd_prefix):]
        else:
            return ''

    def is_cmd_url(self, flow: http.HTTPFlow) -> bool:
        return flow.request.pretty_url.startswith(self.base_cmd_url)


scenario_manager = ScenarioManager()


class ScenarioMangerAddon:
    def request(self, flow: http.HTTPFlow):
        scenario = scenario_manager.get_scenario_from_url(flow)
        if scenario != '':
            scenario_manager.current_scenario = scenario
            print(f'[+] Switch to Scenario: ${scenario}')

            flow.response = http.HTTPResponse.make(
                status_code=200,
                content=f'scenario ${scenario} has been selected'
            )


class TestScenario:
    def __init__(self, risk_id: str, risk_group: str, description: str, cause: str):
        self.risk_id = risk_id
        self.risk_group = risk_group
        self.description = description
        self.cause = cause
        self.scenario_manager = scenario_manager

    def request(self, flow):
        if (scenario_manager.current_scenario == self.risk_id) and (not scenario_manager.is_cmd_url(flow)):
            print(f'[+] Scenario ID: {self.risk_id}')
            print(f'     Risk Group: {self.risk_group}')
            print(f'    Description: {self.description}')
            print(f'          Cause: {self.cause}')
            self.intercept(flow)
            scenario_manager.current_scenario = ''

    @abstractmethod
    def intercept(self, flow):
        pass


class RaApiCs024(TestScenario):
    def __init__(self):
        super().__init__(
            risk_id="RA-API-CS-024",
            risk_group="Create a new Reasonable Adjustment Flag",
            description="Connecting System fails to notify user a new Reasonable Adjustment Flag has NOT been successfully created.",
            cause="Connecting system fails to correctly process response from RA API (System level)")

    def intercept(self, flow):
        flow.response = http.HTTPResponse.make(
            status_code=524,
        )


class RaApiCs025(TestScenario):
    def __init__(self):
        super().__init__(
            risk_id="RA-API-CS-025",
            risk_group="Create a new Reasonable Adjustment Flag",
            description="Connecting System fails to notify user a new Reasonable Adjustment Flag has NOT been successfully created.",
            cause="Connecting system fails to correctly present the data returned from RA API (Presentation layer)")

    def intercept(self, flow):
        flow.response = http.HTTPResponse.make(
            status_code=525,
        )


test_scenarios = [
    RaApiCs024(),
    RaApiCs025(),
]


class MitmproxyTestHelper:
    def request(self, flow):
        for scenario in test_scenarios:
            scenario.request(flow)


addons = [
    ScenarioMangerAddon(),
    MitmproxyTestHelper()
]
