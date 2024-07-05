from langchain_chroma import Chroma
from langchain.chains import create_history_aware_retriever
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_models import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

EMBEDDINGS = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
LLM = ChatOllama(model="gemma:2b")

vectorStore = Chroma(persist_directory='./chroma_db', embedding_function=EMBEDDINGS)
retriever = vectorStore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k":2,
        #have to work on way
        #To make my search results rely mostly on the documents 
        #Rarely on Search results by the LLM
        "score_threshold": 0.30
    },
)

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriever = create_history_aware_retriever(
    LLM, retriever, contextualize_q_prompt
)

system_prompt = (
    '''You are an assistant for question-answering tasks in a career management centre. 
Do not answer any question not related to career development.
If the question's answer is not available in the database say
you don't know. Or if you don't know the answer to the
question say you don't know. Write maximum one paragraph. '''
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(LLM, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever,question_answer_chain)
#rag_chain.invoke({"input": "What does a Data Analyst do?"})
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversationRAGChain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)


def ChatBot(msg: str, sessionID: str = "testing"):
    return conversationRAGChain.invoke(
        {"input": msg},
        config={
            "configurable": {"session_id": sessionID}
        },  # constructs a key "abc123" in `store`.
        )["answer"]
