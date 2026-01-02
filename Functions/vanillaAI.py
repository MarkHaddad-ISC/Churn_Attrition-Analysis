import requests
import time



def vanillaChatBot(inputString, systemPrompt, model, retries=3, delay=61):
    url = 'https://copilot.moodys.com/api/v2/usecases/defaults/chat'
    headers = {
        #'x-api-client': '989ea82f-ec30-4d83-870b-40dd1325d32e',
        #'x-api-key': '8ec2fdbd92ad0921daee58609358b274f193b564db1ad6f40f5ce5a436aafbc8',
        'x-api-client': 'e26c5beb-28c1-4158-9568-68206377c533',
        'x-api-key': 'f6927db9dd9322fbf7961e725660a5a6cc30be407da1d0a7523314126d12444a',
        'genai_token': ''
    }
    body = {
      "messages": [
        {
          "role": "system",
          "content": systemPrompt
        },
        {
          "role": "user",
          "content": inputString
        }
      ],
      "model": model
    }


    for attempt in range(retries):
      response = requests.post(url, headers=headers, json=body)

      if response.status_code == 200:
        for item in response.json()['data']:
          content = item['message']['content']
        return content
      else:
        print(f"Attempt {attempt + 1} failed with status code {response.status_code}. Retrying in {delay} seconds...")
        #print(response.json()['message'])
        time.sleep(delay)

    #change this back to return None for other appilcations
    return '["try again", 2,"try again, server issue most likely"]'




    response = requests.post(url, headers=headers, json=body)

    print(response.status_code)

    #print('the copilot API: ' + str(response.json()['data']))

    for item in response.json()['data']:
        content = item['message']['content']
    
    return content