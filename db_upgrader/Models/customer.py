class Customer():

    def __init__(self, name=None, is_enable=None, ID=None, created_by=None, created_at=None, update_by=None,
                 updated_at=None):
        self.ID = ID
        self.name = name
        self.is_enable = is_enable
        self.created_by = created_by
        self.created_at = created_at
        self.update_by = update_by
        self.updated_at = updated_at
