from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class QueryBuilder:

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def get_result(self):
        pass
