class MemoryStore:
    def __init__(self):
        # Initial memory state
        self._last_result = None

    def save_result(self, value):
        """Pichla calculation result store karne ke liye."""
        self._last_result = value

    def get_last_result(self):
        """Store kiya hua result hasil karne ke liye."""
        return self._last_result

    def clear(self):
        """Memory ko reset karne ke liye."""
        self._last_result = None

# Instance create kar rahe hain taake index.py isse use kar sake
calc_memory = MemoryStore()