from typing import List
from pydantic import BaseModel, Field


class MarketStrategy(BaseModel):
    """A detailed marketing strategy document that outlines the goals, target audience, key messages, and proposed tactics."""

    name: str = Field(..., description="Name of the market strategy")
    tatics: List[str] = Field(
        ..., description="List of tactics to be used in the market strategy"
    )
    channels: List[str] = Field(
        ..., description="List of channels to be used in the market strategy"
    )
    KPIs: List[str] = Field(
        ..., description="List of KPIs to be used in the market strategy"
    )


class CampaignIdea(BaseModel):
    name: str = Field(..., description="Name of the campaign idea")
    description: str = Field(..., description="Description of the campaign idea")
    audience: str = Field(..., description="Audience of the campaign idea")
    channel: str = Field(..., description="Channel of the campaign idea")


class Copy(BaseModel):
    title: str = Field(..., description="Title of the copy")
    body: str = Field(..., description="Body of the copy")


class MarketingCampaign(BaseModel):
    name: str = Field(..., description="Name of the marketing campaign")
    description: str = Field(..., description="Description of the marketing campaign")
    strategy: MarketStrategy = Field(
        ..., description="Marketing strategy for the campaign"
    )
    ideas: List[CampaignIdea] = Field(
        ..., description="List of campaign ideas for the campaign"
    )
    copies: List[Copy] = Field(
        ..., description="List of marketing copies for the campaign"
    )
