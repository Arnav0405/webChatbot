# Chatbot Building & Deployment with FastAPI and JavaScript LangChain

Made a Vector database based on my pdf files. Implemented the Vector Database on this Ollama based LLM that is running on your system, but it's completely free unlike ChatGPT or any other big company one! 


## Modules and Pre-installation
Do install all the requirements from `requirements.txt` file if I have made one. Also you need to install Ollama along with Gemma:2b for the LLM to work.

Ollama Installation, past the following code in your terminal(for linux)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

```bash
ollama run gemma:2b
```
or use the [official Ollama website](https://ollama.com/download) to download the gemma:2b model for the chatting part to work.

## To Deploy 

```bash
python3 app.py 
```

> [!WARNING]
> Do install ollama before anything else as it is 1.7 GB.

## Credits:
Kevin Nacario - [Frontend boilerplate code](https://github.com/hitchcliff/front-end-chatjs)

# webChatbot
