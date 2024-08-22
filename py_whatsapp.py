#import libraries
import pywhatkit as kit
from openai import OpenAI
import time


#connect and get message from openai

#set your Openai key

api_key = ''

client = OpenAI(api_key=api_key)

def generate_message(prompt):
    """
    Generate a message using OpenAI's GPT model based on the provided prompt.
    """
    completion = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "user", "content": prompt},
  ]
)
    return completion.choices[0].message.content.strip()

#send message to whatsapp
def send_whatsapp_message(phone_number, message):
    """
    Send a Whatsapp message
    """
    kit.sendwhatmsg_instantly(phone_no=phone_number, message=message)
    print(f"Message sent to {phone_number}")


#test
prompt = "Compose a very lovely message to my wife on her birthday"
message = generate_message(prompt)
send_whatsapp_message(phone_number,message)
print('done')