import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool,
	FirecrawlCrawlWebsiteTool
)





@CrewBase
class ConceptMapGeneratorCrew:
    """ConceptMapGenerator crew"""

    
    @agent
    def keyword_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["keyword_specialist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def mind_map_designer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["mind_map_designer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def website_content_extractor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["website_content_extractor"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def website_crawler(self) -> Agent:
        
        return Agent(
            config=self.agents_config["website_crawler"],
            
            
            tools=[				FirecrawlCrawlWebsiteTool(),
				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def content_analyzer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_analyzer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def extract_website_content(self) -> Task:
        return Task(
            config=self.tasks_config["extract_website_content"],
            markdown=False,
            
            
        )
    
    @task
    def crawl_target_sections(self) -> Task:
        return Task(
            config=self.tasks_config["crawl_target_sections"],
            markdown=False,
            
            
        )
    
    @task
    def analyze_important_topics(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_important_topics"],
            markdown=False,
            
            
        )
    
    @task
    def extract_key_keywords(self) -> Task:
        return Task(
            config=self.tasks_config["extract_key_keywords"],
            markdown=False,
            
            
        )
    
    @task
    def generate_mind_map(self) -> Task:
        return Task(
            config=self.tasks_config["generate_mind_map"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ConceptMapGenerator crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
