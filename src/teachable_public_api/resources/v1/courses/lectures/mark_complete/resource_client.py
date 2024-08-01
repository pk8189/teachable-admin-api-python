"""File Generated by Sideko (sideko.dev)"""

from teachable_public_api.core import (
    default_request_options,
    SyncBaseClient,
    RequestOptions,
    to_encodable,
    AsyncBaseClient,
)
from teachable_public_api.types.v1.courses.lectures.mark_complete import params
import typing


class MarkCompleteClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.User,
        course_id: int,
        lecture_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mark a specific course lecture as complete.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerUser)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/v1/courses/{course_id}/lectures/{lecture_id}/mark_complete",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncMarkCompleteClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.User,
        course_id: int,
        lecture_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mark a specific course lecture as complete.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerUser)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/v1/courses/{course_id}/lectures/{lecture_id}/mark_complete",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)