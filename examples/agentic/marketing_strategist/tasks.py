from semantix import Semantic
from agents import (
    lead_market_analyst,
    chief_marketing_strategist,
    creative_content_creator,
)
from models import MarketStrategy, CampaignIdea, Copy


@lead_market_analyst.task
def research_task(customer_domain: str, project_description: str) -> Semantic[
    str,
    "A complete report on the customer and their customers and competitors, "
    "including their demographics, preferences, market positioning and audience engagement.",  # type: ignore
]:
    """
    Conduct a thorough research about the customer and competitors in the context
    of {customer_domain}.
    Make sure you find any interesting and relevant information given the
    current year is 2024.
    We are working with them on the following project: {project_description}.
    """
    ...


@chief_marketing_strategist.task
def project_understanding_task(
    project_description: str,
) -> Semantic[
    str, "A detailed summary of the project and a profile of the target audience."  # type: ignore
]:
    """
    Understand the project details and the target audience for
    {project_description}.
    Review any provided materials and gather additional information as needed.
    """
    ...


@chief_marketing_strategist.task
def marketing_strategy_task(
    project_description: str,
    customer_domain: str,
) -> MarketStrategy:
    """
    Formulate a comprehensive marketing strategy for the project
    {project_description} of the customer {customer_domain}.
    Use the insights from the research task and the project understanding
    task to create a high-quality strategy.
    """
    ...


@creative_content_creator.task
def create_campaign_ideas(
    project_description: str,
) -> Semantic[list[CampaignIdea], "A list of 5 campaign ideas"]:  # type: ignore
    """
    Develop creative marketing campaign ideas for {project_description}.
    Ensure the ideas are innovative, engaging, and aligned with the overall marketing strategy.
    """
    ...


@creative_content_creator.task
def copy_creation_task(
    project_description: str,
) -> Semantic[list[Copy], "Marketing copy for each campaign idea"]:  # type: ignore
    """
    Create marketing copies based on the approved campaign ideas for {project_description}.
    Ensure the copies are compelling, clear, and tailored to the target audience.
    """
    ...


market_strategy_creation_tasks = [
    research_task,
    project_understanding_task,
    marketing_strategy_task,
    create_campaign_ideas,
    copy_creation_task,
]

print(market_strategy_creation_tasks)

__all__ = ["market_strategy_creation_tasks"]
