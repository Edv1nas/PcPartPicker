def read_cpu(cpu_list, brand: str, model: str):
    for cpu in cpu_list:
        if cpu._brand == brand and cpu._model == model:
            return cpu
    return None


def update_cpu(cpu_list, brand: str, model: str, price: float):
    cpu = read_cpu(cpu_list, brand, model)
    if cpu:
        cpu.price = price
        return True
    return False


def delete_cpu(cpu_list, brand: str, model: str):
    cpu = read_cpu(cpu_list, brand, model)
    if cpu:
        cpu_list.remove(cpu)
        return True
    return False
