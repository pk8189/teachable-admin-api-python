"""File Generated by Sideko (sideko.dev)"""

from teachable_public_api.core import (
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    encode_param,
    AsyncBaseClient,
    default_request_options,
)
import typing
from teachable_public_api.types.v1.courses.progress import models


class ProgressClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        course_id: int,
        user_id: int,
        page: typing.Optional[int] = None,
        per: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CourseProgressesResponse:
        """
        Fetch a specific user's course progress.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["user_id"] = encode_param(user_id, False)
        if page is not None:
            _query["page"] = encode_param(page, False)
        if per is not None:
            _query["per"] = encode_param(per, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/courses/{course_id}/progress",
            auth_names=["ApiKeyAuth"],
            query_params=_query,
            cast_to=models.CourseProgressesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncProgressClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        course_id: int,
        user_id: int,
        page: typing.Optional[int] = None,
        per: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CourseProgressesResponse:
        """
        Fetch a specific user's course progress.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["user_id"] = encode_param(user_id, False)
        if page is not None:
            _query["page"] = encode_param(page, False)
        if per is not None:
            _query["per"] = encode_param(per, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/courses/{course_id}/progress",
            auth_names=["ApiKeyAuth"],
            query_params=_query,
            cast_to=models.CourseProgressesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
