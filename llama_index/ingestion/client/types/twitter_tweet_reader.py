# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.core.datetime_utils import serialize_datetime


class TwitterTweetReader(pydantic.BaseModel):
    """
    Twitter tweets reader.

    Read tweets of user twitter handle.

    Check 'https://developer.twitter.com/en/docs/twitter-api/        getting-started/getting-access-to-the-twitter-api'         on how to get access to twitter API.

    Args:
        bearer_token (str): bearer_token that you get from twitter API.
        num_tweets (Optional[int]): Number of tweets for each user twitter handle.            Default is 100 tweets.
    """

    is_remote: typing.Optional[bool]
    bearer_token: str
    num_tweets: typing.Optional[int]
    class_name: typing.Optional[str]

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
