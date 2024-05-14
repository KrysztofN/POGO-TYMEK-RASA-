from flask import Flask, render_template, jsonify, request
import requests

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)

policy_accepted = False

@app.route('/')
def index():
    return render_template("weather_bot.html")

@app.route('/webhook', methods=['POST'])
def webhook():
    global policy_accepted

    if not policy_accepted:
        return jsonify({'response': 'Proszę zaakceptować naszą politykę prywatności przed kontynuacją.'})

    user_message = request.json['message']
    print("User message:", user_message)

    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response: ", rasa_response_json)

    bot_responses = [response.get('text', '') for response in rasa_response_json]
    bot_response = ' '.join(bot_responses)

    return jsonify({'response': bot_response})


@app.route('/accept_policy', methods=['POST'])
def accept_policy():
    global policy_accepted
    policy_accepted = True
    return jsonify({'message': 'Dziękujemy za zaakceptowanie naszej polityki prywatności.'})


if __name__ == "__main__":
    app.run(debug=True, port=3000)
