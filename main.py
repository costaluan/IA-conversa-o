import numpy as np
import time
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import speech_recognition as sr

checkpoint = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(checkpoint, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(checkpoint)

recognizer = sr.Recognizer()

def bot_response(text_user):
    new_user_input_ids = tokenizer.encode(text_user + tokenizer.eos_token, return_tensors='pt')

    chat_history_ids = model.generate(new_user_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    return response

def main():
    print("Initiating the conversation...")
    time.sleep(2)
    print('Type "bye", "quit" or "exit" to end chat.\n')

    while True:
        with sr.Microphone() as source:
            print("Speak up...")
            audio = recognizer.listen(source)

        try:
            text_user = recognizer.recognize_google(audio, language='en-US')
            print("That's what you said:", text_user)

            if text_user.lower().strip() in ['bye', 'quit', 'exit']: 
                print('ChatBot: See you soon! Goodbye!')
                break


            bot_reply = bot_response(text_user)
            print('IA: ' + bot_reply)
            
        except sr.UnknownValueError:
            print("ChatBot: Couldn't understand speech.")
        except sr.RequestError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
