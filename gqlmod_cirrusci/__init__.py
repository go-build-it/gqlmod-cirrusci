"""
Provider for Cirrus CI's GraphQL API.
"""
from gqlmod.helpers.httpx import HttpxProvider


class CirrusCiProvider(HttpxProvider):
    endpoint = 'https://api.cirrus-ci.com/graphql'

    def __init__(self, token=None):
        self.token = token

    def build_request(self, query, variables):
        req = super().build_request(query, variables)
        if self.token:
            req.headers['Authorization'] = f"Bearer {self.token}"
        return req
