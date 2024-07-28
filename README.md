# Chatbot Deployment with FastAPI and JavaScript LangChain

Made a Vector database based on my pdf files. Implemented the Vector Database on this Ollama based LLM that is running on your system, but it's completely free unlike ChatGPT or any other big compan one! 


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
