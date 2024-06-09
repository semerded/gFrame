import uuid
from . import data

def generateID():
    return uuid.uuid4()

def removeIDfromWCU(id: uuid.UUID):
    "remove a widget ID from the widget constant update list"
    if id in data.widgetConstantUpdates.keys():
        return data.widgetConstantUpdates.pop(id)