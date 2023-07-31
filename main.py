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

    def read_parts(self, parts: list, parts_brand: str, parts_model: str) -> List:
        try:
            matching_parts = []
            for part in parts:
                if part.get_brand() == parts_brand and part.get_model() == parts_model:
                    matching_parts.append(part)
            return matching_parts
        except Exception as e:
            logging.exception(f"Error in read_parts: {e}")

    def delete_parts(self, parts: list, parts_brand: str, parts_model: str):
        try:
            for part in parts:
                if part.get_brand() == parts_brand and part.get_model() == parts_model:
                    parts.remove(part)
                    return True
            return False
        except Exception as e:
            logging.exception(f"Error in delete_parts: {e}")

    def update_price(self, parts: list, parts_brand: str, parts_model: str, part_price: float):
        try:
            for part in parts:
                if part.get_brand() == parts_brand and part.get_model() == parts_model:
                    part.set_price(part_price)
                    return True
            return False
        except Exception as e:
            logging.exception(f"Error in update_parts: {e}")

    def view_all_parts(self, parts) -> List[str]:
        try:
            result = []
            for part in parts:
                part_info = f"{part.get_brand()} {part.get_model()} - Price: {part.get_price()}€"
                result.append(part_info)
                print(part_info)
                print(result)
            return result
        except Exception as e:
            logging.exception(f"Error in view_all_parts: {e}")

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
