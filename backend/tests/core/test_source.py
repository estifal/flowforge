import pytest
from typing import AsyncIterator, Any
from src.core.source import Source

class TestSource(Source):
    def __init__(self, name: str, data: list):
        super().__init__(name)
        self.data = data
        self.connected = False
    
    async def connect(self) -> None:
        self.connected = True
    
    async def disconnect(self) -> None:
        self.connected = False
    
    async def read(self) -> AsyncIterator[Any]:
        for item in self.data:
            yield item

@pytest.mark.asyncio
async def test_source_creation():
    """Тест создания источника"""
    source = TestSource("test_source", [1, 2, 3])
    assert source.name == "test_source"
    assert not source.connected

@pytest.mark.asyncio
async def test_source_connection():
    """Тест подключения и отключения источника"""
    source = TestSource("test_source", [1, 2, 3])
    assert not source.connected
    
    await source.connect()
    assert source.connected
    
    await source.disconnect()
    assert not source.connected

@pytest.mark.asyncio
async def test_source_data_reading():
    """Тест чтения данных из источника"""
    source = TestSource("test_source", [1, 2, 3])
    data = []
    async for item in source.read():
        data.append(item)
    assert data == [1, 2, 3] 