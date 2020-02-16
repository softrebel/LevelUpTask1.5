class Product:
    def __init__(self, name: str = None, customerId: int = None, is_enable: int = None, ID: int = None):
        self.ID: int = ID
        self.customerId: int = customerId
        self.name: str = name
        self.is_enable: int = is_enable
