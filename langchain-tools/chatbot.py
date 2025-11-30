from dotenv import load_dotenv
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_groq import ChatGroq

load_dotenv()  

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=3, doc_content_chars_max=500)
arxiv_tool = ArxivQueryRun(
    api_wrapper=api_wrapper_arxiv,
    description="Search for scientific papers on arXiv",
)

api_wrapper_wikipedia = WikipediaAPIWrapper(
    top_k_results=3, doc_content_chars_max=500
)
wikipedia_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper_wikipedia,
    description="Search for information on Wikipedia",
)

tools = [arxiv_tool, wikipedia_tool]

llm = ChatGroq(model="llama3-8b-8192")

print(llm.invoke("What is the latest research on quantum computing?"))

llm.bind_tools(tools)
