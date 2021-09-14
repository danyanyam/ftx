from base import BaseApiClass
import datetime as dt


class Mining(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#mining-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def acquiring_algorithm(self,
                            recvWindow: int = None,
                            time_req: bool = True,
                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#acquiring-algorithm-user_data"""
        return self.get('/sapi/v1/mining/pub/algoList',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def acquiring_coinName(self,
                           recvWindow: int = None,
                           time_req: bool = True,
                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#acquiring-coinname-user_data"""
        return self.get('/sapi/v1/mining/pub/coinList',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def request_for_detail_miner_list(self,
                                      algo: str = None,
                                      userName: str = None,
                                      workerName: str = None,
                                      recvWindow: int = None,
                                      time_req: bool = True,
                                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#request-for-detail-miner-list-user_data"""
        return self.get('/sapi/v1/mining/worker/detail',
                        algo=algo,
                        userName=userName,
                        workerName=workerName,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def request_for_miner_list(self,
                               algo: str = None,
                               userName: str = None,
                               pageIndex: int = None,
                               sort: int = None,
                               sortColumn: int = None,
                               workerStatus: int = None,
                               recvWindow: int = None,
                               time_req: bool = True,
                               sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#request-for-miner-list-user_data"""
        return self.get('/sapi/v1/mining/worker/list',
                        algo=algo,
                        userName=userName,
                        pageIndex=pageIndex,
                        sort=sort,
                        sortColumn=sortColumn,
                        workerStatus=workerStatus,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def earnings_list(self,
                      algo: str = None,
                      userName: str = None,
                      coin: str = None,
                      start_time: dt.datetime = None,
                      end_time: dt.datetime = None,
                      pageIndex: int = None,
                      pageSize: int = None,
                      recvWindow: int = None,
                      time_req: bool = True,
                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#earnings-list-user_data"""
        return self.get('/sapi/v1/mining/payment/list',
                        algo=algo,
                        userName=userName,
                        coin=coin,
                        start_time=start_time,
                        end_time=end_time,
                        pageIndex=pageIndex,
                        pageSize=pageSize,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def extra_bonus_list(self,
                         algo: str = None,
                         userName: str = None,
                         coin: str = None,
                         start_time: dt.datetime = None,
                         end_time: dt.datetime = None,
                         pageIndex: int = None,
                         pageSize: int = None,
                         recvWindow: int = None,
                         time_req: bool = True,
                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#extra-bonus-list-user_data"""
        return self.get('/sapi/v1/mining/payment/other',
                        algo=algo,
                        userName=userName,
                        coin=coin,
                        start_time=start_time,
                        end_time=end_time,
                        pageIndex=pageIndex,
                        pageSize=pageSize,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def hashrate_resale_list(self,
                             pageIndex: int = None,
                             pageSize: int = None,
                             recvWindow: int = None,
                             time_req: bool = True,
                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-list-user_data"""
        return self.get('/sapi/v1/mining/hash-transfer/config/details/list',
                        pageIndex=pageIndex,
                        pageSize=pageSize,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def hashrate_resale_detail(self,
                               configId: int = None,
                               userName: str = None,
                               pageIndex: int = None,
                               pageSize: int = None,
                               recvWindow: int = None,
                               time_req: bool = True,
                               sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-detail-user_data"""
        return self.get('/sapi/v1/mining/hash-transfer/profit/details',
                        configId=configId,
                        userName=userName,
                        pageSize=pageSize,
                        pageIndex=pageIndex,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def hashrate_resale_request(self,
                                userName: str = None,
                                algo: str = None,
                                start_time: dt.datetime = None,
                                end_time: dt.datetime = None,
                                toPoolUser: str = None,
                                hashRate: int = None,
                                recvWindow: int = None,
                                time_req: bool = True,
                                sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-request-user_data"""
        return self.post('/sapi/v1/mining/hash-transfer/config',
                         userName=userName,
                         algo=algo,
                         start_time=start_time,
                         end_time=end_time,
                         toPoolUser=toPoolUser,
                         hashRate=hashRate,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def cancel_hashrate_resale_configuration(self,
                                             configId: int = None,
                                             userName: str = None,
                                             recvWindow: int = None,
                                             time_req: bool = True,
                                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cancel-hashrate-resale-configuration-user_data"""
        return self.post('/sapi/v1/mining/hash-transfer/config/cancel',
                         configId=configId,
                         userName=userName,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def statistic_list(self,
                       algo: str = None,
                       userName: str = None,
                       recvWindow: int = None,
                       time_req: bool = True,
                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#statistic-list-user_data"""
        return self.get('/sapi/v1/mining/statistics/user/status',
                        algo=algo,
                        userName=userName,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def account_list(self,
                     algo: str = None,
                     userName: str = None,
                     recvWindow: int = None,
                     time_req: bool = True,
                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#account-list-user_data"""
        return self.get('/sapi/v1/mining/statistics/user/list',
                        algo=algo,
                        userName=userName,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
