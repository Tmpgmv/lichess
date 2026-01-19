import berserk
from .const import API_TOKEN

class ClientManager:

    @staticmethod
    def get_client():
        session = berserk.TokenSession(API_TOKEN)
        client = berserk.Client(session=session)

        return client