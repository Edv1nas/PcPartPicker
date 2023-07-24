import logging
from typing import List
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

    def read_parts(self, parts_list, parts_brand: str, parts_model: str):
        for parts in parts_list:
            if parts._brand == parts_brand and parts._model == parts_model:
                return parts
        return None

    def delete_parts(self, parts_list, parts_brand: str, parts_model: str):
        for part in parts_list:
            if part.get_brand() == parts_brand and part.get_model() == parts_model:
                parts_list.remove(part)
                return True
        return False

    def update_parts(self, parts_list, parts_brand: str, parts_model: str, part_price: float):
        for part in parts_list:
            if part.get_brand() == parts_brand and part.get_model() == parts_model:
                part.set_price(part_price)
                return True
        return False


def main():
    part_picker = PartPicker(cpus_list)

    while True:
        print("Choose an operation:")
        print("1. View all CPUs")
        print("2. Get processors by brand")
        print("3. Get CPUs by core count")
        print("4. Get CPUs by price [=>]")
        print("5. Update CPU price")
        print("6. Delete CPU by model")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nAll CPUs\n")
            for cpu in part_picker._cpus:
                print(
                    f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€")

        elif choice == "2":
            brand = input("Enter the brand: ").capitalize()
            print(brand)
            processors = part_picker.get_processors_by_brand(brand)
            if not processors:
                print(f"No CPUs found for brand {brand}.")
            else:
                print(f"\n{brand} CPUs\n")
                for cpu in processors:
                    print(
                        f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€")

        elif choice == "3":
            try:
                core_count = int(input("Enter the core count: "))
                cpus_with_cores = part_picker.get_cpus_by_cores(core_count)
                print("\nCPUs by core count\n")
                for cpu in cpus_with_cores:
                    print(
                        f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€ - Cores: {cpu.get_core_count()}")
            except ValueError:
                print("Invalid input. Core count must be an integer.")

        elif choice == "4":
            try:
                price = float(input("Enter the maximum price: "))
                cpus_by_price = part_picker.get_cpus_by_price(price)
                print("\nCPUs by price [lower or equal]\n")
                for cpu in cpus_by_price:
                    print(
                        f"{cpu.get_brand()} {cpu.get_model()} - Price: {cpu.get_price()}€")
            except ValueError:
                print("Invalid input. Price must be a number.")

        elif choice == "5":
            brand = input("Enter the brand: ").capitalize()
            model = input("Enter the model: ").capitalize()
            try:
                new_price = float(input("Enter the new price: "))
                if part_picker.update_parts(part_picker._cpus, brand, model, new_price):
                    print("CPU price updated successfully.")
                else:
                    print("CPU not found, update failed.")
            except ValueError:
                print("Invalid input. Price must be a number.")

        elif choice == "6":
            brand = input("Enter the brand: ").capitalize()
            model = input("Enter the model: ").capitalize()
            if part_picker.delete_parts(part_picker._cpus, brand, model):
                print("CPU deleted successfully.")
            else:
                print("CPU not found, delete failed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
