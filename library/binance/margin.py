from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class Margin(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#margin-account-trade"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def cross_margin_account_transfer(self,
                                      asset: str = 'BTC',
                                      amount: float = 0.01,
                                      type: int = 1,
                                      recvWindow: int = None,
                                      time_req: bool = True,
                                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-margin-account-transfer-margin"""
        return self.post('/sapi/v1/margin/transfer',
                         asset=asset,
                         amount=amount,
                         type=type,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def margin_account_borrow(self,
                              asset: str = 'BTC',
                              isIsolated: str = None,
                              symbol: str = None,
                              amount: float = 0.00001,
                              recvWindow: int = None,
                              time_req: bool = True,
                              sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-borrow-margin"""
        return self.post('/sapi/v1/margin/loan',
                         asset=asset,
                         isIsolated=isIsolated,
                         symbol=symbol,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def magrin_account_repay(self,
                             asset: str = None,
                             isIsolated: str = None,
                             symbol: str = None,
                             amount: float = None,
                             recvWindow: int = None,
                             time_req: bool = True,
                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-repay-margin"""
        return self.post('/sapi/v1/margin/repay',
                         asset=asset,
                         isIsolated=isIsolated,
                         symbol=symbol,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def query_margin_asset(self,
                           asset: str = None,
                           recvWindow: int = None,
                           time_req: bool = True,
                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-asset-market_data"""
        return self.get('/sapi/v1/margin/asset',
                        asset=asset,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_cross_margin_pair(self,
                                symbol: str = None,
                                recvWindow: int = None,
                                time_req: bool = True,
                                sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-cross-margin-pair-market_data"""
        return self.get('/sapi/v1/margin/pair',
                        symbol=symbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_all_margin_assets(self,
                              recvWindow: int = None,
                              time_req: bool = True,
                              sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-all-margin-assets-market_data"""
        return self.get('/sapi/v1/margin/allAssets',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_all_cross_margin_pairs(self,
                                   recvWindow: int = None,
                                   time_req: bool = True,
                                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-all-cross-margin-pairs-market_data"""
        return self.get('/sapi/v1/margin/allPairs',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_priceIndex(self,
                                symbol: str = None,
                                recvWindow: int = None,
                                time_req: bool = True,
                                sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-priceindex-market_data"""
        return self.get('/sapi/v1/margin/priceIndex',
                        symbol=symbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def margin_account_new_order(self,
                                 symbol: str = None,
                                 isIsolated: str = None,
                                 side: str = None,
                                 type: str = None,
                                 quantity: float = None,
                                 quoteOrderQty: float = None,
                                 price: float = None,
                                 stopPrice: float = None,
                                 newClientOrderId: str = None,
                                 icebergQty: float = None,
                                 newOrderRespType: str = None,
                                 sideEffectType: str = None,
                                 timeInForce: str = None,
                                 recvWindow: int = None,
                                 time_req: bool = True,
                                 sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-new-order-trade"""
        return self.post('/sapi/v1/margin/order',
                         symbol=symbol,
                         isIsolated=isIsolated,
                         side=side,
                         type=type,
                         quantity=quantity,
                         quoteOrderQty=quoteOrderQty,
                         price=price,
                         stopPrice=stopPrice,
                         newClientOrderId=newClientOrderId,
                         icebergQty=icebergQty,
                         newOrderRespType=newOrderRespType,
                         sideEffectType=sideEffectType,
                         timeInForce=timeInForce,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def margin_account_cancel_order(self,
                                    symbol: str = None,
                                    isIsolated: str = None,
                                    orderId: int = None,
                                    origClientOrderId: str = None,
                                    newClientOrderId: str = None,
                                    recvWindow: int = None,
                                    time_req: bool = True,
                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-cancel-order-trade"""
        return self.delete('/sapi/v1/margin/order',
                           symbol=symbol,
                           isIsolated=isIsolated,
                           orderId=orderId,
                           origClientOrderId=origClientOrderId,
                           newClientOrderId=newClientOrderId,
                           recvWindow=recvWindow,
                           time_req=time_req,
                           sign=sign)

    def margin_account_cancel_all_open_orders_on_a_symbol(self,
                                                          symbol: str = None,
                                                          isIsolated: str = None,
                                                          recvWindow: int = None,
                                                          time_req: bool = True,
                                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-cancel-all-open-orders-on-a-symbol-trade"""
        return self.delete('/sapi/v1/margin/openOrders',
                           symbol=symbol,
                           isIsolated=isIsolated,
                           recvWindow=recvWindow,
                           time_req=time_req,
                           sign=sign)

    def get_cross_margin_transfer_history(self,
                                          asset: str = None,
                                          type: str = None,
                                          start_time: dt.datetime = None,
                                          end_time: dt.datetime = None,
                                          current: str = None,
                                          size: int = None,
                                          archived: str = None,
                                          recvWindow: int = None,
                                          time_req: bool = True,
                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-cross-margin-transfer-history-user_data"""
        return self.get('/sapi/v1/margin/transfer',
                        asset=asset,
                        type=type,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        archived=archived,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_loan_record(self,
                          asset: str = None,
                          isolatedSymbol: str = None,
                          txId: str = None,
                          start_time: dt.datetime = None,
                          end_time: dt.datetime = None,
                          current: str = None,
                          size: int = None,
                          archived: str = None,
                          recvWindow: int = None,
                          time_req: bool = True,
                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-loan-record-user_data"""

        assert txId is not None or start_time is not None, 'txId or start_time must be sent. txId takes precedence'

        return self.get('/sapi/v1/margin/loan',
                        asset=asset,
                        isolatedSymbol=isolatedSymbol,
                        txId=txId,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        archived=archived,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_repay_record(self,
                           asset: str = None,
                           isolatedSymbol: str = None,
                           txId: str = None,
                           start_time: dt.datetime = None,
                           end_time: dt.datetime = None,
                           current: str = None,
                           size: int = None,
                           archived: str = None,
                           recvWindow: int = None,
                           time_req: bool = True,
                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-repay-record-user_data"""

        assert txId is not None or start_time is not None, 'txId or start_time must be sent. txId takes precedence'

        return self.get('/sapi/v1/margin/repay',
                        asset=asset,
                        isolatedSymbol=isolatedSymbol,
                        txId=txId,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        archived=archived,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_interest_history(self,
                             asset: str = None,
                             isolatedSymbol: str = None,
                             start_time: dt.datetime = None,
                             end_time: dt.datetime = None,
                             current: str = None,
                             size: int = None,
                             archived: str = None,
                             recvWindow: int = None,
                             time_req: bool = True,
                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-interest-history-user_data"""

        return self.get('/sapi/v1/margin/interestHistory',
                        asset=asset,
                        isolatedSymbol=isolatedSymbol,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        archived=archived,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_force_liquidation_record(self,
                                     start_time: dt.datetime = None,
                                     end_time: dt.datetime = None,
                                     isolatedSymbol: str = None,
                                     current: str = None,
                                     size: int = None,
                                     recvWindow: int = None,
                                     time_req: bool = True,
                                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-force-liquidation-record-user_data"""
        return self.get('/sapi/v1/margin/forceLiquidationRec',
                        start_time=start_time,
                        end_time=end_time,
                        isolatedSymbol=isolatedSymbol,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_cross_margin_account_details(self,
                                           recvWindow: int = None,
                                           time_req: bool = True,
                                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-cross-margin-account-details-user_data"""
        return self.get('/sapi/v1/margin/account',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_accounts_order(self,
                                    symbol: str = None,
                                    isolatedSymbol: str = None,
                                    orderId: str = None,
                                    origClientOrderId: str = None,
                                    recvWindow: int = None,
                                    time_req: bool = True,
                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-order-user_data"""
        return self.get('/sapi/v1/margin/order',
                        symbol=symbol,
                        isolatedSymbol=isolatedSymbol,
                        orderId=orderId,
                        orig=origClientOrderId,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_accounts_open_orders(self,
                                          symbol: str = None,
                                          isolatedSymbol: str = None,
                                          recvWindow: int = None,
                                          time_req: bool = True,
                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-open-orders-user_data"""
        return self.get('/sapi/v1/margin/openOrders',
                        symbol=symbol,
                        isolatedSymbol=isolatedSymbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_accounts_all_orders(self,
                                         symbol: str = None,
                                         isolatedSymbol: str = None,
                                         orderId: str = None,
                                         start_time: dt.datetime = None,
                                         end_time: dt.datetime = None,
                                         limit: int = None,
                                         recvWindow: int = None,
                                         time_req: bool = True,
                                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-all-orders-user_data"""
        return self.get('/sapi/v1/margin/allOrders',
                        symbol=symbol,
                        isolatedSymbol=isolatedSymbol,
                        orderId=orderId,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def margin_account_new_OCO(self,
                               symbol: str = None,
                               isIsolated: str = None,
                               listClientOrderId: str = None,
                               side: str = None,
                               quantity: float = None,
                               limitClientOrderId: str = None,
                               price: float = None,
                               limitIcebergQty: float = None,
                               stopClientOrderId: str = None,
                               stopPrice: float = None,
                               stopLimitPrice: float = None,
                               stopIcebergQty: float = None,
                               stopLimitTimeInForce: str = None,
                               newOrderRespType: str = None,
                               sideEffectType: str = None,
                               recvWindow: int = None,
                               time_req: bool = True,
                               sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-new-oco-trade"""
        return self.post('/sapi/v1/margin/order/oco',
                         symbol=symbol,
                         isIsolated=isIsolated,
                         listClientOrderId=listClientOrderId,
                         side=side,
                         quantity=quantity,
                         limitClientOrderId=limitClientOrderId,
                         price=price,
                         limitIcebergQty=limitIcebergQty,
                         stopClientOrderId=stopClientOrderId,
                         stopPrice=stopPrice,
                         stopIcebergQty=stopIcebergQty,
                         stopLimitPrice=stopLimitPrice,
                         stopLimitTimeInForce=stopLimitTimeInForce,
                         newOrderRespType=newOrderRespType,
                         sideEffectType=sideEffectType,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def margin_account_cancel_OCO(self,
                                  symbol: str = None,
                                  isIsolated: str = None,
                                  orderListId: str = None,
                                  listClientOrderId: str = None,
                                  newClientOrderId: str = None,
                                  recvWindow: int = None,
                                  time_req: bool = True,
                                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-cancel-oco-trade"""
        return self.delete('/sapi/v1/margin/orderList',
                           symbol=symbol,
                           isIsolated=isIsolated,
                           orderListId=orderListId,
                           listClientOrderId=listClientOrderId,
                           newClientOrderId=newClientOrderId,
                           recvWindow=recvWindow,
                           time_req=time_req,
                           sign=sign)

    def query_margin_accounts_OCO(self,
                                  isIsolated: str = None,
                                  symbol: str = None,
                                  orderListId: str = None,
                                  origClientOrderId: str = None,
                                  recvWindow: int = None,
                                  time_req: bool = True,
                                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-oco-user_data"""
        return self.get('/sapi/v1/margin/orderList',
                        isIsolated=isIsolated,
                        symbol=symbol,
                        orderListId=orderListId,
                        origClientOrderId=origClientOrderId,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_accounts_all_OCO(self,
                                      isIsolated: str = None,
                                      symbol: str = None,
                                      fromId: str = None,
                                      start_time: dt.datetime = None,
                                      end_time: dt.datetime = None,
                                      limit: int = None,
                                      recvWindow: int = None,
                                      time_req: bool = True,
                                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-all-oco-user_data"""
        return self.get('/sapi/v1/margin/allOrderList',
                        isIsolated=isIsolated,
                        symbol=symbol,
                        fromId=fromId,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_accounts_open_OCO(self,
                                       isIsolated: str = None,
                                       symbol: str = None,
                                       recvWindow: int = None,
                                       time_req: bool = True,
                                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-open-oco-user_data"""
        return self.get('/sapi/v1/margin/openOrderList',
                        isIsolated=isIsolated,
                        symbol=symbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_accounts_trade_list(self,
                                         isIsolated: str = None,
                                         symbol: str = None,
                                         fromId: str = None,
                                         start_time: dt.datetime = None,
                                         end_time: dt.datetime = None,
                                         limit: int = None,
                                         recvWindow: int = None,
                                         time_req: bool = True,
                                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-account-39-s-trade-list-user_data"""
        return self.get('/sapi/v1/margin/myTrades',
                        isIsolated=isIsolated,
                        symbol=symbol,
                        fromId=fromId,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_max_borrow(self,
                         asset: str = None,
                         isolatedSymbol: str = None,
                         recvWindow: int = None,
                         time_req: bool = True,
                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-max-borrow-user_data"""
        return self.get('/sapi/v1/margin/maxBorrowable',
                        asset=asset,
                        isolatedSymbol=isolatedSymbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_max_transfer_out_amount(self,
                                      asset: str = None,
                                      isolatedSymbol: str = None,
                                      recvWindow: int = None,
                                      time_req: bool = True,
                                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-max-transfer-out-amount-user_data"""
        return self.get('/sapi/v1/margin/maxTransferable',
                        asset=asset,
                        isolatedSymbol=isolatedSymbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def isolated_margin_account_transfer(self,
                                         asset: str = None,
                                         symbol: str = None,
                                         transFrom: str = None,
                                         transTo: str = None,
                                         amount: float = None,
                                         recvWindow: int = None,
                                         time_req: bool = True,
                                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#isolated-margin-account-transfer-margin"""
        return self.post('/sapi/v1/margin/isolated/transfer',
                         asset=asset,
                         symbol=symbol,
                         transFrom=transFrom,
                         transTo=transTo,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_isolated_margin_transfer_history(self,
                                             asset: str = None,
                                             symbol: str = None,
                                             transFrom: str = None,
                                             transTo: str = None,
                                             start_time: dt.datetime = None,
                                             end_time: dt.datetime = None,
                                             current: int = None,
                                             size: int = None,
                                             recvWindow: int = None,
                                             time_req: bool = True,
                                             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-isolated-margin-transfer-history-user_data"""
        return self.get('/sapi/v1/margin/isolated/transfer',
                        asset=asset,
                        symbol=symbol,
                        transFrom=transFrom,
                        transTo=transTo,
                        start_time=start_time,
                        end_time=end_time,
                        current=current,
                        size=size,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_isolated_margin_account_info(self,
                                           symbols: str = None,
                                           recvWindow: int = None,
                                           time_req: bool = True,
                                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-account-info-user_data"""
        return self.get('/sapi/v1/margin/isolated/account',
                        symbols=symbols,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def disable_isolated_margin_account(self,
                                        symbol: str = None,
                                        recvWindow: int = None,
                                        time_req: bool = True,
                                        sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#disable-isolated-margin-account-trade"""
        return self.delete('/sapi/v1/margin/isolated/account',
                           symbol=symbol,
                           recvWindow=recvWindow,
                           time_req=time_req,
                           sign=sign)

    def enable_isolated_margin_account(self,
                                       symbol: str = None,
                                       recvWindow: int = None,
                                       time_req: bool = True,
                                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#enable-isolated-margin-account-trade"""
        return self.post('/sapi/v1/margin/isolated/account',
                         symbol=symbol,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def query_enabled_isolated_margin_account_limit(self,
                                                    recvWindow: int = None,
                                                    time_req: bool = True,
                                                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-enabled-isolated-margin-account-limit-user_data"""
        return self.get('/sapi/v1/margin/isolated/accountLimit',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_isolated_margin_symbol(self,
                                     symbol: str = None,
                                     recvWindow: int = None,
                                     time_req: bool = True,
                                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-isolated-margin-symbol-user_data"""
        return self.get('/sapi/v1/margin/isolated/pair',
                        symbol=symbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_all_isolated_margin_symbol(self,
                                       recvWindow: int = None,
                                       time_req: bool = True,
                                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-all-isolated-margin-symbol-user_data"""
        return self.get('/sapi/v1/margin/isolated/allPairs',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def toggle_BNB_burn_on_spot_trade_and_margin_interest(self,
                                                          spotBNBBurn: str = None,
                                                          interestBNBBurn: str = None,
                                                          recvWindow: int = None,
                                                          time_req: bool = True,
                                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#toggle-bnb-burn-on-spot-trade-and-margin-interest-user_data"""
        return self.post('/sapi/v1/bnbBurn',
                         spotBNBBurn=spotBNBBurn,
                         interestBNBBurn=interestBNBBurn,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_BNB_burn_status(self,
                            recvWindow: int = None,
                            time_req: bool = True,
                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-bnb-burn-status-user_data"""
        return self.get('/sapi/v1/bnbBurn',
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def query_margin_interest_rate_history(self,
                                           asset: str = None,
                                           vipLevel: int = None,
                                           start_time: dt.datetime = None,
                                           end_time: dt.datetime = None,
                                           limit: int = None,
                                           recvWindow: int = None,
                                           time_req: bool = True,
                                           sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-margin-interest-rate-history-user_data"""
        return self.get('/sapi/v1/margin/interestRateHistory',
                        asset=asset,
                        vipLevel=vipLevel,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
