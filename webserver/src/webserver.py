from flask import Flask, request
from strands import Agent
from strands.agent import NullConversationManager
from strands.models.ollama import OllamaModel
from urllib.parse import unquote_plus


ollama_model = OllamaModel(
    host="http://host.docker.internal:11434",
    model_id="llama3",
)

agent = Agent(model=ollama_model, conversation_manager=NullConversationManager())
app = Flask(__name__)

@app.route('/', methods=['GET'])
def simple_prompt():
    prompt = request.args.get('prompt')

    if prompt is None:
        return 'no prompt', 200

    print(prompt)
    prompt_text = unquote_plus(prompt)
    agent_response = agent(prompt_text)
    print(agent_response)

    return agent_response.message, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True, use_reloader=True)