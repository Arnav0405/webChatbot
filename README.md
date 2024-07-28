# Chatbot Deployment with FastAPI and JavaScript LangChain

I have used a youtube tutorial to get the JS and HTML part

But the tutorial was using Flask, which work somewhat slower than FastAPI and FastAPI works well with langchain hence, I had to convert most of the Flask code to FastAPI code. But FastAPI is shit, so I re-wrote it to Flask.

## Modules and Pre-installation
Do install all the requirements from requirements.txt file if I have made one. Also we need to install Ollama along with Gemma:2b for the LLM to work.

Ollama Installation, past the following code in your terminal(for linux)
'''
curl -fsSL https://ollama.com/install.sh | sh

ollama run gemma:2b
'''
or use the website, download the gemma:2b model for the chatting part to work.
https://ollama.com/download

## To Deploy 
'''
python3 app.py 
'''

## Note
Do install ollama before anything else as it is 1.7gb.

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
# webChatbot
