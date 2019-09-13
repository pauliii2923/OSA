import os
import subprocess

class OSA:
  def clear_notifications(self):
    os.system("""osascript -e 'tell application "System Events"' -e 'tell process "NotificationCenter"' -e 'set numwins to (count windows)' -e 'repeat with i from numwins to 1 by -1' -e 'try' -e 'click button "Close" of window i' -e 'end try' -e 'end repeat' -e 'end tell' -e 'end tell' &> /dev/null &""")
  
  def notify(self, title, text):
    os.system("""osascript -e 'display notification "{}" with title "{}" sound name "default"' """.format(text.replace("'","’").replace('"',"“"),title.replace("'","’").replace('"',"“")))
  
  def dropdown_list_prompt(self, query, options):
    option_list = ",".join(list(map(lambda i:('"%s"'%i.replace("'","’").replace('"',"“").replace(",","，")),options)))
    return subprocess.check_output("""osascript -e 'tell application (path to frontmost application as text)' -e 'with timeout of 30000 seconds -- wait 500 minutes' -e 'choose from list {%s} with prompt "%s"' -e 'end timeout' -e 'end tell'"""%(option_list,query.replace("'","’").replace('"',"“")),shell=True).decode()[:-1]
  
  def text_prompt(self, query):
    return subprocess.check_output("""osascript -e 'tell application (path to frontmost application as text)' -e 'with timeout of 30000 seconds -- wait 500 minutes' -e 'display dialog "%s" default answer "" buttons {"Ok"} ' -e 'end timeout' -e 'end tell'"""%(query.replace("'","’").replace('"',"“")),shell=True).decode()[:-1].split("text returned:")[1]
  
  def password_prompt(self, query):
    return subprocess.check_output("""osascript -e 'tell application (path to frontmost application as text)' -e 'with timeout of 30000 seconds -- wait 500 minutes' -e 'display dialog "%s" default answer "" buttons {"Ok"} with hidden answer' -e 'end timeout' -e 'end tell'"""%(query.replace("'","’").replace('"',"“")),shell=True).decode()[:-1].split("text returned:")[1]
  
  def notification_box(self, notification_text):
    os.system("""osascript -e 'tell application (path to frontmost application as text)' -e 'with timeout of 30000 seconds -- wait 500 minutes' -e 'display dialog "%s" buttons {"Ok"}' -e 'end timeout' -e 'end tell'"""%(notification_text.replace("'","’").replace('"',"“")))



