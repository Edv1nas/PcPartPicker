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

    def set_price(self, new_price):
        self._price = new_price


class CPU(PCParts):
    def __init__(self, brand: str, model: str, price: float, core_count: int, threads: int, base_clock: float, max_boost_clock: float):
        super().__init__(brand, model, price)
        self.core_count = core_count
        self.threads = threads
        self.base_clock = base_clock
        self.max_boost_clock = max_boost_clock

    def get_core_count(self) -> int:
        return self.core_count

    def get_threads(self) -> int:
        return self.threads

    def get_base_clock(self) -> float:
        return self.base_clock

    def get_max_boost_clock(self) -> float:
        return self.max_boost_clock


class CPUColler(PCParts):
    def __init__(self, brand: str, model: str, price: float, fan_rpm: int, noise_level: float):
        super().__init__(brand, model, price)
        self.fan_rpm = fan_rpm
        self.noise_level = noise_level

    def get_fan_rpm(self):
        return self.fan_rpm

    def get_noise_level(self):
        return self.noise_level


class Motherboard(PCParts):
    def __init__(self, brand: str, model: str, price: float, socket: str, form_factor: str, memory_max: int):
        super().__init__(brand, model, price)
        self.socket = socket
        self.form_factor = form_factor
        self.memory_max = memory_max

    def get_socket(self):
        return self.socket

    def get_form_factor(self):
        return self.form_factor

    def get_memory_max(self):
        return self.memory_max


class Memory(PCParts):
    def __init__(self, brand: str, model: str, price: float, memory_quantity: int, memory_type: str, memory_speed: int):
        super().__init__(brand, model, price)
        self.memory_quantity = memory_quantity
        self.memory_type = memory_type
        self.memory_speed = memory_speed

    def get_memory_quantity(self):
        return self.memory_quantity

    def get_memory_type(self):
        return self.memory_type

    def get_memory_speed(self):
        return self.memory_speed


class Storage(PCParts):
    def __init__(self, brand: str, model: str, price: float, capacity: str, type: str, interface: str):
        super().__init__(brand, model, price)
        self.capacity = capacity
        self.type = type
        self.interface = interface

    def get_capacity(self):
        return self.capacity

    def get_type(self):
        return self.type

    def get_interface(self):
        return self.interface


class VideoCard(PCParts):
    def __init__(self, brand: str, model: str, price: float, chipset: str, memory_size: int, core_clock: int, boost_clock: int):
        super().__init__(brand, model, price)
        self.chipset = chipset
        self.memory_size = memory_size
        self.core_clock = core_clock
        self.boost_clock = boost_clock

    def get_chipset(self):
        return self.chipset

    def get_memory_size(self):
        return self.memory_size

    def get_core_clock(self):
        return self.core_clock

    def get_boost_clock(self):
        return self.boost_clock


class Case(PCParts):
    def __init__(self, brand: str, model: str, price: float, case_type: str, case_color: str, side_panel: str):
        super().__init__(brand, model, price)
        self.case_type = case_type
        self.case_color = case_color
        self.side_panel = side_panel

    def get_case_type(self):
        return self.case_type

    def get_case_color(self):
        return self.case_color

    def get_side_panel(self):
        return self.side_panel


class PowerSupply(PCParts):
    def __init__(self, brand: str, model: str, price: float, power_supply_type: str, efficiency_rating: str, wattage: int, modular: str):
        super().__init__(brand, model, price)
        self.power_supply_type = power_supply_type
        self.efficiency_rating = efficiency_rating
        self.wattage = wattage
        self.modular = modular

    def get_power_supply_type(self):
        return self.power_supply_type

    def get_efficiency_rating(self):
        return self.efficiency_rating

    def get_wattage(self):
        return self.wattage

    def get_modular(self):
        return self.modular
