from library.ftx.base import BaseApiClass
import datetime as dt

# TODO: check links


class Nft(BaseApiClass):

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name, 'https://ftx.com')

    async def list_nfts(self):
        """ https://docs.ftx.com/#list-nfts """
        return await self.get('/api/nft/nfts')

    async def get_nft_info(self, nft_id: int):
        """ https://docs.ftx.com/#get-nft-info """
        return await self.get(f'/api/nft/{nft_id}')

    async def get_nft_trades(self, nft_id: int, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-trades """
        return await self.get(f'/api/nft/{nft_id}/trades', start_time=start_time, end_time=end_time)

    async def get_all_nft_trades(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-all-nft-trades """
        return await self.get(f'/api/nft/all_trades', start_time=start_time, end_time=end_time)

    async def get_nft_account_info(self, nft_id: int):
        """ https://docs.ftx.com/#get-nft-account-info """
        return await self.get(f'/api/nft/{nft_id}')

    async def get_all_nft_collections(self):
        """ https://docs.ftx.com/#get-all-nft-collections """
        return await self.get(f'/api/nft/collections')

    async def get_nft_balances(self):
        """ https://docs.ftx.com/#get-nft-account-info """
        return await self.get(f'/api/bft/balances')

    async def make_nft_offer(self, nftId: int, price: float):
        """ https://docs.ftx.com/#make-nft-offer """
        return await self.post('/api/ndt/offer', data={'nftId': nftId, 'price': price})

    async def buy_nft(self, nftId: int, price: float):
        """ https://docs.ftx.com/#make-nft-offer """
        return await self.post('/api/ndt/buy', data={'nftId': nftId, 'price': price})

    async def create_auction(self, initialPrice: float, reservationPrice: float, duration: int):
        """ https://docs.ftx.com/#create-auction """
        return await self.post('/api/nft/auction', data={'initialPrice': initialPrice, 'reservationPrice': reservationPrice, 'duration': duration})

    async def edit_auction(self, reservationPrice: float):
        """ https://docs.ftx.com/#edit-auction """
        return await self.post('/api/nft/edit_auction', data={'reservationPrice': reservationPrice})

    async def cancel_auction(self, nftId: int, reservationPrice: float):
        """ https://docs.ftx.com/#cancel-auction """
        return await self.post('/api/nft/cancel_auction', data={'nftId': nftId, 'reservationPrice': reservationPrice})

    async def get_bids(self):
        """ https://docs.ftx.com/#get-bids """
        return await self.get('/api/nft/bids')

    async def place_bid(self, nftId: int, price: float):
        """ https://docs.ftx.com/#place-bid """
        return await self.post('/api/nft/bids', data={'nftId': nftId, 'price': price})

    async def get_nft_deposits(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-deposits """
        return await self.get('/api/nft/deposits', start_time=start_time, end_time=end_time)

    async def get_nft_withdrawals(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-withdrawals """
        return await self.get('/api/nft/withdrawals', start_time=start_time, end_time=end_time)

    async def get_nft_fills(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-nft-fills """
        return await self.get('/api/nft/fills', start_time=start_time, end_time=end_time)

    async def redeem_nft(self, nftId: int, address: str, notes: str):
        """ https://docs.ftx.com/#redeem-nft """
        return await self.post('/api/nft/redeem', data={'nftId': nftId, 'address': address, 'notes': notes})

    async def get_nft_gallery(self, gallery_id: int):
        """ https://docs.ftx.com/#get-nft-gallery """
        return await self.get(f'/api/nft/gallery/{gallery_id}')

    async def get_gallery_settings(self):
        """ https://docs.ftx.com/#get-gallery-settings """
        return await self.get(f'/api/nft/gallery_settings')

    async def edit_gallery_settings(self, public: bool = True):
        """ https://docs.ftx.com/#get-gallery-settings """
        assert isinstance(public, bool)
        return await self.get(f'/api/nft/gallery_settings', data={'public': public})
