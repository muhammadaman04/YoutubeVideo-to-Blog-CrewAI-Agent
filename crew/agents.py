from crewai import Agent, LLM
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = "NA"
groq_api_key = os.getenv("GROQ_API_KEY")
llm = LLM(model="groq/llama-3.1-70b-versatile")

blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="Get the relevant video transcription for the topic {topic} from the provided YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, "
        "and Generative AI and providing suggestions."
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm = llm

)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)
