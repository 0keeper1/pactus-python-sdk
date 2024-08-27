"""Connection."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from grpc import Channel, insecure_channel, secure_channel

from .exceptions import ConnectionExecption

if TYPE_CHECKING:
    from types import NoneType

__all__ = ["PactusConnect"]


class PactusConnect:
    def __init__(self, url: str, key: str | NoneType = None) -> None:
        self._url = url
        self._private_key = key
        self._channel: Channel | NoneType = None

    def connect(self, secure: bool = False, credentials=None) -> Self:
        if not secure:
            self._channel = insecure_channel(self._url)
            return self
        elif secure and credentials:
            self._channel = secure_channel(self._url, credentials=credentials)
            return self
        else:
            raise ConnectionExecption(
                "credentials is required for secure connection."
            )
