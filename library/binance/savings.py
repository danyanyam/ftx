from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class Savings(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#margin-account-trade"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def get_flx_product_list(self,
                             status: str = None,
                             featured: str = None,
                             current: int = None,
                             size: int = None,
                             recvWindow: int = None,
                             time_req: bool = True,
                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-margin-account-transfer-margin"""
        return self.get('/sapi/v1/lending/daily/product/list',
                        status=status,
                        featured=featured,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_left_daily_quota(self,
                             productId: str = None,
                             recvWindow: int = None,
                             time_req: bool = True,
                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-purchase-quota-of-flexible-product-user_data"""
        return self.get('/sapi/v1/lending/daily/userLeftQuota',
                        productId=productId,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def purchase_daily_product(self,
                               productId: str = 'BUSD',
                               amount: float = 0.001,
                               recvWindow: int = None,
                               time_req: bool = True,
                               sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#purchase-flexible-product-user_data"""
        return self.post('/sapi/v1/lending/daily/purchase',
                         productId=productId,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_left_daily_redemption_quota(self,
                                        productId: str = None,
                                        type: str = None,
                                        recvWindow: int = None,
                                        time_req: bool = True,
                                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-left-daily-redemption-quota-of-flexible-product-user_data"""

        assert type in ["FAST", "NORMAL"], f'{type} is not in possible values'

        return self.get('/sapi/v1/lending/daily/userRedemptionQuota',
                        productId=productId,
                        type=type,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def redeem_flx_product(self,
                           productId: str = 'BUSD',
                           amount: float = 0.001,
                           type: str = None,
                           recvWindow: int = None,
                           time_req: bool = True,
                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#redeem-flexible-product-user_data"""
        return self.post('/sapi/v1/lending/daily/redeem',
                         productId=productId,
                         amount=amount,
                         type=type,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_flx_product_position(self,
                                 asset: str = None,
                                 recvWindow: int = None,
                                 time_req: bool = True,
                                 sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-position-user_data"""
        return self.get('/sapi/v1/lending/daily/token/position',
                        asset=asset,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_flexible_product_position(self,
                                      asset: str = None,
                                      recvWindow: int = None,
                                      time_req: bool = True,
                                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-flexible-product-position-user_data"""
        return self.get('/sapi/v1/lending/daily/token/position',
                        asset=asset,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_fixed_and_activity_product_list(self,
                                            type: str = None,
                                            status: str = None,
                                            isSortAsc: str = None,
                                            sortBy: str = None,
                                            current: int = None,
                                            size: int = None,
                                            recvWindow: int = None,
                                            time_req: bool = True,
                                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-fixed-and-activity-project-list-user_data"""
        return self.get('/sapi/v1/lending/project/list',
                        type=type,
                        status=status,
                        isSortAsc=isSortAsc,
                        sortBy=sortBy,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def purchase_fixed_act_product(self,
                                   projectId: str = None,
                                   lot: int = None,
                                   recvWindow: int = None,
                                   time_req: bool = True,
                                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#purchase-fixed-activity-project-user_data"""
        return self.post('/sapi/v1/lending/customizedFixed/purchase',
                         projectId=projectId,
                         lot=lot,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_fixed_activity_project_position(self,
                                            asset: str = None,
                                            projectId: str = None,
                                            status: str = None,
                                            recvWindow: int = None,
                                            time_req: bool = True,
                                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-fixed-activity-project-position-user_data"""
        return self.get('/sapi/v1/lending/project/position/list',
                        asset=asset,
                        projectId=projectId,
                        status=status,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def lending_amount(self,
                       recvWindow: int = None,
                       time_req: bool = True,
                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#lending-account-user_data"""
        return self.get('/sapi/v1/lending/union/account',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_purchase_record(self,
                            lendingType: str = None,
                            asset: str = None,
                            start_time: dt.datetime = None,
                            end_time: dt.datetime = None,
                            current: int = None,
                            size: int = None,
                            recvWindow: int = None,
                            time_req: bool = True,
                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-purchase-record-user_data"""
        return self.get('/sapi/v1/lending/union/purchaseRecord',
                        lendingType=lendingType,
                        asset=asset,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_redemption_record(self,
                              lendingType: str = None,
                              asset: str = None,
                              start_time: dt.datetime = None,
                              end_time: dt.datetime = None,
                              current: int = None,
                              size: int = None,
                              recvWindow: int = None,
                              time_req: bool = True,
                              sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-redemption-record-user_data"""
        return self.get('/sapi/v1/lending/union/redemptionRecord',
                        lendingType=lendingType,
                        asset=asset,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_interest_history(self,
                             lendingType: str = None,
                             asset: str = None,
                             start_time: dt.datetime = None,
                             end_time: dt.datetime = None,
                             current: int = None,
                             size: int = None,
                             recvWindow: int = None,
                             time_req: bool = True,
                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-interest-history-user_data-2"""
        return self.get('/sapi/v1/lending/union/interestHistory',
                        lendingType=lendingType,
                        asset=asset,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def change_fixed_activity_position_to_daily_position(self,
                                                         projectId: str = None,
                                                         lot: int = None,
                                                         positionId: int = None,
                                                         recvWindow: int = None,
                                                         time_req: bool = True,
                                                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#change-fixed-activity-position-to-daily-position-user_data"""
        return self.post('/sapi/v1/lending/positionChanged',
                         projectId=projectId,
                         lot=lot,
                         positionId=positionId,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)
