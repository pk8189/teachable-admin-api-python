"""File Generated by Sideko (sideko.dev)"""

import pytest
from teachable_public_api import AsyncClient, Client
from teachable_public_api.types.v1.users import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_create_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = client.v1.users.create(
        data={
            "email_field": "string",
            "name": "string",
            "password": "string",
            "src": "string",
        }
    )
    adapter = TypeAdapter(models.UserResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = await client.v1.users.create(
        data={
            "email_field": "string",
            "name": "string",
            "password": "string",
            "src": "string",
        }
    )
    adapter = TypeAdapter(models.UserResponse)
    adapter.validate_python(response)


def test_patch_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = client.v1.users.patch(
        user_id=123, data={"name": "string", "src": "string"}
    )
    adapter = TypeAdapter(models.UserResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_patch_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = await client.v1.users.patch(
        user_id=123, data={"name": "string", "src": "string"}
    )
    adapter = TypeAdapter(models.UserResponse)
    adapter.validate_python(response)


def test_get_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = client.v1.users.get(user_id=123)
    adapter = TypeAdapter(models.UserResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = await client.v1.users.get(user_id=123)
    adapter = TypeAdapter(models.UserResponse)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = client.v1.users.list(email_query="string", page=123, per=123)
    adapter = TypeAdapter(models.ListUsersResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = await client.v1.users.list(email_query="string", page=123, per=123)
    adapter = TypeAdapter(models.ListUsersResponse)
    adapter.validate_python(response)