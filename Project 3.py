# AI ChatBot PyCode - ไปโค้ด (Simple)
# --> 1. Database --> != OpenAi --> DIY DB
# --> 2. Loops for live chat --> While
# --> 3. Condition for select answer from database
# --> 4. Advance function --> Google Search, Google Map, Youtube,  Text to Speech (Project III)
# --> 5. Test And Fix

import random
import webbrowser
import pyttsx3


response = {
        "hi": ["Salamarekum", "Sup bro", "Hey!", "Hello", ":)"],
        "how are you?": ["Im fine ;)", "im good, are you?", "good", "im good"],
        "bye": ["where you go?", "ok :(", "bye!", "see you soon", "hope you enjoy your day"],
        "need help": ["how im can help you", "what problem sir", "Yes i can", "Your welcome", "tell me"],
        "thankyou": ["No problem sir", "Your welcome", "Sure", "THAT EASY", "YOU NEED TO PAID"],
        "google": ["let's search", "On my way", "Travel", "Find", "GO GO GO"],
        "map": ["Location", "Fine Located", "Go to point", "Make direction", "Go went home"],
        "youtube": ["Okay", "Let's open", "Sure", "Open now", "ok"]
}

engine = pyttsx3.init()


while True:
    user_input = str(input("User Text:"))

    if user_input.lower() == "exit":
            print("Thank you")
            engine.say("Thankyou")
            engine.runAndWait()
            break
    
    for key in response:
          if key in user_input.lower():
                if key == "hi":
                      chatbot = random.choice(response[key])
                      engine.say(chatbot)
                      engine.runAndWait()


                elif key == "how are you?":
                      chatbot = random.choice(response[key])
                      engine.say(chatbot)
                      engine.runAndWait()


                elif key == "bye":
                      chatbot = random.choice(response[key])
                      engine.say(chatbot)
                      engine.runAndWait()


                elif key == "need help":
                      chatbot = random.choice(response[key])
                      engine.say(chatbot)
                      engine.runAndWait()


                elif key == "thankyou":
                      chatbot = random.choice(response[key])
                      engine.say(chatbot)
                      engine.runAndWait()
                      

                elif key == "google": ## Change 1 --> map,youtube
                      chatbot = random.choice(response[key])
                      print("Bot answer:" + " " + chatbot)
                      engine.say("Bot answer" + " " + chatbot)
                      engine.runAndWait

                      query = input("Enter your search in google:") ## Change 2 --> Strings
                      engine.say("Enter your Search in google")
                      engine.runAndWait

                      print("Bot Opening" + " " + query)
                      engine.say("Bot Opening" + " " + query)
                      engine.runAndWait


                      search_url = "https://www.google.com/search?q=" + query.replace(" ", "+") ## Change 3 --> URL
                      webbrowser.open(search_url)

            
                elif key == "map":
                      chatbot = random.choice(response[key])
                      print("Bot answer:" + " " + chatbot)
                      engine.say("Bot answer" + " " + chatbot)
                      engine.runAndWait

                      query = input("Enter your search in google map:")
                      engine.say("Enter Your search in google map")
                      engine.runAndWait

                      print("Bot Opening" + " " + query)
                      engine.say("Bot Opening" + " " + query)
                      engine.runAndWait

                      search_url = "https://www.google.com/maps/search/" + query.replace(" ", "+")
                      webbrowser.open(search_url)


                elif key == "youtube":
                      chatbot = random.choice(response[key])
                      print("Bot answer:" + " " + chatbot)
                      engine.say("Bot answer:" + " " + chatbot)
                      engine.runAndWait

                      query = input("Enter your search in Youtube:")
                      engine.say("Enter your search in Youtube")
                      engine.runAndWait
                
                      print("Bot Opening" + " " + query)
                      engine.say("Bot Opening" + " " + query)
                      engine.runAndWait

                      search_url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
                      webbrowser.open(search_url)


                print("Bot answer:" + " " + chatbot)
                break
    else:
          print("Bot answer:" + " " + "Please Try again")
