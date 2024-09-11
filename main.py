import telebot

def img(m):
  import requests,time

  url = "https://api.prodia.com/v1/sd/generate"

  payload = {
      "model": "dreamshaper_8.safetensors [9d40847d]",
      "prompt": m ,
      "negative_prompt": "(worst quality, low quality:1.4), (jpeg artifacts:1.4),greyscale, monochrome, motion blur, emphasis lines, text, title, logo, signature,censored, 3d,patreon username, patreon logo, artist name, watermark, extra fingers, bad fingers,male"

  }
  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "X-Prodia-Key": "4d012f3f-13f7-4a92-b1f6-ac0e65002803"
  }

  try:response = requests.post(url, json=payload, headers=headers,timeout=10)
  except:
    return None
  for ij in range(30):
    try:
      time.sleep(1)
      url = "https://api.prodia.com/v1/job/"+response.json()["job"]

      headers = {
          "accept": "application/json",
          "X-Prodia-Key": "4d012f3f-13f7-4a92-b1f6-ac0e65002803"
      }

      response = requests.get(url, headers=headers,, timeout=10)

      im = response.json()["imageUrl"]
      return im
    except:pass
   return None   
API_TOKEN = '7237066851:AAHaI3EXTlA_1ozw4Zk6THme5AAfjkHx0Co'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "/start":
        bot.reply_to(message, "ok")
    else:
      image = img(message.text)
      if image == None:
        bot.reply_to(message, "None!")
      else:  
        chat_id = message.chat.id
        bot.send_photo(chat_id, image)


bot.polling()
