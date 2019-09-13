import time
from OSA import OSA

# Get a basic notification
OSA().notify("Notification title", "Notification text")
time.sleep(2)
# Clear all notifications
OSA().clear_notifications()

# Prompt for an option inside a dialog list
OSA().dropdown_list_prompt("Favorite ice cream?", ["Chocolate","Vanilla","Strawberry"])

# Prompt for a text input
OSA().text_prompt("What is the temperature?")

# Get input with hidden text
OSA().password_prompt("What is your passphrase?")

# Get a notification box
OSA().notification_box("It's been four hours! Time to stop working!")
