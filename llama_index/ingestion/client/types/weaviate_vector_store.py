# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class WeaviateVectorStore(pydantic.BaseModel):
    """
    Weaviate vector store.

    In this vector store, embeddings and docs are stored within a
    Weaviate collection.

    During query time, the index uses Weaviate to query for the top
    k most similar nodes.

    Args:
        weaviate_client (weaviate.Client): WeaviateClient
            instance from `weaviate-client` package
        index_name (Optional[str]): name for Weaviate classes
    """

    stores_text: typing.Optional[bool]
    is_embedding_query: typing.Optional[bool]
    index_name: str
    url: typing.Optional[str]
    text_key: str
    auth_config: typing.Optional[typing.Dict[str, typing.Any]]
    client_kwargs: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
