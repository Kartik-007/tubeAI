from crewai import Crew, Process

from agents import YoutubeAutomationAgents
from tasks import YoutubeAutomationTasks
from langchain_openai import ChatOpenAI
from tools.youtube_video_details_tool import YoutubeVideoDetailsTool
from tools.youtube_video_search_tool import YoutubeVideoSearchTool

from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)

agents = YoutubeAutomationAgents()
tasks = YoutubeAutomationTasks()

youtube_video_search_tool = YoutubeVideoSearchTool()
youtube_video_details_tool = YoutubeVideoDetailsTool()

youtube_manager = agents.youtube_manager()
research_manager = agents.research_manager(
    youtube_video_search_tool, youtube_video_details_tool)
title_creator = agents.title_creator()
description_creator = agents.description_creator()
# email_creator = agents.email_creator()

# TODO: UPDATE THE VIDEO DETAILS

video_topic = "How to make money using Ai"
video_details = """
In this video I will talk about some ways one can harness the power of new AI tools and technolgies to start
earning money online with much greater efficiency. This video will focus on using Ai tools to make money online and start
online businesses. It will provide the user with ideas and tools needed to execute them.
"""

manage_youtube_video_creation = tasks.manage_youtube_video_creation(
    agent=youtube_manager,
    video_topic=video_topic,
    video_details=video_details
)
manage_youtube_video_research = tasks.manage_youtube_video_research(
    agent=research_manager,
    video_topic=video_topic,
    video_details=video_details,
)
create_youtube_video_title = tasks.create_youtube_video_title(
    agent=title_creator,
    video_topic=video_topic,
    video_details=video_details
)
create_youtube_video_description = tasks.create_youtube_video_description(
    agent=description_creator,
    video_topic=video_topic,
    video_details=video_details
)



# Create a new Crew instance
crew = Crew(
    agents=[youtube_manager,
            research_manager,
            title_creator,
            description_creator,
            ],
    tasks=[manage_youtube_video_creation,
           manage_youtube_video_research,
           create_youtube_video_title,
           create_youtube_video_description
        ],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4
)

# Kick of the crew
results = crew.kickoff()

print("Crew usage", crew.usage_metrics)

print("Crew work results:")
print(results)