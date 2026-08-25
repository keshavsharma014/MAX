import os
import psutil


def get_process_count():
    """Return the number of currently running processes."""
    return len(psutil.pids())

def get_process_info(pid):
    """Return information about a specific process."""
    
    try:
        process = psutil.Process(pid)

        return {
            "pid": process.pid,
            "name": process.name(),
            "status": process.status(),
            "cpu_usage_percent": process.cpu_percent(interval=1),
            "memory_usage_percent": process.memory_percent()
        }
    except psutil.NoSuchProcess:
        return {
            "error": f"No process found with PID: {pid}"
        }

    except psutil.AccessDenied:
        return {
            "error": f"Access denied for process with PID: {pid}"
        }

def get_top_processes_by_cpu(limit=5):
    """Return processes using the most CPU."""

    processes = []

    for process in psutil.process_iter(["pid", "name","status"]):
        try:
            cpu_usage = process.cpu_percent(interval=0.1)
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "status": process.info["status"],
                "cpu_usage_percent": cpu_usage
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(
        key=lambda process: process["cpu_usage_percent"],
        reverse=True
    )

    return processes[:limit]

def get_top_processes_by_memory(limit=5):
    """Return processes using the most memory."""

    processes = []

    for process in psutil.process_iter(["pid", "name","status"]):
        try:
            memory_usage = process.memory_percent()

            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "status": process.info["status"],
                "memory_usage_percent": round(memory_usage, 2)
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(
        key=lambda process: process["memory_usage_percent"],
        reverse=True
    )

    return processes[:limit]

def get_all_processes():
    """Return basic information about all running processes."""
    processes = []

    for process in psutil.process_iter(["pid", "name", "status"]):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes

def find_process(name):
    """Find running processes by name."""

    found_processes = []

    for process in psutil.process_iter(["pid", "name", "status"]):
        try:
            process_name = process.info["name"]
            if process_name and name.lower() in process_name.lower():
                found_processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return found_processes

def get_current_process_info():
    """Return information about the current MAX process."""
    current_pid = os.getpid()
    return get_process_info(current_pid)

if __name__ == "__main__":
    print("Process Count:")
    print(get_process_count())

    print("\nCurrent MAX Process:")
    print(get_current_process_info())

    print("\nChrome Processes:")
    print(find_process("chrome"))

    print("\nTop CPU Processes:")
    for process in get_top_processes_by_cpu():
        print(process)

    print("\nTop Memory Processes:")
    for process in get_top_processes_by_memory():
        print(process)