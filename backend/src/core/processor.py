from abc import ABC, abstractmethod
from typing import Any, AsyncIterator

class Processor(ABC):
    """Базовый класс для обработчиков данных"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    async def process(self, data: AsyncIterator[Any]) -> AsyncIterator[Any]:
        """Обработка потока данных"""
        pass
