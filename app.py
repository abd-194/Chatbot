import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
os.environ['OPENAI_API_KEY'] = "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"
# App framework
st.title('Cedrics')
prompt = st.text_input('Write your Query')
# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='act as a fitness expert and your name is Olivia. answer politely about the {topic} if it is related to fitness, health or diet only. Otherwise tell the user that it is out of your scope and don\'t answer his query in anyway. don\'t talk extra.'
)
# Initialize or get the session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history', buffer=st.session_state.chat_history)
# Llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
wiki = WikipediaAPIWrapper()
# Show stuff to the screen if there’s a prompt
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    st.write(title)
