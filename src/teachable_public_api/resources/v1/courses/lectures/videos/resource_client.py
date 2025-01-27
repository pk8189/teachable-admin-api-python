"""File Generated by Sideko (sideko.dev)"""

from teachable_public_api.core import (
    RequestOptions,
    default_request_options,
    AsyncBaseClient,
    SyncBaseClient,
    QueryParams,
    encode_param,
)
import typing
from teachable_public_api.types.v1.courses.lectures.videos import models


class VideosClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        course_id: int,
        lecture_id: int,
        video_id: int,
        user_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetV1CoursesCourseIdLecturesLectureIdVideosVideoIdResponse:
        """
        Fetch a specific video information.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if user_id is not None:
            _query["user_id"] = encode_param(user_id, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/courses/{course_id}/lectures/{lecture_id}/videos/{video_id}",
            auth_names=["ApiKeyAuth"],
            query_params=_query,
            cast_to=models.GetV1CoursesCourseIdLecturesLectureIdVideosVideoIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncVideosClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        course_id: int,
        lecture_id: int,
        video_id: int,
        user_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetV1CoursesCourseIdLecturesLectureIdVideosVideoIdResponse:
        """
        Fetch a specific video information.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if user_id is not None:
            _query["user_id"] = encode_param(user_id, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/courses/{course_id}/lectures/{lecture_id}/videos/{video_id}",
            auth_names=["ApiKeyAuth"],
            query_params=_query,
            cast_to=models.GetV1CoursesCourseIdLecturesLectureIdVideosVideoIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
