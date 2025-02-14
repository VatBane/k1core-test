import requests

from currency.dto.block import BlockDetailsDTO, BlockDTO
from currency.exceptions import ServiceConnectionError, ResourceNotFoundError


class BlockChairAPIServicer:
    def get_last_block(self, currency: str) -> BlockDTO:
        url = f"https://api.blockchair.com/{currency.lower()}/stats"
        response = requests.get(url, timeout=15)

        print(response.status_code)
        print(response.json())
        if response.status_code >= 500:
            raise ServiceConnectionError('BlockChair service not available!')
        elif response.status_code == 404:
            raise ResourceNotFoundError('Information about given currency not found!')
        elif response.status_code != 200:
            raise Exception('Error occurred while trying to access BlockChair!')

        return BlockDTO(**response.json()['data'])

    def get_block_details(self, currency: str, block_hash: str | int) -> BlockDetailsDTO:
        url = f'https://api.blockchair.com/{currency.lower()}/dashboards/block/{block_hash}'
        response = requests.get(url, timeout=15)

        if response.status_code >= 500:
            raise ServiceConnectionError('BlockChair service not available!')
        elif response.status_code == 404:
            raise ResourceNotFoundError('Information about given currency or block not found!')
        elif response.status_code != 200:
            raise Exception('Error occurred while trying to access BlockChair!')

        data = response.json()
        return BlockDetailsDTO(**data['data'][str(block_hash)]['block'])
