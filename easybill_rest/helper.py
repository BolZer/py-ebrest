from urllib.parse import urlencode


class Helper:
    @staticmethod
    def create_request_url_from_params(
            endpoint: str, params: dict = None) -> str:
        """create_request_url_from_params is a helper function which is used by the
        resources to generate the request_url"""

        if params is None:
            return "/rest/v1" + endpoint

        return "/rest/v1" + endpoint + "?" + urlencode(params)
