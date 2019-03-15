from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceAbstract(ABC):

    def __init__(self) -> None:
        super().__init__()

    @property
    def _endpoint(self) -> str:
        raise NotImplementedError

    @property
    def _client(self) -> Client:
        raise NotImplementedError
