class Source:
    def __init__(self, name: str = None, is_premium: int = None, is_enable: int = None, ID: int = None):
        self.ID: int = ID
        self.name: str = name
        self.is_premium: int = is_premium
        self.is_enable: int = is_enable
