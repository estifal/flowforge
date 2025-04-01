from abc import ABC, abstractmethod
from typing import Any, AsyncIterator

class Source(ABC):
    """Базовый класс для источников данных"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    async def connect(self) -> None:
        """Установка соединения с источником данных"""
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """Закрытие соединения с источником данных"""
        pass
    
    @abstractmethod
    async def read(self) -> AsyncIterator[Any]:
        """Чтение данных из источника"""
        pass
