# POGO-TYMEK-RASA
Pogo-Tymek (Polish RASA weather bot)

Weather Bot that supports over 200 000 cities worldwide.
<br><br>
How to use?
1. Install all neccessary libraries
2. Open rasa project and in terminal navigate to rasa project directory
3. To start Chat with the bot type:  rasa run && rasa run actions
4. Wait for the bot model to load and start chatting ;)

<br><br>
How to use website with the bot?
1. Open rasa project and in terminal navigate to rasa project directory
2. In terminal run: rasa run && rasa run actions
3. Navigate to app.py and run
4. Open localhost on port 3000
5. Talk to the bot ;)

<br><br>
How to use rasa with telegram?
1. Instal ngrok: https://ngrok.com/download
2. Open ngrok and type: ngrok http 5005
3. In ngrok copy the "Forwarding" address
4. Go to Bot Father in telegram : https://telegram.me/BotFather
5. Follow further steps described here: https://rasa.com/docs/rasa/connectors/telegram/
6. From step 2 copy the forwarding address into: http://your_forwarding_address/webhooks/telegram/webhook
7. In terminal type: rasa run --enable-api --cors "*" --debug && rasa run actions
8. Open your created telegram bot and start a conversation.
9. You're now able to talk to the bot via telegram

<br><br>
Debugging:
1. If you have problems with getting internal server error when you try to run your telegram bot
2. Try to type in terminal: pip install -U aiogram==2.25.2.
3. If that didn't help try to upgrade rasa and again aiogram.
4. ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/de2de1ea-0bcd-43de-8017-4b2c6e380a83)
5. You should see this:
6. ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/517e2bad-0120-4d4a-8f6d-a8945b20e18f)


Pogo-Tymek in action:
<br>
1. Telegram private conversation: ![one](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/dd2501db-3ce1-4414-bce9-792bc23d1cdd)
<br>
3. Telegram Channel : ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/1725f4f4-a820-43ee-b657-067691f74c1d)
<br>
5. Webapp: ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/b7547636-1f05-4b70-b16c-bfb2ca40958b)



