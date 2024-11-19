from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from src.relationships.relationship_model import RelationshipModel
from src.visualize.visualize_graph import GraphVisualization
from src.globals import text, system_prompt


visualizer = GraphVisualization() 
llm = ChatOpenAI(model='gpt-4o', temperature=0.9).with_structured_output(RelationshipModel)
prompt = ChatPromptTemplate.from_messages([
        ("system", "{system_prompt}"),
        ("human", "{text}")
    ])

chain = prompt | llm
response = chain.invoke({"system_prompt":system_prompt, "text":text})
relationships = response.model_dump()['relationships']

for rel in relationships:
    visualizer.add_edge(rel['source']['name'], rel['target']['name'], rel['description'])
    
visualizer.visualize()
