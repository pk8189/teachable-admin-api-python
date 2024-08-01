"""File Generated by Sideko (sideko.dev)"""

import pytest
from teachable_public_api import AsyncClient, Client
from teachable_public_api.types.v1.courses.lectures.quizzes.responses import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = client.v1.courses.lectures.quizzes.responses.list(
        course_id=123, lecture_id=123, quiz_id=123
    )
    adapter = TypeAdapter(models.QuizResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(
        api_key="API_KEY",
        base_url="https://api.sideko.dev/v1/api_project/a067d36b-0caa-4dbc-8cb5-2f889a41de78/version/bd7f72fe-0881-4488-810b-354d1662c897/mock",
    )
    response = await client.v1.courses.lectures.quizzes.responses.list(
        course_id=123, lecture_id=123, quiz_id=123
    )
    adapter = TypeAdapter(models.QuizResponse)
    adapter.validate_python(response)
