import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('assistant'):
#     st.text('How can i help you')


# user_input = st.chat_input('type here')
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# user_input = st.chat_input('type here')

# if user_input:
#     # first add the message to message_history
#     st.session_state['message_history'].append(
#         {'role': 'user', 'content': user_input}
#     )
#     with st.chat_message('user'):
#         st.text(user_input)

#     chatbot.invoke()
    
#     # first add the message to message_history
#     st.session_state['message_history'].append(
#         {'role': 'assistant', 'content': user_input}
#     )
#     with st.chat_message('assistant'):
#         st.text(user_input)

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input}) #Role defining as user
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    
    ai_message = response['messages'][-1].content
    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})     #Role defining as assistant
    with st.chat_message('assistant'):
        st.text(ai_message)
