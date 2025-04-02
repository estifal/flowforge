import pytest
from typing import AsyncIterator, Any
from src.core.sink import Sink

class TestSink(Sink):
    def __init__(self, name: str):
        super().__init__(name)
        self.connected = False
        self.received_data = []
    
    async def connect(self) -> None:
        self.connected = True
    
    async def disconnect(self) -> None:
        self.connected = False
    
    async def write(self, data: AsyncIterator[Any]) -> None:
        async for item in data:
            self.received_data.append(item)

@pytest.mark.asyncio
async def test_sink_creation():
    """Тест создания точки вывода"""
    sink = TestSink("test_sink")
    assert sink.name == "test_sink"
    assert not sink.connected
    assert sink.received_data == []

@pytest.mark.asyncio
async def test_sink_connection():
    """Тест подключения и отключения точки вывода"""
    sink = TestSink("test_sink")
    assert not sink.connected
    
    await sink.connect()
    assert sink.connected
    
    await sink.disconnect()
    assert not sink.connected

@pytest.mark.asyncio
async def test_sink_data_writing():
    """Тест записи данных в точку вывода"""
    sink = TestSink("test_sink")
    async def data_generator():
        yield 1
        yield 2
        yield 3
    
    await sink.write(data_generator())
    assert sink.received_data == [1, 2, 3]

@pytest.mark.asyncio
async def test_sink_empty_input():
    """Тест записи пустых данных"""
    sink = TestSink("test_sink")
    async def empty_generator():
        return
    
    await sink.write(empty_generator())
    assert sink.received_data == [] 