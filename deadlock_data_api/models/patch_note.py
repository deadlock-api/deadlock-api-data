from datetime import datetime
from email.utils import parsedate_to_datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class PatchNoteGuid(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_perma_link: bool = Field(..., validation_alias="@isPermaLink")
    text: str = Field(..., validation_alias="#text")


class PatchNoteCategory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    domain: str = Field(..., validation_alias="@domain")
    text: str = Field(..., validation_alias="#text")


class PatchNote(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str
    pub_date: str | datetime = Field(..., validation_alias="pubDate")
    link: str
    guid: PatchNoteGuid
    author: str
    category: PatchNoteCategory
    dc_creator: str = Field(..., validation_alias="dc:creator")
    content_encoded: str = Field(..., validation_alias="content:encoded")
    slash_comments: str = Field(..., validation_alias="slash:comments")

    @field_validator("pub_date", mode="before")
    @classmethod
    def validate_pub_date(cls, value):
        if isinstance(value, str):
            return parsedate_to_datetime(value)
        return value
