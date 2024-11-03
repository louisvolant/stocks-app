# app/data/asset.py

# Définir la classe Asset
class Asset:
    def __init__(self, name, exchange, assetType, ipoDate, delistingDate, status):
        self.name = name
        self.exchange = exchange
        self.assetType = assetType
        self.ipoDate = ipoDate
        self.delistingDate = delistingDate
        self.status = status

    def __repr__(self):
        return f"Asset(name={self.name}, exchange={self.exchange}, assetType={self.assetType}, ipoDate={self.ipoDate}, delistingDate={self.delistingDate}, status={self.status})"
