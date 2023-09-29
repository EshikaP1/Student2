from emoji import emojize 
print(emojize(":thumbs_up: Python is awesome! :grinning_face:"))  
heart_emoji = emojize(":heart:", use_aliases=True)
print(heart_emoji)
print(":sadface:")