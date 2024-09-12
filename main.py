import telebot

def img(m , g):
  import requests,time

  url = "https://api.prodia.com/v1/sd/generate"

  payload = {
      "model": g,
      "prompt": m ,
      "negative_prompt": "(worst quality, low quality:1.4), (jpeg artifacts:1.4),greyscale, monochrome, motion blur, emphasis lines, text, title, logo, signature,censored, 3d,patreon username, patreon logo, artist name, watermark, extra fingers, bad fingers,male"

  }
  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "X-Prodia-Key": "72b18186-fb64-46a4-b4f2-a91af84dd398"
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

      response = requests.get(url, headers=headers, timeout=10)

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
      p = [
        "aniverse_v30.safetensors [579e6f85]",
        "absolutereality_v181.safetensors [3d9d4d2b]",
        "AOM3A3_orangemixs.safetensors [9600da17]",
        "ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]", "revAnimated_v122.safetensors [3f4fefd9]"
      ]
      for i in p:
        image = img(message.text,i)
        if image == None:
          bot.reply_to(message, "None!")
      else:  
        chat_id = message.chat.id
        bot.send_photo(chat_id, image)


bot.polling()
