# customWarnings.py (Python)

class CustomWarnings:
    def __init__(self):
        self.warnings = {}

    def add_warning(self, user_id, reason):
        if user_id in self.warnings:
            self.warnings[user_id].append(reason)
        else:
            self.warnings[user_id] = [reason]

    def remove_warning(self, user_id):
        if user_id in self.warnings:
            del self.warnings[user_id]
        else:
            print("User does not have any warnings.")

    def get_warnings(self, user_id):
        if user_id in self.warnings:
            return self.warnings[user_id]
        else:
            return []

# End of customWarnings.py