"""Module to collect statistics of memory, cpu and I/O"""
import os
import psutil

def collect_statistics():
    """Collect memory and CPU statistics."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    cpu_times = process.cpu_times()
    io_counters = process.io_counters()

    stats = {
            "memory_rss": mem_info.rss,  # Resident Set Size
            "memory_vms": mem_info.vms,  # Virtual Memory Size
            "cpu_user": cpu_times.user,
            "cpu_system": cpu_times.system,
            "io_read_count": io_counters.read_count,
            "io_write_count": io_counters.write_count,
            "io_read_bytes": io_counters.read_bytes,
            "io_write_bytes": io_counters.write_bytes
        }
        
    return stats

def print_stats(tracemalloc)->str:
    """
    Print memory, cpu and io stats
    """
    stats = collect_statistics()
    current, peak = tracemalloc.get_traced_memory()
    log_message = f"""
    ##################### Some Stats ########################
    Current memory usage: {current} bytes | Peak: {peak} bytes
    CPU User: {float(stats.get('cpu_user')) * 100:.2f} % | CPU System {float(stats.get('cpu_system')) * 100:.2f} %
    IO Read Bytes: {float(stats.get('io_read_bytes')):.2f} | IO Write Bytes: {float(stats.get('io_write_bytes')):.2f}
    """
    return log_message