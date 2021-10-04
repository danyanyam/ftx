from base import BaseApiClass
import datetime as dt
from typing import List


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
        pass
        return self.post('/sapi/v1/account/disableFastWithdrawSwitch', time_req=time_req, sign=sign)

    def enable_fast_withdraw_switch(self, recvWindow: int = None, time_req: bool = True, sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#disable-fast-withdraw-switch-user_data"""
        pass
        return self.post('/sapi/v1/account/disableFastWithdrawSwitch', time_req=time_req, sign=sign)

    def withdraw(self,
                 coin: str = None,
                 withdrawOrderId: str = None,
                 network: str = None,
                 address: str = None,
                 addressTag: str = None,
                 amount: float = None,
                 transactionFeeFlag: bool = None,
                 name: str = None,
                 recvWindow: int = None,
                 time_req: bool = True,
                 sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#withdraw-user_data"""
        pass
        return self.post('/sapi/v1/capital/withdraw/apply',
                         coin=coin,
                         withdrawOrderId=withdrawOrderId,
                         network=network,
                         address=address,
                         addressTag=addressTag,
                         amount=amount,
                         transactionFeeFlag=transactionFeeFlag,
                         name=name,
                         recvWindow=recvWindow,
                         time_reqtime_req=time_req,
                         sign=sign)

    def deposit_history(self,
                        coin: str = None,
                        status: int = None,
                        start_time: dt.datetime = None,
                        end_time: dt.datetime = None,
                        offset: int = None,
                        limit: int = None,
                        recvWindow: int = None,
                        time_req: bool = True,
                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#deposit-history-supporting-network-user_data"""
        return self.get('/sapi/v1/capital/deposit/hisrec',
                        coin=coin,
                        status=status,
                        start_time=start_time,
                        end_time=end_time,
                        offset=offset,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def withdraw_history(self,
                         coin: str = None,
                         withdrawOrderId: str = None,
                         status: int = None,
                         offset: int = None,
                         limit: int = None,
                         start_time: dt.datetime = None,
                         end_time: dt.datetime = None,
                         recvWindow: int = None,
                         time_req: bool = True,
                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#withdraw-history-supporting-network-user_data"""
        return self.get('/sapi/v1/capital/withdraw/history',
                        coin=coin,
                        withdrawOrderId=withdrawOrderId,
                        status=status,
                        offset=offset,
                        limit=limit,
                        start_time=start_time,
                        end_time=end_time,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def deposit_address(self,
                        coin: str = 'BTC',
                        network: str = None,
                        recvWindow: int = None,
                        time_req: bool = True,
                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data"""
        return self.get('/sapi/v1/capital/deposit/address',
                        coin=coin, network=network, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def account_status(self,
                       recvWindow: int = None,
                       time_req: bool = True,
                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#account-status-user_data"""
        return self.get('/sapi/v1/account/status',
                        recvWindow=recvWindow, time_req=time_req, sign=sign)

    def account_api_trading_status(self,
                                   recvWindow: int = None,
                                   time_req: bool = True,
                                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#account-api-trading-status-user_data"""
        return self.get('/sapi/v1/account/apiTradingStatus',
                        recvWindow=recvWindow, time_req=time_req, sign=sign)

    def dust_log(self,
                 start_time: dt.datetime = None,
                 end_time: dt.datetime = None,
                 recvWindow: int = None,
                 time_req: bool = True,
                 sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#dustlog-user_data"""
        return self.get('/sapi/v1/asset/dribblet',
                        start_time=start_time, end_time=end_time, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def dust_transfer(self,
                      asset: List[str] = ['BTC', 'USDT'],
                      recvWindow: int = None,
                      time_req: bool = True,
                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#dust-transfer-user_data"""
        pass
    # TO DO: Computer asset parament
        # asset = {'asset': asset}
        return self.post('/sapi/v1/asset/dust', asset=asset, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def asset_dividend_record(self,
                              asset: str = None,
                              start_time: dt.datetime = None,
                              end_time: dt.datetime = None,
                              limit: int = None,
                              recvWindow: int = None,
                              time_req: bool = True,
                              sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#asset-dividend-record-user_data"""
        return self.get('/sapi/v1/asset/assetDividend', asset=asset, start_time=start_time, end_time=end_time,
                        limit=limit, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def asset_detail(self,
                     asset: str = None,
                     recvWindow: int = None,
                     time_req: bool = True,
                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#asset-detail-user_data"""
        return self.get('/sapi/v1/asset/assetDetail', asset=asset, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def trade_fee(self,
                  symbol: str = None,
                  recvWindow: int = None,
                  time_req: bool = True,
                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#trade-fee-user_data"""
        return self.get('/sapi/v1/asset/tradeFee', symbol=symbol, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def user_universal_transfer(self,
                                type: str = None,
                                asset: str = 'SPOT',
                                amount: float = 0.0,
                                fromSymbol: str = None,
                                toSymbol: str = None,
                                recvWindow: int = None,
                                time_req: bool = True,
                                sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#user-universal-transfer-user_data"""

        assert type in ['MAIN_MINING', 'C2C_MAIN', 'C2C_UMFUTURE', 'C2C_MINING', 'C2C_MARGIN',
                        'UMFUTURE_MAIN', 'UMFUTURE_C2C', 'UMFUTURE_MARGIN', 'CMFUTURE_MAIN',
                        'CMFUTURE_MARGIN', 'MARGIN_MAIN', 'MARGIN_UMFUTURE', 'MARGIN_CMFUTURE',
                        'MARGIN_MINING', 'MARGIN_C2C', 'MINING_MAIN', 'MINING_UMFUTURE', 'MINING_C2C',
                        'MINING_MARGIN', 'MAIN_PAY', 'PAY_MAIN', 'ISOLATEDMARGIN_MARGIN', 'MARGIN_ISOLATEDMARGIN',
                        'ISOLATEDMARGIN_ISOLATEDMARGIN'], f"Type {type} is not in possible values"

        # if type in ['ISOLATEDMARGIN_MARGIN', 'ISOLATEDMARGIN_ISOLATEDMARGIN'] and (fromSymbol is None or toSymbol is None):
        #     print("Error!")
        # else:
        #     pass
        return self.post('/sapi/v1/asset/transfer', type=type, asset=asset, amount=amount,
                         fromSymbol=fromSymbol, toSymbol=toSymbol, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def user_universal_transfer_history(self,
                                        type: str = None,
                                        start_time: dt.datetime = None,
                                        end_time: dt.datetime = None,
                                        current: int = None,
                                        size: int = None,
                                        fromSymbol: str = None,
                                        toSymbol: str = None,
                                        recvWindow: int = None,
                                        time_req: bool = True,
                                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-user-universal-transfer-history-user_data"""
        # TODO: Fix Error
        # TypeError: Invalid variable type: value should be str, int or float, got True of type <class 'bool'>
        # IDK why - something happens in asyncio
        assert type in ['MAIN_MINING', 'C2C_MAIN', 'C2C_UMFUTURE', 'C2C_MINING', 'C2C_MARGIN',
                        'UMFUTURE_MAIN', 'UMFUTURE_C2C', 'UMFUTURE_MARGIN', 'CMFUTURE_MAIN',
                        'CMFUTURE_MARGIN', 'MARGIN_MAIN', 'MARGIN_UMFUTURE', 'MARGIN_CMFUTURE',
                        'MARGIN_MINING', 'MARGIN_C2C', 'MINING_MAIN', 'MINING_UMFUTURE', 'MINING_C2C',
                        'MINING_MARGIN', 'MAIN_PAY', 'PAY_MAIN', 'ISOLATEDMARGIN_MARGIN', 'MARGIN_ISOLATEDMARGIN',
                        'ISOLATEDMARGIN_ISOLATEDMARGIN'], f"Type {type} is not in possible values"
        return self.get('/sapi/v1/asset/transfer', type=type, start_time=start_time, end_time=end_time,
                        current=current, size=sign, fromSymbol=fromSymbol, toSymbol=toSymbol, recvWindow=recvWindow, sign=sign)

    def funding_wallet(self,
                       asset: str = None,
                       needBtcValuation: str = None,  # TODO: ['True', 'False' without str instance]
                       recvWindow: int = None,
                       time_req: bool = True,
                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#funding-wallet-user_data"""
        assert needBtcValuation in ['True', 'False'], f"Parametr needBtcValuation ({needBtcValuation}) is not in ['True', 'False']"
        return self.post('/sapi/v1/asset/get-funding-asset', asset=asset, needBtcValuation=needBtcValuation, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def api_key_permission(self, recvWindow: int = None, time_req: bool = True, sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-api-key-permission-user_data"""
        return self.get('/sapi/v1/account/apiRestrictions', recvWindow=recvWindow, time_req=time_req, sign=sign)
