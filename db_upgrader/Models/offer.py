import datetime


class Offer:
    def __init__(self, userId: int = None, productId: int = None, sourceId: int = None, created_at: datetime = None,
                 order: int = None, ID: int = None):
        self.ID: int = ID
        self.userId: int = userId
        self.productId: int = productId
        self.sourceId: int = sourceId
        self.created_at: datetime = created_at
        self.order: int = order
