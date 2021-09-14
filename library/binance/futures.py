from base import BaseApiClass
import datetime as dt


class Futures(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#futures"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def new_future_account_transfer(self,
                                    asset: str = None,
                                    amount: float = None,
                                    type: int = None,
                                    recvWindow: int = None,
                                    time_req: bool = True,
                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#acquiring-algorithm-user_data"""
        return self.post('/sapi/v1/futures/transfer',
                         asset=asset,
                         amount=amount,
                         type=type,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_future_account_transaction_history_list(self,
                                                    asset: str = None,
                                                    start_time: dt.datetime = None,
                                                    end_time: dt.datetime = None,
                                                    current: int = None,
                                                    size: int = None,
                                                    recvWindow: int = None,
                                                    time_req: bool = True,
                                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-future-account-transaction-history-list-user_data"""
        return self.get('/sapi/v1/futures/transfer',
                        asset=asset,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def borrow_for_cross_collateral(self,
                                    coin: str = None,
                                    amount: float = None,
                                    collateralCoin: str = None,
                                    collateralAmount: float = None,
                                    recvWindow: int = None,
                                    time_req: bool = True,
                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#borrow-for-cross-collateral-trade"""
        return self.post('/sapi/v1/futures/loan/borrow',
                         coin=coin,
                         amount=amount,
                         collateralCoin=collateralCoin,
                         collateralAmount=collateralAmount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def cross_collateral_borrow_history(self,
                                        coin: str = None,
                                        start_time: dt.datetime = None,
                                        end_time: dt.datetime = None,
                                        limit: int = None,
                                        recvWindow: int = None,
                                        time_req: bool = True,
                                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-borrow-history-user_data"""
        return self.get('/sapi/v1/futures/loan/borrow/history',
                        coin=coin,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def repay_for_cross_collateral(self,
                                   coin: str = None,
                                   collateralCoin: str = None,
                                   amount: float = None,
                                   recvWindow: int = None,
                                   time_req: bool = True,
                                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#repay-for-cross-collateral-trade"""
        return self.post('/sapi/v1/futures/loan/repay',
                         coin=coin,
                         collateralCoin=collateralCoin,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def cross_collateral_repayment_history(self,
                                           coin: str = None,
                                           start_time: dt.datetime = None,
                                           end_time: dt.datetime = None,
                                           limit: int = None,
                                           recvWindow: int = None,
                                           time_req: bool = True,
                                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-repayment-history-user_data"""
        return self.get('/sapi/v1/futures/loan/repay/history',
                        coin=coin,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def cross_collateral_wallet(self,
                                recvWindow: int = None,
                                time_req: bool = True,
                                sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-wallet-user_data"""
        return self.get('/sapi/v1/futures/loan/wallet',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def cross_collateral_wallet_v2(self,
                                   recvWindow: int = None,
                                   time_req: bool = True,
                                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-wallet-v2-user_data"""
        return self.get('/sapi/v2/futures/loan/wallet',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def cross_collateral_information(self,
                                     collateralCoin: str = None,
                                     recvWindow: int = None,
                                     time_req: bool = True,
                                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-information-user_data"""
        return self.get('/sapi/v1/futures/loan/configs',
                        collateralCoin=collateralCoin,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def cross_collateral_information_v2(self,
                                        loanCoin: str = None,
                                        collateralCoin: str = None,
                                        recvWindow: int = None,
                                        time_req: bool = True,
                                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-information-v2-user_data"""
        return self.get('/sapi/v2/futures/loan/configs',
                        loanCoin=loanCoin,
                        collateralCoin=collateralCoin,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def calculate_rate_after_adjust_cross_collateral_LTV(self,
                                                         collateralCoin: str = None,
                                                         amount: float = None,
                                                         direction: str = None,
                                                         recvWindow: int = None,
                                                         time_req: bool = True,
                                                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#calculate-rate-after-adjust-cross-collateral-ltv-user_data"""
        return self.get('/sapi/v1/futures/loan/calcAdjustLevel',
                        collateralCoin=collateralCoin,
                        amount=amount,
                        direction=direction,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def calculate_rate_after_adjust_cross_collateral_LTV_v2(self,
                                                            loanCoin: str = None,
                                                            collateralCoin: str = None,
                                                            amount: float = None,
                                                            direction: str = None,
                                                            recvWindow: int = None,
                                                            time_req: bool = True,
                                                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#calculate-rate-after-adjust-cross-collateral-ltv-v2-user_data"""
        return self.get('/sapi/v2/futures/loan/calcAdjustLevel',
                        loanCoin=loanCoin,
                        collateralCoin=collateralCoin,
                        amount=amount,
                        direction=direction,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_max_amount_for_adjust_cross_collateral_LTV(self,
                                                       collateralCoin: str = None,
                                                       recvWindow: int = None,
                                                       time_req: bool = True,
                                                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-max-amount-for-adjust-cross-collateral-ltv-user_data"""
        return self.get('/sapi/v1/futures/loan/calcMaxAdjustAmount',
                        collateralCoin=collateralCoin,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_max_amount_for_adjust_cross_collateral_LTV_v2(self,
                                                          loanCoin: str = None,
                                                          collateralCoin: str = None,
                                                          recvWindow: int = None,
                                                          time_req: bool = True,
                                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-max-amount-for-adjust-cross-collateral-ltv-v2-user_data"""
        return self.get('/sapi/v2/futures/loan/calcMaxAdjustAmount',
                        loanCoin=loanCoin,
                        collateralCoin=collateralCoin,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def adjust_cross_collateral_LTV(self,
                                    collateralCoin: str = None,
                                    amount: float = None,
                                    direction: str = None,
                                    recvWindow: int = None,
                                    time_req: bool = True,
                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-trade"""
        return self.post('/sapi/v1/futures/loan/adjustCollateral',
                         collateralCoin=collateralCoin,
                         amount=amount,
                         direction=direction,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def adjust_cross_collateral_LTV_v2(self,
                                       loanCoin: str = None,
                                       collateralCoin: str = None,
                                       amount: float = None,
                                       direction: str = None,
                                       recvWindow: int = None,
                                       time_req: bool = True,
                                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-v2-trade"""
        return self.post('/sapi/v2/futures/loan/adjustCollateral',
                         loanCoin=loanCoin,
                         collateralCoin=collateralCoin,
                         amount=amount,
                         direction=direction,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def adjust_cross_collateral_LTV_history(self,
                                            loanCoin: str = None,
                                            collateralCoin: str = None,
                                            start_time: dt.datetime = None,
                                            end_time: dt.datetime = None,
                                            limit: int = None,
                                            recvWindow: int = None,
                                            time_req: bool = True,
                                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#adjust-cross-collateral-ltv-history-user_data"""
        return self.get('/sapi/v1/futures/loan/adjustCollateral/history',
                        loanCoin=loanCoin,
                        collateralCoin=collateralCoin,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def cross_collateral_liquidation_history(self,
                                             loanCoin: str = None,
                                             collateralCoin: str = None,
                                             start_time: dt.datetime = None,
                                             end_time: dt.datetime = None,
                                             limit: int = None,
                                             recvWindow: int = None,
                                             time_req: bool = True,
                                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-liquidation-history-user_data"""
        return self.get('/sapi/v1/futures/loan/liquidationHistory',
                        loanCoin=loanCoin,
                        collateralCoin=collateralCoin,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def check_collateral_repay_limit(self,
                                     coin: str = None,
                                     collateralCoin: str = None,
                                     recvWindow: int = None,
                                     time_req: bool = True,
                                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#check-collateral-repay-limit-user_data"""
        return self.get('/sapi/v1/futures/loan/collateralRepayLimit',
                        coin=coin,
                        collateralCoin=collateralCoin,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_collateral_repay_quote(self,
                                   coin: str = None,
                                   collateralCoin: str = None,
                                   amount: float = None,
                                   recvWindow: int = None,
                                   time_req: bool = True,
                                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-collateral-repay-quote-user_data"""
        return self.get('/sapi/v1/futures/loan/collateralRepay',
                        coin=coin,
                        collateralCoin=collateralCoin,
                        amount=amount,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def repay_with_collateral(self,
                              quoteId: str = None,
                              recvWindow: int = None,
                              time_req: bool = True,
                              sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#repay-with-collateral-user_data"""
        return self.post('/sapi/v1/futures/loan/collateralRepay',
                         quoteId=quoteId,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def collateral_repayment_result(self,
                                    quoteId: str = None,
                                    recvWindow: int = None,
                                    time_req: bool = True,
                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#collateral-repayment-result-user_data"""
        return self.get('/sapi/v1/futures/loan/collateralRepayResult',
                        quoteId=quoteId,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def cross_collateral_interest_history(self,
                                          collateralCoin: str = None,
                                          start_time: dt.datetime = None,
                                          end_time: dt.datetime = None,
                                          current: int = None,
                                          limit: int = None,
                                          recvWindow: int = None,
                                          time_req: bool = True,
                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-collateral-interest-history-user_data"""
        return self.get('/sapi/v1/futures/loan/interestHistory',
                        collateralCoin=collateralCoin,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
