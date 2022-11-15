import datetime


class Extension:
    def __init__(self, name, version, url,
                 date_added=None):
        self.name = name
        self.version = version
        self.url = url
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()

    def __repr__(self) -> str:
        return f"({self.name}, {self.version}, {self.url}, {self.date_added})"