"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Webhook(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    event_trigger: str = pydantic.Field(alias="event_trigger")
    id: int = pydantic.Field(alias="id")
    url: str = pydantic.Field(alias="url")
    webhook_events_count: int = pydantic.Field(alias="webhook_events_count")
    workflow_state: str = pydantic.Field(alias="workflow_state")


class ListWebhooksResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    webhooks: typing.List[Webhook] = pydantic.Field(alias="webhooks")
