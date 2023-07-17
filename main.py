from typing import List
from utilities.database import cpus_list
from utilities.pc_parts import CPU


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


part_picker = PartPicker(cpus_list)
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
