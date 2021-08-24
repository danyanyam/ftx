from typing import Dict
from library.utils import _get, _post


class ApiObject:
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.subaccount_name = subaccount_name

    async def get(self, endpoint: str, authentication_requires: bool = True):
        """ Basic get request """
        return await _get(endpoint, is_auth=authentication_requires, subaccount_name=self.subaccount_name, api_key=self.api_key, secret_key=self.secret_key)

    async def post(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True):
        """ Basic post request """
        return await _post(endpoint, data=data, is_auth=authentication_required,  subaccount_name=self.subaccount_name, api_key=self.api_key, secret_key=self.secret_key)