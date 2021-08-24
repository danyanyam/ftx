from typing import Any, Dict
from library.utils import _get, _post


class Wallet:
    """https://docs.ftx.com/#account"""

    def __init__(self, api: str, secret: str):
        self.api_key = api
        self.secret_key = secret

    async def get(self, endpoint: str, authentication_required: bool = True) -> Dict[str, Any]:
        return await _get(endpoint, is_auth=authentication_required, api_key=self.api_key, secret_key=self.secret_key)

    async def post(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True) -> Dict[str, Any]:
        return await _post(endpoint, data=data, is_auth=authentication_required, api_key=self.api_key, secret_key=self.secret_key)

    async def get_coins(self) -> Dict[str, Any]:
        return await self.get('/wallet/coins')

    async def get_balances(self) -> Dict[str, Any]:
        return await self.get('/wallet/balances')

    async def get_balances_of_all_accounts(self) -> Dict[str, Any]:
        """
        The response will contain an object whose keys are the subaccount names.
        The main account will appear under the key main.
        """
        return await self.get('/wallet/all_balances')

    async def get_deposit_address(self, coin: str, method: str) -> Dict[str, Any]:
        """
        For ERC20 tokens    : method=erc20
        For TRC20 tokens    : method=trx
        For SPL tokens      : method=sol
        For Omni tokens     : method=omni
        For BEP2 tokens     : method=bep2
        """
        return await self.get(f'/wallet/deposit_address/{coin}?method={method}')

    async def get_deposit_history(self):
        return await self.get('/wallet/deposits')

    async def get_withdrawal_history(self):
        return await self.get('/wallet/withdrawals')

    async def request_withdrawal(self, coin: str, size: float, address: str, tag: str = None, method: str = None, password: str = None, code: str = None) -> Dict[str, Any]:
        """
        Args:
            coin (str)                : [USDTBEAR] coin to withdraw
            size (float)              : [20.2] amount to withdraw
            address (str)             : [0x83a12795...] address to send to
            tag (str, optional)       : string text
            method (str, optional)    : blockchain to use for withdrawal. Defaults to None.
            password (str, optional)  : withdrawal password if it is required for your account.
            Defaults to None.
            code (str, optional)      : 2fa code if it is required for your account. Defaults to None.

        Returns:
            Dict[str, Any]: result
        """
        return await self.post('/wallet/withdrawals', data={coin: coin, size: size, address: address, tag: tag, method: method, password: password, code: code})
