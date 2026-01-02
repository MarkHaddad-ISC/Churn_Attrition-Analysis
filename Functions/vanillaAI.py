import requests
import time



def vanillaChatBot(inputString, systemPrompt, model, retries=3, delay=61):
    url = 'https://copilot.moodys.com/api/v2/usecases/defaults/chat'
    headers = {
        'x-api-client': ENV_API_CLIENT,
        'x-api-key': ENV_API_KEY,
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
