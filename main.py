import logging
from typing import List
from utilities.database import parts_dict


logging.basicConfig(level=logging.DEBUG, filename="data_flow.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PartPicker:

    def get_parts_by_brand(self, parts, brand: str) -> List:
        try:
            logging.debug(f"Getting processors by brand: {brand}")
            parts_list = []
            for part in parts:
                if part.get_brand() == brand:
                    parts_list.append(part)
            return parts_list
        except Exception as e:
            logging.error(f"Error in get_processors_by_brand: {str(e)}")

    def get_parts_by_price(self, parts, price: float) -> List:
        try:
            logging.debug(f"Getting CPUs by price: {price}")
            parts_list = []
            for part in parts:
                if part.get_price() <= price:
                    parts_list.append(part)
            return parts_list
        except Exception as e:
            logging.error(f"Error in get_cpus_by_price: {str(e)}")

    def read_parts(self, parts, parts_brand: str, parts_model: str):
        for part in parts:
            if part.get_brand() == parts_brand and part.get_model() == parts_model:
                return part
        return None

    def delete_parts(self, parts, parts_brand: str, parts_model: str):
        for part in parts:
            if part.get_brand() == parts_brand and part.get_model() == parts_model:
                parts.remove(part)
                return True
        return False

    def update_parts(self, parts, parts_brand: str, parts_model: str, part_price: float):
        for part in parts:
            if part.get_brand() == parts_brand and part.get_model() == parts_model:
                part.set_price(part_price)
                return True
        return False

    def view_all_parts(self, parts) -> List:
        for part in parts:
            print(
                f"{part.get_brand()} {part.get_model()} - Price: {part.get_price()}€")

    def get_parts_by_specification(self, parts: List, specification_name: str, specification_value) -> List:
        try:
            logging.debug(
                f"Filtering parts by specification: {specification_name} = {specification_value}")
            return [part for part in parts if getattr(part, specification_name) == specification_value]
        except Exception as e:
            logging.error(f"Error in filter_parts_by_specification: {str(e)}")

    def get_part_list(self, part_type):
        parts_list = parts_dict.get(part_type, [])
        if not parts_list:
            print(f"No parts found for part type: {part_type}")
        else:
            return parts_list


def main():
    part_picker = PartPicker()

    while True:
        print("\nChoose an operation:")
        print("1. View all parts by type")
        print("2. Get part by brand")
        print("3. Get part by part specification")
        print("4. Get parts by price [=>]")
        print("5. Update part price")
        print("6. Delete part by model")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            part_type = input("Enter part type: ").lower()
            parts_list = part_picker.get_part_list(part_type)
            if parts_list:
                print(f"\nAll {part_type.upper()}\n")
                part_picker.view_all_parts(parts_list)
            else:
                print(f"No parts found for part type: {part_type}")

        elif choice == "2":
            part_type = input("Enter part type: ").lower()
            brand = input("Enter the brand: ").capitalize()
            parts_list = part_picker.get_part_list(part_type)
            if parts_list:
                matching_parts = part_picker.get_parts_by_brand(
                    parts_list, brand)
                if not matching_parts:
                    print(f"No parts found for brand {brand}.")
                else:
                    print(f"\n{brand} {part_type.upper()}\n")
                    part_picker.view_all_parts(matching_parts)
            else:
                print(f"No parts found for part type: {part_type}")

        elif choice == "3":
            part_type = input("Enter part type: ").lower()
            spec_name = input("Enter specification for part: ")
            spec_value = int(input("Enter the core count: "))
            parts_list = part_picker.get_part_list(part_type)
            if parts_list:
                matching_parts = part_picker.get_parts_by_specification(
                    parts_list, spec_name, spec_value)
                if not matching_parts:
                    print(
                        f"No parts found for given specifications {spec_name}:{spec_value}.")
                else:
                    print(
                        f"\n{part_type.upper()}: {spec_name}-{spec_value} \n")
                    part_picker.view_all_parts(matching_parts)
            else:
                print(f"No parts found for part type: {part_type}")

        elif choice == "4":
            try:
                part_type = input("Enter part type: ").lower()
                price = float(input("Enter the maximum price: "))
                parts_list = part_picker.get_part_list(part_type)
                if parts_list:
                    parts_by_price = part_picker.get_parts_by_price(
                        parts_list, price)
                    if not parts_by_price:
                        print(
                            f"No parts found for given price: {price}.")
                    else:
                        print(
                            f"\n{part_type.upper()}: >={price} \n")
                        part_picker.view_all_parts(parts_by_price)
            except ValueError:
                print("Invalid input. Price must be a number.")

        elif choice == "5":
            part_type = input("Enter part type: ").lower()
            brand = input("Enter the brand: ").capitalize()
            model = input("Enter the model: ").capitalize()
            try:
                new_price = float(input("Enter the new price: "))
                parts_list = part_picker.get_part_list(part_type)
                if parts_list:
                    part_to_update = part_picker.update_parts(
                        parts_list, brand, model, new_price)
                    if not part_to_update:
                        print("CPU not found, update failed.")
                    else:
                        print("CPU price updated successfully.")
            except ValueError:
                print("Invalid input. Price must be a number.")

        elif choice == "6":
            part_type = input("Enter part type: ").lower()
            brand = input("Enter the brand: ").capitalize()
            model = input("Enter the model: ").capitalize()
            parts_list = part_picker.get_part_list(part_type)
            if parts_list:
                parts_to_delete = part_picker.delete_parts(
                    parts_list, brand, model)
                if not parts_to_delete:
                    print("Part not found, delete failed.")
                else:
                    print("CPU deleted successfully.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
