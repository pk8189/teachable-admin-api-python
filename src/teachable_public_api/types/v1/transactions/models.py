"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PaginationMeta(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    from_field: int = pydantic.Field(alias="from")
    number_of_pages: int = pydantic.Field(alias="number_of_pages")
    page: int = pydantic.Field(alias="page")
    per_page: int = pydantic.Field(alias="per_page")
    to: int = pydantic.Field(alias="to")
    total: int = pydantic.Field(alias="total")


class TransactionSummary(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    affiliate_fees: int = pydantic.Field(alias="affiliate_fees")
    affiliate_id: typing.Optional[int] = pydantic.Field(
        alias="affiliate_id", default=None
    )
    amount_refunded: int = pydantic.Field(alias="amount_refunded")
    author_fees: int = pydantic.Field(alias="author_fees")
    author_id: typing.Optional[int] = pydantic.Field(alias="author_id", default=None)
    charge: int = pydantic.Field(alias="charge")
    chargeback_fee: typing.Optional[int] = pydantic.Field(
        alias="chargeback_fee", default=None
    )
    coupon_id: typing.Optional[int] = pydantic.Field(alias="coupon_id", default=None)
    created_at: str = pydantic.Field(alias="created_at")
    currency: str = pydantic.Field(alias="currency")
    final_price: int = pydantic.Field(alias="final_price")
    has_chargeback: typing.Optional[bool] = pydantic.Field(
        alias="has_chargeback", default=None
    )
    id: int = pydantic.Field(alias="id")
    pricing_plan_id: int = pydantic.Field(alias="pricing_plan_id")
    purchased_at: str = pydantic.Field(alias="purchased_at")
    refunded_at: typing.Optional[str] = pydantic.Field(
        alias="refunded_at", default=None
    )
    revenue: int = pydantic.Field(alias="revenue")
    sale_id: int = pydantic.Field(alias="sale_id")
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    tax_charge: int = pydantic.Field(alias="tax_charge")
    user_id: int = pydantic.Field(alias="user_id")


class ListTransactionsResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    meta: PaginationMeta = pydantic.Field(alias="meta")
    transactions: typing.List[TransactionSummary] = pydantic.Field(alias="transactions")
