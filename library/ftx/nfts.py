from library.ftx.base import BaseApiClass
import datetime as dt

# TODO: check links


class Nft(BaseApiClass):

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name, 'https://ftx.com')

    def list_nfts(self):
        """ https://docs.ftx.com/#list-nfts """
        return self.get('/api/nft/nfts')

    def get_nft_info(self, nft_id: int):
        """ https://docs.ftx.com/#get-nft-info """
        return self.get(f'/api/nft/{nft_id}')

    def get_nft_trades(self, nft_id: int, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-trades """
        return self.get(f'/api/nft/{nft_id}/trades', start_time=start_time, end_time=end_time)

    def get_all_nft_trades(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-all-nft-trades """
        return self.get(f'/api/nft/all_trades', start_time=start_time, end_time=end_time)

    def get_nft_account_info(self, nft_id: int):
        """ https://docs.ftx.com/#get-nft-account-info """
        return self.get(f'/api/nft/{nft_id}')

    def get_all_nft_collections(self):
        """ https://docs.ftx.com/#get-all-nft-collections """
        return self.get(f'/api/nft/collections')

    def get_nft_balances(self):
        """ https://docs.ftx.com/#get-nft-account-info """
        return self.get(f'/api/bft/balances')

    def make_nft_offer(self, nftId: int, price: float):
        """ https://docs.ftx.com/#make-nft-offer """
        return self.post('/api/ndt/offer', data={'nftId': nftId, 'price': price})

    def buy_nft(self, nftId: int, price: float):
        """ https://docs.ftx.com/#make-nft-offer """
        return self.post('/api/ndt/buy', data={'nftId': nftId, 'price': price})

    def create_auction(self, initialPrice: float, reservationPrice: float, duration: int):
        """ https://docs.ftx.com/#create-auction """
        return self.post('/api/nft/auction', data={'initialPrice': initialPrice, 'reservationPrice': reservationPrice, 'duration': duration})

    def edit_auction(self, reservationPrice: float):
        """ https://docs.ftx.com/#edit-auction """
        return self.post('/api/nft/edit_auction', data={'reservationPrice': reservationPrice})

    def cancel_auction(self, nftId: int, reservationPrice: float):
        """ https://docs.ftx.com/#cancel-auction """
        return self.post('/api/nft/cancel_auction', data={'nftId': nftId, 'reservationPrice': reservationPrice})

    def get_bids(self):
        """ https://docs.ftx.com/#get-bids """
        return self.get('/api/nft/bids')

    def place_bid(self, nftId: int, price: float):
        """ https://docs.ftx.com/#place-bid """
        return self.post('/api/nft/bids', data={'nftId': nftId, 'price': price})

    def get_nft_deposits(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-deposits """
        return self.get('/api/nft/deposits', start_time=start_time, end_time=end_time)

    def get_nft_withdrawals(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-withdrawals """
        return self.get('/api/nft/withdrawals', start_time=start_time, end_time=end_time)

    def get_nft_fills(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-fills """
        return self.get('/api/nft/fills', start_time=start_time, end_time=end_time)

    def redeem_nft(self, nftId: int, address: str, notes: str):
        """ https://docs.ftx.com/#redeem-nft """
        return self.post('/api/nft/redeem', data={'nftId': nftId, 'address': address, 'notes': notes})

    def get_nft_gallery(self, gallery_id: int):
        """ https://docs.ftx.com/#get-nft-gallery """
        return self.get(f'/api/nft/gallery/{gallery_id}')

    def get_gallery_settings(self):
        """ https://docs.ftx.com/#get-gallery-settings """
        return self.get(f'/api/nft/gallery_settings')

    def edit_gallery_settings(self, public: bool = True):
        """ https://docs.ftx.com/#get-gallery-settings """
        assert isinstance(public, bool)
        return self.get(f'/api/nft/gallery_settings', data={'public': public})
