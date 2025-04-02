import pytest
from typing import AsyncIterator, Any
from src.core.processor import Processor
import asyncio

class TestProcessor(Processor):
    def __init__(self, name: str, transform_func):
        super().__init__(name)
        self.transform_func = transform_func
    
    async def process(self, data: AsyncIterator[Any]) -> AsyncIterator[Any]:
        async for item in data:
            yield self.transform_func(item)

@pytest.mark.asyncio
async def test_processor_creation():
    """Тест создания процессора"""
    processor = TestProcessor("test_processor", lambda x: x * 2)
    assert processor.name == "test_processor"

@pytest.mark.asyncio
async def test_processor_transformation():
    """Тест трансформации данных процессором"""
    processor = TestProcessor("test_processor", lambda x: x * 2)
    async def data_generator():
        yield 1
        yield 2
        yield 3
    
    result = []
    async for item in processor.process(data_generator()):
        result.append(item)
    assert result == [2, 4, 6]

@pytest.mark.asyncio
async def test_processor_empty_input():
    """Тест процессора с пустым входом"""
    processor = TestProcessor("test_processor", lambda x: x * 2)
    async def empty_generator():
        await asyncio.sleep(0)  # Создаем пустой асинхронный итератор
    
    result = []
    async for item in processor.process(empty_generator()):
        result.append(item)
    assert result == [] 