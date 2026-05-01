def prepare_input(data):
    return {
        "context": data.context,
        "image_description": data.image_description or "",
        "brand_voice": data.brand_voice,
        "target_audience": data.target_audience,
        "platform": data.platform,
        "goal": data.goal,
        "constraints": data.constraints or ""
    }