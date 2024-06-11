import psutil
import os

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