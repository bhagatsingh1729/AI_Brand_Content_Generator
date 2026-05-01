from langchain_core.prompts import ChatPromptTemplate

# -------- CONTENT PROMPT --------
content_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a brand content generator. Generate high-quality content."),
    ("human", """
Context: {context}
Image: {image_description}
Brand Voice: {brand_voice}
Audience: {target_audience}
Platform: {platform}
Goal: {goal}
Constraints: {constraints}

Return JSON with:
content, content_type, tone_used, strategy_used
""")
])


# -------- ROUTER PROMPT --------
router_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI model selector."),
    ("human", """
Context: {context}

Classify complexity:
LOW / MEDIUM / HIGH

Return JSON:
complexity, selected_model
""")
])