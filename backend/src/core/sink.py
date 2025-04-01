from abc import ABC, abstractmethod
from typing import Any, AsyncIterator

class Sink(ABC):
    """Базовый класс для точек вывода данных"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    async def connect(self) -> None:
        """Установка соединения с точкой вывода"""
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """Закрытие соединения с точкой вывода"""
        pass
    
    @abstractmethod
    async def write(self, data: AsyncIterator[Any]) -> None:
        """Запись данных в точку вывода"""
        pass
