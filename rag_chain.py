# from langchain.chat_models import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from db_utils import run_query
# import os

# def get_rag_chain():
#     template = """
#     You are a helpful assistant. Convert the user's question into a MySQL query 
#     based on the fealty_db database schema. Do not explain. Just output the SQL query.

#     Question: {question}

#     MySQL Query:
#     """
#     prompt = PromptTemplate(input_variables=["question"], template=template)
#     llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
#     return LLMChain(prompt=prompt, llm=llm)

# def answer_question(question):
#     chain = get_rag_chain()
#     sql_query = chain.run(question)
#     try:
#         results = run_query(sql_query)
#         return f"SQL Query:\n{sql_query}\n\nResults:\n{results}"
#     except Exception as e:
#         return f"Error running SQL: {sql_query}\n{e}"


#  use by openai_api_key
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from db_utils import run_query

# def get_rag_chain():
#     template = """
#     You are a helpful assistant. Convert the user's question into a MySQL query 
#     based on the fealty_db database schema. Do not explain. Just output the SQL query.

#     Question: {question}

#     MySQL Query:
#     """
#     prompt = PromptTemplate(input_variables=["question"], template=template)

   
#     llm = ChatOpenAI(
#         temperature=0,
#         openai_api_key="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"
#     )

#     return LLMChain(prompt=prompt, llm=llm)

# def answer_question(question):
#     chain = get_rag_chain()
#     sql_query = chain.run(question)
#     try:
#         results = run_query(sql_query)
#         return f"SQL Query:\n{sql_query}\n\nResults:\n{results}"
#     except Exception as e:
#         return f"Error running SQL: {sql_query}\n{e}"
# from langchain_community.chat_models import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from db_utils import run_query

# def get_rag_chain():
#     template = """
#     You are a helpful assistant. Convert the user's question into a MySQL query 
#     based on the fealty_db database schema. Do not explain. Just output the SQL query.

#     Question: {question}

#     MySQL Query:
#     """
#     prompt = PromptTemplate(input_variables=["question"], template=template)

#     llm = ChatOpenAI(
#         temperature=0,
#         openai_api_key="sk-..."  # 
#     )

#     return LLMChain(prompt=prompt, llm=llm)

# def answer_question(question):
#     chain = get_rag_chain()
#     sql_query = chain.run(question)
#     try:
#         results = run_query(sql_query)
#         return f"SQL Query:\n{sql_query}\n\nResults:\n{results}"
#     except Exception as e:
#         return f"Error running SQL: {sql_query}\n\n{e}"

# gemini key use 
import google.generativeai as genai
from db_utils import run_query


genai.configure(api_key="AIzaSyAAaLNWsJ1w4jX93S4nM3TFfOPSd-Tv-iQ")


model = genai.GenerativeModel(model_name="gemini-1.5-pro")

def get_sql_from_question(question):
    prompt = f"""
    You are a helpful assistant. Convert the following question into a MySQL query 
    for the fealty_db schema. Only return the SQL query.

    Question: {question}

    SQL Query:
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def answer_question(question):
    sql_query = get_sql_from_question(question)
    try:
        results = run_query(sql_query)
        return f"SQL Query:\n{sql_query}\n\nResults:\n{results}"
    except Exception as e:
        return f"Error running SQL: {sql_query}\n\n{e}"
