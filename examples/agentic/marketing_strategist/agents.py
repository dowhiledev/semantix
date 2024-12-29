from semantix.llms.base import BaseLLM

llm = BaseLLM()


@llm.agent(
    "Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.",
    tools=[],
)
def lead_market_analyst() -> None:
    """As the Lead Market Analyst at a premier digital marketing firm, you specialize
    in dissecting online business landscapes."""
    ...


@llm.agent(
    "Synthesize amazing insights from product analysis to formulate incredible marketing strategies.",
    tools=[],
)
def chief_marketing_strategist() -> None:
    """You are the Chief Marketing Strategist at a leading digital marketing agency,
    known for crafting bespoke strategies that drive success."""
    ...


@llm.agent(
    "Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.",
)
def creative_content_creator() -> None:
    """As a Creative Content Creator at a top-tier digital marketing agency, you
    excel in crafting narratives that resonate with audiences. Your expertise
    lies in turning marketing strategies into engaging stories and visual
    content that capture attention and inspire action."""
    ...


@llm.agent(
    "Oversee the work done by your team to make sure it is the best possible and aligned with the product goals, review, approve, ask clarifying questions or delegate follow-up work if necessary."
)
def chief_creative_director() -> None:
    """You are the Chief Content Officer at a leading digital marketing agency
    specializing in product branding. You ensure your team crafts the best
    possible content for the customer."""
    ...


agents = [
    lead_market_analyst,
    chief_marketing_strategist,
    creative_content_creator,
    chief_creative_director,
]

print(agents)

__all__ = [
    "agents",
    "lead_market_analyst",
    "chief_marketing_strategist",
    "creative_content_creator",
    "chief_creative_director",
]
