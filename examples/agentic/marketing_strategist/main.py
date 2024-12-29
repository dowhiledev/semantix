"""Market Research Agent."""

from marketing_strategist.models import MarketingCampaign
from marketing_strategist.tasks import tasks

from semantix import llms

llm = llms.BaseLLM


@llm.manager(tasks, verbose=True)
def marketing_campaign(
    project_description: str, customer_domain: str
) -> MarketingCampaign:
    """You are the Marketing Campaign Manager at a leading digital marketing agency.
    Your role is to oversee the development and execution of marketing campaigns for clients.
    """
    ...


if __name__ == "__main__":
    project_description = """TalentZap! is a new online platform for Talents and Human Resource Teams
    Customer Domain:
    Project Overview: Creating a comprehensive marketing campaign to boost awareness and adoption of
    CrewAI's services among enterprise clients.
    """
    campaign = marketing_campaign("crewai.com", project_description)
    print(campaign)
