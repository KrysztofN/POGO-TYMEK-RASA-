# POGO-TYMEK-RASA
Pogo-Tymek (Polish RASA weather bot)

Weather Bot that supports over 200 000 cities worldwide.
<br><br>

**DESCRIPTION**
<br>

**How does it work?**
<br><br>
1. Accept Terms of usage
2. Enter city name
3. Enter a date
4. Get the weather
<br><br>
Good to know...
- Commands: /restart (restarts conversation with the bot),  /hej (starts the conversation)
- Bot accepts date formats specified in the date_check.py file
- Bot can recognize variues cities (including vast majority of polish ones), corrects small typos
- Issues with running multiple questions to the bot, sometimes gives an unexpected result
<br><br>

How to use?
<br>
1. Create an account on https://openweathermap.org/appid
2. Download your api_key and in directory actions paste it inside api_key variable
3. Install all neccessary libraries
4. Open rasa project and in terminal navigate to rasa project directory
5. Train the model: rasa train
6. To start Chat with the bot type: rasa run && rasa run actions 
7. Wait for the bot model to load and start chatting ;)

<br><br>
How to use website with the bot?
<br>
1. Open rasa project and in terminal navigate to rasa project directory
2. In terminal run: rasa run && rasa run actions
3. Navigate to app.py and run
4. Open localhost on port 3000
5. Talk to the bot ;)

<br><br>
**How to use rasa with telegram?**
<br>
1. Instal ngrok: https://ngrok.com/download
2. Open ngrok and type: ngrok http 5005
3. In ngrok copy the "Forwarding" address
4. Go to Bot Father in telegram : https://telegram.me/BotFather
5. Follow further steps described here: https://rasa.com/docs/rasa/connectors/telegram/
6. In credentials.yml specify access_token and verify, which will be given by BotFather during the creation of your bot
7. From step 2 copy the forwarding address into: http://your_forwarding_address/webhooks/telegram/webhook
8. In terminal type: rasa run --enable-api --cors "*" --debug && rasa run actions
9. Open your created telegram bot and start a conversation.
10. You're now able to talk to the bot via telegram

<br><br>
**Debugging:**
<br>
1. If you have problems with getting internal server error when you try to run your telegram bot
2. Try to type in terminal: pip install -U aiogram==2.25.2.
3. If that didn't help try to upgrade rasa and again aiogram. <br><br> ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/de2de1ea-0bcd-43de-8017-4b2c6e380a83)
5. In ngrok you should see this: <br><br> ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/517e2bad-0120-4d4a-8f6d-a8945b20e18f)

<br><br>
**Pogo-Tymek in action:**
<br>
1. **Telegram private conversation:**<br><br> ![one](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/dd2501db-3ce1-4414-bce9-792bc23d1cdd) <br>
2. **Telegram Channel:**<br><br> ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/1725f4f4-a820-43ee-b657-067691f74c1d) <br>
3. **Webapp:**<br><br> ![image](https://github.com/KrysztofN/POGO-TYMEK-RASA-/assets/149100411/b7547636-1f05-4b70-b16c-bfb2ca40958b) <br>



