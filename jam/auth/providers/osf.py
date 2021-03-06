import aiohttp

from jam import exceptions
from jam.auth.providers.base import BaseAuthProvider


class OSFAuthProvider(BaseAuthProvider):
    name = 'osf'
    type = 'user'

    async def _authenticate(self, data):
        resp = await aiohttp.request('GET', 'https://staging-accounts.osf.io/oauth2/profile', headers={
            'Authorization': 'Bearer {}'.format(data.get('access_token'))
        })

        if resp.status != 200:
            raise exceptions.Unauthorized()
        return 'user', 'osf', (await resp.json())['id']
