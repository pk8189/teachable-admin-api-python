"""File Generated by Sideko (sideko.dev)"""

from teachable_public_api import AsyncClient, Client


def test_init_client():
    """Tests initializing sdk client with all authentication methods"""
    Client(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )


def test_init_async_client():
    """Tests initializing async sdk client with all authentication methods"""
    AsyncClient(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )


# test sync & async methods (keep comment for code generation)
