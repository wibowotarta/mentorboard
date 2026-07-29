# === Stage 61: Add performance timing for core list and search operations ===
# Project: MentorBoard
import time

class PerformanceTimer:
    def __init__(self):
        self.timings = []
        self.name_to_count = {}
    
    def measure(self, name, operation_func):
        start = time.perf_counter()
        result = operation_func()
        elapsed_ms = (time.perf_counter() - start) * 1000
        
        count = self.name_to_count.get(name, 0)
        if isinstance(result, list):
            avg_ms = sum(self.timings[-count*2:] if len(self.timings) >= count*2 else []) / max(count, 1)
        else:
            avg_ms = (self.timings[-1] * count + elapsed_ms) / (count + 1) if self.timings else elapsed_ms
        
        self.timings.append(elapsed_ms)
        self.name_to_count[name] = count + 1
        
        return {
            'name': name,
            'time_ms': round(elapsed_ms, 3),
            'avg_ms': round(avg_ms, 3),
            'count': count + 1
        }

    def report(self):
        if not self.timings:
            return "No measurements taken yet."
        
        lines = []
        for i in range(0, len(self.timings), 5):
            batch = self.timings[i:i+5]
            avg = sum(batch) / len(batch)
            min_t = min(batch)
            max_t = max(batch)
            
            if len(batch) == 1:
                label = "Single operation"
            elif len(batch) <= 3:
                label = f"{len(batch)} operations"
            else:
                label = f"{len(batch)} operations (avg)"
            
            lines.append(f"[{label}] avg={avg:.2f}ms min={min_t:.2f}ms max={max_t:.2f}ms")
        
        return "\n".join(lines)

# Example usage:
timer = PerformanceTimer()

def list_all_items():
    # Simulate listing items from a mentoring session tracker
    return [
        {"id": 1, "name": "Goal Setting", "status": "active"},
        {"id": 2, "name": "Question Review", "status": "completed"},
        {"id": 3, "name": "Resource Sharing", "status": "pending"},
        {"id": 4, "name": "Feedback Collection", "status": "in_progress"},
        {"id": 5, "name": "Progress Report", "status": "scheduled"}
    ]

def search_by_status(status):
    # Simulate searching items by status in mentoring tracker
    return [item for item in list_all_items() if item["status"] == status]

# Measure performance of core operations
list_result = timer.measure("List all items", lambda: list_all_items())
search_result = timer.measure(f"Search by '{active}' status", lambda: search_by_status("active"))

print(f"\nPerformance Report:")
print(timer.report())
