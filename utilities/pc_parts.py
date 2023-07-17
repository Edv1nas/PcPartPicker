class PCParts:
    def __init__(self, brand: str, model: str, price: float):
        self._brand = brand
        self._model = model
        self._price = price

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def get_price(self) -> float:
        return self._price


class CPU(PCParts):
    def __init__(self, brand: str, model: str, price: float, core_count: int, threads: int, base_clock: float, max_boost_clock: float):
        super().__init__(brand, model, price)
        self._core_count = core_count
        self._threads = threads
        self._base_clock = base_clock
        self._max_boost_clock = max_boost_clock

    def get_core_count(self) -> int:
        return self._core_count

    def get_threads(self) -> int:
        return self._threads

    def get_base_clock(self) -> float:
        return self._base_clock

    def get_max_boost_clock(self) -> float:
        return self._max_boost_clock


class CPUColler(PCParts):
    pass


class Motherboard(PCParts):
    pass


class Memory(PCParts):
    pass


class Storage(PCParts):
    pass


class VideoCard(PCParts):
    pass


class Case(PCParts):
    pass


class PowerSupply(PCParts):
    pass
