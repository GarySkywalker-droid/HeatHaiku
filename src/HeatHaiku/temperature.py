import psutil


def get_cpu_temperature() -> float | None:
    """
    returns float | None, temperature of the CPU in celsius
    """
    if not hasattr(psutil, "sensors_temperatures"):
        return None
    temps = psutil.sensors_temperatures()
    if not temps:
        return None

    avg_temps = 0
    valid_cores = 0
    for cores in temps["coretemp"]:
        if cores.current is not None:
            avg_temps += cores.current
            valid_cores += 1
    if valid_cores == 0:
        return None
    return avg_temps / valid_cores
