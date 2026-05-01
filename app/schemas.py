from pydantic import BaseModel
from typing import Optional

class ContentRequest(BaseModel):
    context: str
    image_description: Optional[str] = ""
    brand_voice: str
    target_audience: str
    platform: str
    goal: str
    constraints: Optional[str] = ""


class ContentResponse(BaseModel):
    content: str
    content_type: str
    tone_used: str
    strategy_used: str