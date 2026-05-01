from fastapi import APIRouter
from app.schemas import ContentRequest, ContentResponse
from app.graph import graph
from app.utils import prepare_input

router = APIRouter()

@router.post("/generate", response_model=ContentResponse)
def generate_content(request: ContentRequest):
    
    input_data = prepare_input(request)

    result = graph.invoke({
        "input_data": input_data
    })

    return result["final_output"]