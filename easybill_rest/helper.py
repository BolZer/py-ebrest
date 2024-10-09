from urllib.parse import urlencode


class Helper:
    @staticmethod
    def create_request_url_from_params(
            endpoint: str, params=None) -> str:
        """create_request_url_from_params is a helper function which is used by the
        resources to generate the request_url"""

        if params is None:
            params = {}

        if len(params) == 0:
            return "/rest/v1" + endpoint

        return "/rest/v1" + endpoint + "?" + urlencode(params)
