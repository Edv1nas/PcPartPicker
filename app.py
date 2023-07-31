from main import PartPicker


if __name__ == '__main__':

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
