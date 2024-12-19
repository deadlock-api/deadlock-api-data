from pydantic import BaseModel


class MatchCreatedWebhookPayload(BaseModel):
    match_id: int
    metadata_url: str
    raw_metadata_url: str


class WebhookSubscribeRequest(BaseModel):
    webhook_url: str
