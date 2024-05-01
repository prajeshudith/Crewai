# Using Inference API
import requests
import config
from textwrap import dedent

class Mask_PII:
    def __init__(self,text):
        self.text = text

    def query(self,payload):
        response = requests.post(config.API_URL, headers=config.headers, json=payload)
        return response.json()

    def request(self,prompt: str) -> str:  
        output = self.query(
            {
                "inputs": prompt,
            }
        )
        print(*output,sep='\n')
        return output

    def create_entity_map(self,text):
        model_output = self.request(text)
        entity_map = {}
        for token in model_output:
            start = token["start"]
            end = token["end"]
            entity = text[start: end]
            entity_map[entity] = token["entity_group"]
        print(entity_map)
        return entity_map

    def __call__(self):
        entity_map = self.create_entity_map(self.text)
        unmasked_text = self.text
        for word in entity_map:
            if word in unmasked_text:
                unmasked_text = unmasked_text.replace(word, f"[{entity_map[word]}]")
        #print(text)
        return unmasked_text

text = dedent("""My name is Sarah Jessica Parker but you can call me Jessica. My mobile number is 9600143355, username is praju_s and 
        my password is aab@123""")
output = Mask_PII(text=text)()
print(output)