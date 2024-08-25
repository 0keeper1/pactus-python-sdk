"""Connection."""

from __future__ import annotations

import grp
from types import NoneType
from typing import Self

import grpc
from grpc import Channel, insecure_channel, secure_channel

from .exceptions import ConnectionExecption

__all__ = ["PactusConnect"]


class PactusConnect:
    def __init__(self, url: str, key: str | NoneType = None) -> None:
        self._url = url
        self._private_key = key
        self._channel: Channel = None

    def connect(self, secure: bool = False, credentials=None) -> Self:
        if not secure:
            self._channel = insecure_channel(self._url)
        elif secure and credentials:
            self._channel = secure_channel(self._url, credentials=credentials)
        else:
            raise ConnectionExecption(
                "credentials is required for secure connection."
            )

    async def async_connect(
        self,
        secure: bool = False,
        credentials=None,
    ) -> Self:
        if not secure:
            self._channel = await grpc.aio.insecure_channel()
        elif secure and credentials:
            self._channel = await grpc.aio.secure_channel()
        else:
            raise ConnectionExecption(
                "credentials is required for secure connection."
            )
