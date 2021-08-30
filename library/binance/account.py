from base import BaseApiClass
import datetime as dt


class Wallet(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#wallet-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def system_status(self):
        """https://binance-docs.github.io/apidocs/spot/en/#system-status-system"""
        return self.get('/sapi/v1/system/status')

    def coins_infromation(self, recvWindow: int = None, time_req: bool = True, sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data"""
        return self.get('/sapi/v1/capital/config/getall', sign=sign, time_req=time_req, recvWindow=recvWindow)

    def account_snapshot(self,
                         time_req: bool = True,
                         sign=True,
                         type: str = "SPOT",
                         limit: int = None, start_time: dt.datetime = None,
                         end_time: dt.datetime = None):
        """https://binance-docs.github.io/apidocs/spot/en/#daily-account-snapshot-user_data"""
        return self.get('/sapi/v1/accountSnapshot', time_req=time_req, sign=sign, type=type, limit=limit, startTime=start_time, endTime=end_time)

    def disable_fast_withdraw_switch(self, recvWindow: int = None, time_req: bool = True, sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#disable-fast-withdraw-switch-user_data"""
        return self.post('/sapi/v1/account/disableFastWithdrawSwitch', time_req=time_req, sign=sign)

    def enable_fast_withdraw_switch(self, recvWindow: int = None, time_req: bool = True, sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#disable-fast-withdraw-switch-user_data"""
        pass
        return self.post('/sapi/v1/account/disableFastWithdrawSwitch', time_req=time_req, sign=sign)
