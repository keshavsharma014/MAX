import platform
from pprint import pprint
import psutil


def get_os_info():
    """Return basic operating system information."""
    print("Getting OS information...")
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine()
    }

def get_cpu_count():
    """Return the number of physical CPU cores."""
    print("Getting physical CPU count...")
    return psutil.cpu_count(logical=False)  # Physical cores

def get_logical_cpu_count():
    """Return the number of logical CPU cores."""
    print("Getting logical CPU count...")
    return psutil.cpu_count(logical=True)  # Logical cores


def get_cpu_usage():
    """Return current CPU usage percentage."""
    print("Getting cpu usage information...")
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Return current RAM usage information."""
    print("Getting memory usage...")
    memory = psutil.virtual_memory()

    return {
        "total_gb": round(memory.total / (1024 ** 3), 2),
        "used_gb": round(memory.used / (1024 ** 3), 2),
        "available_gb": round(memory.available / (1024 ** 3), 2),
        "usage_percent": memory.percent
    }


def get_disk_usage():
    """Return disk usage information."""
    print("Getting disk usage information...")
    disk = psutil.disk_usage("/")

    return {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "usage_percent": disk.percent
    }


def get_system_info():
    """Return complete basic system information."""
    print("Getting system information...")
    return {
        "os": get_os_info(),
        "cpu_usage_percent": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "cpu_count": get_cpu_count(),
        "logical_cpu_count": get_logical_cpu_count(),
        
    }


if __name__ == "__main__":
    pprint(get_system_info())