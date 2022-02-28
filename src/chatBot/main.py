from src.controllers.DialogFlowController import dialogFlowController
from src.utils.helpers.general.logging import setup_logging
import fastapi

setup_logging()

app = fastapi.FastAPI(title="EtherBot_DataService")
app.include_router(dialogFlowController, prefix="/dialogFlow", tags=["dialogFlow"])