# controller/permissions.py
class Permissions:
    def can_read(self, path: str) -> bool:
        return path.startswith("./memory/")