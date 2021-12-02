from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceAbstract(ABC):

    def __init__(self) -> None:
        super().__init__()

    @property
    def __endpoint(self) -> str:
        raise NotImplementedError

    @property
    def __client(self) -> Client:
        raise NotImplementedError

    def get_resource_endpoint(self):
        return self.__endpoint
