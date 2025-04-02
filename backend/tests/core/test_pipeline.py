import pytest
from src.core.pipeline import Pipeline
from .test_source import TestSource
from .test_processor import TestProcessor
from .test_sink import TestSink

@pytest.mark.asyncio
async def test_pipeline_creation():
    """Тест создания пайплайна"""
    pipeline = Pipeline("test_pipeline")
    assert pipeline.name == "test_pipeline"

@pytest.mark.asyncio
async def test_pipeline_add_components():
    """Тест добавления компонентов в пайплайн"""
    pipeline = Pipeline("test_pipeline")
    
    source = TestSource("test_source", [1, 2, 3])
    processor = TestProcessor("test_processor", lambda x: x * 2)
    sink = TestSink("test_sink")
    
    pipeline.add_source(source)
    pipeline.add_processor(processor)
    pipeline.add_sink(sink)
    
    # Проверяем, что компоненты добавлены
    assert len(pipeline.sources) == 1
    assert len(pipeline.processors) == 1
    assert len(pipeline.sinks) == 1

@pytest.mark.asyncio
async def test_pipeline_execution():
    """Тест выполнения пайплайна"""
    pipeline = Pipeline("test_pipeline")
    
    # Создаем тестовые данные
    source_data = [1, 2, 3]
    source = TestSource("test_source", source_data)
    processor = TestProcessor("test_processor", lambda x: x * 2)
    sink = TestSink("test_sink")
    
    pipeline.add_source(source)
    pipeline.add_processor(processor)
    pipeline.add_sink(sink)
    
    # Запускаем пайплайн
    await pipeline.run()
    
    # Проверяем результаты
    assert sink.received_data == [2, 4, 6]  # Данные должны быть умножены на 2

@pytest.mark.asyncio
async def test_pipeline_error_handling():
    """Тест обработки ошибок в пайплайне"""
    pipeline = Pipeline("test_pipeline")
    
    # Создаем источник, который вызывает ошибку
    class ErrorSource(TestSource):
        async def read(self):
            raise ValueError("Test error")
    
    source = ErrorSource("error_source", [])
    sink = TestSink("test_sink")
    
    pipeline.add_source(source)
    pipeline.add_sink(sink)
    
    # Проверяем, что ошибка обрабатывается корректно
    with pytest.raises(ValueError):
        await pipeline.run()
    
    # Проверяем, что соединения закрыты
    assert not source.connected
    assert not sink.connected

@pytest.mark.asyncio
async def test_pipeline_multiple_processors():
    """Тест пайплайна с несколькими процессорами"""
    pipeline = Pipeline("test_pipeline")
    
    source = TestSource("test_source", [1, 2, 3])
    processor1 = TestProcessor("processor1", lambda x: x * 2)
    processor2 = TestProcessor("processor2", lambda x: x + 1)
    sink = TestSink("test_sink")
    
    pipeline.add_source(source)
    pipeline.add_processor(processor1)
    pipeline.add_processor(processor2)
    pipeline.add_sink(sink)
    
    await pipeline.run()
    
    # Проверяем результаты последовательной обработки
    # 1 -> 2 -> 3
    # 2 -> 4 -> 5
    # 3 -> 6 -> 7
    assert sink.received_data == [3, 5, 7] 