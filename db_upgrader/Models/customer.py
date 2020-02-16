import datetime


class Customer:
    def __init__(self, name: str = None, is_enable: int = None, ID: int = None, created_by: int = None,
                 created_at: datetime = None,
                 update_by: int = None,
                 updated_at: datetime = None):
        self.ID: int = ID
        self.name: str = name
        self.is_enable: int = is_enable
        self.created_by: int = created_by
        self.created_at: datetime = created_at
        self.update_by: int = update_by
        self.updated_at: datetime = updated_at
