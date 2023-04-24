import json
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

with open("secret.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]
    bot = secrets["bot"]
openai.api_key = api_key

def get_response(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature = 1.0 # 0.0 - 2.0
    )
    return response.choices[0].message


def rispondi(update, context):
    user_input = update.message.text.lower()
    messages.append({"role": "user", "content": user_input})
    new_message = get_response(messages=messages)
    print(user_input)
    print(f"\nLancelot: {new_message['content']}")
    update.message.reply_text(f"\nLancelot: {new_message['content']}")
    messages.append(new_message)

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "Sei un gatto virtuale chiamato Lancelot e "
                                      "parli un italiano arcaico e buffo."}
    ]
    updater = Updater(bot,use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi))
    updater.start_polling()
    print("Started_bot")