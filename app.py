import streamlit as st
import time
    
def char_converter(raw_char):
        """Convert Korean character by manipulating its Unicode value"""
        n = ord(raw_char)
        b = (n-44032) % 588
        c = (n-44032) % 28
        return chr(n-b+84+c)
    
def sentence_converter(raw_sentence):
        """Convert Korean characters in a sentence"""
        result = ''
        for c in raw_sentence:
            if '가' <= c <= '힣':
                result += char_converter(c)
            else:
                result += c
        return result
    
    # Streamlit app configuration
st.set_page_config(
        page_title="킹받는 챗봇",
        page_icon="💬",
        layout="centered"
    )
    
    # Title
st.title("매우 킹받는 챗봇: 햬쟤먤럐걔")
st.caption("떽! 을 입력하면 멈춥니다(느낌표까지)")
    
    # Initialize chat history in session state
if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history
for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
flag = st.session_state.get("flag", False)
if prompt := st.chat_input(placeholder="메시지를 입력하세요", disabled=flag):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
    
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Generate response
        if prompt == '떽!':
            response = "메롱!"
            st.session_state.flag = True
            st.rerun()
        else:
            response = sentence_converter(prompt)
    
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
        # Display assistant response
        time.sleep(0.3)
        with st.chat_message("assistant"):
            st.markdown(response)
    
    
