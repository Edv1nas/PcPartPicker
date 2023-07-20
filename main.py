import logging
from typing import List
from utilities.crud_operations import read_cpu, update_cpu, delete_cpu
from utilities.database import cpus_list, cpu_collers_list, motherboards_list, memories_list, storages_list, video_cards_list, cases_list, power_supplies_list
from utilities.pc_parts import CPU, CPUColler, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply

logging.basicConfig(level=logging.DEBUG, filename="data_flow.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PartPicker:
    def __init__(self, cpus: List[CPU]) -> None:
        self._cpus = cpus

    def get_processors_by_brand(self, brand: str) -> List[CPU]:
        try:
            logging.debug(f"Getting processors by brand: {brand}")
            processors_list = []
            for cpu in self._cpus:
                if cpu.get_brand() == brand:
                    processors_list.append(cpu)
            return processors_list
        except Exception as e:
            logging.error(f"Error in get_processors_by_brand: {str(e)}")
            return e

    def get_cpus_by_cores(self, core_count: int) -> List[CPU]:
        try:
            logging.debug(f"Getting CPUs by core count: {core_count}")
            processors_list = []
            for cpu in self._cpus:
                if cpu.get_core_count() == core_count:
                    processors_list.append(cpu)
            return processors_list
        except Exception as e:
            logging.error(f"Error in get_cpus_by_cores: {str(e)}")
            return e

    def get_cpus_by_price(self, price: float) -> List[CPU]:
        try:
            logging.debug(f"Getting CPUs by price: {price}")
            processors_list = []
            for cpu in self._cpus:
                if cpu.get_price() <= price:
                    processors_list.append(cpu)
            return processors_list
        except Exception as e:
            logging.error(f"Error in get_cpus_by_price: {str(e)}")
            return e

    # def read_cpu(self, brand: str, model: str):
    #     for cpu in self._cpus:
    #         if cpu.get_brand() == brand and cpu.get_model() == model:
    #             return cpu
    #     return None


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

print("Crud Operations: READ")
found_cpu = read_cpu(part_picker._cpus, "AMD", "Ryzen 9 5950X")
if found_cpu:
    print("Found CPU:", found_cpu._model)
else:
    print("CPU not found.")

print("\nCrud Operations: UPDATE")
update_price = update_cpu(part_picker._cpus, "AMD", "Ryzen 9 5950X", 110.99)
if update_price:
    print("CPU price updated successfully.")
else:
    print("CPU not found, update failed.")

print("\nCrud Operations: Check if price changed")
cpu = read_cpu(part_picker._cpus, "AMD", "Ryzen 9 5950X")
if cpu:
    print("Updated CPU Price:", cpu.price)
else:
    print("CPU not found.")

print("\nCrud Operations: DELETE")
delete = delete_cpu(part_picker._cpus, "AMD", "Ryzen 9 5950X")
if delete:
    print("CPU deleted successfully.")
else:
    print("CPU not found, delete failed.")

print("\nCrud Operations: Check deleted item.")
check_deleted = read_cpu(part_picker._cpus, "AMD", "Ryzen 9 5950X")
if check_deleted:
    print("Found CPU:", found_cpu._model)
else:
    print("CPU not found.")
