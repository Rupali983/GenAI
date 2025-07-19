from rag_chain import answer_question

if __name__ == "__main__":
    print("Welcome to GenAI RAG Chatbot (type 'exit' to quit)\n")
    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break
        response = answer_question(question)
        print(response + "\n")


