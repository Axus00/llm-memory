from fastapi import FastAPI, APIRouter
from core.graph import graph_compiled
from pydantic import BaseModel
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


router = APIRouter(prefix="/agent")


class ChatRequest(BaseModel):
    user_input: str
    user_id: str


class ChatResponse(BaseModel):
    response: str
    user_id: str
    status: str


@router.post("/")
def execute_agent(request: ChatRequest):
    try:
        logger.info(f"Procesando solicitud del usuario: {request.user_id}")


        initial_state = {
            "user_input": request.user_input,
            "response": "",
            "memory_loaded": False,
            "context": ""
        }

        config = {"configurable": {"thread_id": request.user_id}}


        result = graph_compiled.invoke(initial_state, config=config)


        logger.info(f"Respuesta generada exitosamente para: {request.user_id}")
        
        return ChatResponse (
            response = result["response"],
            user_id = request.user_id,
            status = "Success"
        )
    except Exception as e:
        logger.error(f"Error procesando solicitud: {str(e)}")

        return ChatResponse(
            response=f"Lo siento, ocurrió un error al procesar tu solicitud: {str(e)}",
            user_id=request.user_id,
            status="error"
        )


app.include_router(router)