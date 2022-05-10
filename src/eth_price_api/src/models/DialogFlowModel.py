from pydantic import BaseModel

class DisplayNameModel(BaseModel):
    displayName: str

class IntentModel(BaseModel):
    intent: DisplayNameModel

class DialogFlowModel(BaseModel):
    queryResult: IntentModel
