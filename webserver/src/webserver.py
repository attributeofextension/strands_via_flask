from flask import Flask, request, render_template
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

@app.route('/prompt', methods=['POST'])
def simple_prompt():
    prompt = request.form.get('prompt')

    if prompt is None:
        return 'no prompt', 400


    agent_response = agent(prompt)
    print(agent_response)

    return render_template('ai-message.html', message=agent_response)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True, use_reloader=True)