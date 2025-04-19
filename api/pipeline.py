from run import get_recommendation_summary, get_top_options, implement_selected_option

async def deployment_recommendation_request(requirements: str):
    summary, requirements = await get_recommendation_summary(requirements)
    if summary:
        recommendations = await get_top_options(summary=summary, requirements=requirements)
    return {'summary': summary.raw, 'recommendations': recommendations}


async def process_deployment_request(selected_option: str):
    response = await implement_selected_option(selected_option)
    return {'status': response}