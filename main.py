from typing import List


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


class PartPicker:
    def __init__(self, cpus: List[CPU]) -> None:
        self._cpus = cpus

    def get_processors_by_brand(self, brand: str) -> List[CPU]:
        processors_list = []
        for cpu in self._cpus:
            if cpu.get_brand() == brand:
                processors_list.append(cpu)
        return processors_list

    def get_cpus_by_cores(self, core_count: int) -> List[CPU]:
        processors_list = []
        for cpu in self._cpus:
            if cpu.get_core_count() == core_count:
                processors_list.append(cpu)
        return processors_list

    def get_cpus_by_price(self, price: float) -> List[CPU]:
        processors_list = []
        for cpu in self._cpus:
            if cpu.get_price() <= price:
                processors_list.append(cpu)
        return processors_list


cpus = [
    CPU("Intel", "Core i9-11900K", 399, 8, 16, 3.5, 5.3),
    CPU("AMD", "Ryzen 9 5950X", 299, 16, 32, 3.4, 4.9),
    CPU("Intel", "Core i7-11700K", 239, 8, 16, 3.6, 5.0),
    CPU("AMD", "Ryzen 7 5800X", 200, 8, 16, 3.8, 4.7),
    CPU("Intel", "Core i5-11600K", 209, 6, 12, 3.9, 4.9),
]


part_picker = PartPicker(cpus)
print("\nIntel CPUs\n")
intel_processors = part_picker.get_processors_by_brand("Intel")
for cpu in intel_processors:
    print(f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€")

print("\nAMD CPUs\n")
amd_processors = part_picker.get_processors_by_brand("AMD")
for cpu in amd_processors:
    print(f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€")

print("\nCPUs by core count\n")
cpus_with_cores = part_picker.get_cpus_by_cores(8)
for cpu in cpus_with_cores:
    print(f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€ - Cores: {cpu.get_core_count()}")

print("\nCPUs by price[lower or equal]\n")
cpus_by_price = part_picker.get_cpus_by_price(250)
for cpu in cpus_by_price:
    print(f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€")
