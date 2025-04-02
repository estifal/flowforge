from src.core.source import Source
from src.core.processor import Processor
from src.core.sink import Sink

class Pipeline:
    def __init__(self, name: str):
        self.name = name
        # Добавьте необходимые атрибуты для хранения компонентов
    
    def add_source(self, source: Source) -> None:
        # Реализуйте метод
        pass
    
    def add_processor(self, processor: Processor) -> None:
        # Реализуйте метод
        pass
    
    def add_sink(self, sink: Sink) -> None:
        # Реализуйте метод
        pass
    
    async def run(self) -> None:
        # Реализуйте метод
        pass
