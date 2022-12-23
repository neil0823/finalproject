import weather
from transitions.extensions import GraphMachine

from utils import send_text_message



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "weather"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "rain"
    
    def is_going_to_state3(self, event):
        text = event.message.text  
        return text.lower() == "temperature"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        replyMessage = weather.get_data1()
        send_text_message(reply_token, replyMessage)
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        replyMessage = weather.get_data2()
        send_text_message(reply_token, replyMessage)
        self.go_back()
        

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        replyMessage = weather.get_data3()
        send_text_message(reply_token, replyMessage)
        self.go_back()
    
    def on_exit_state3(self):
        print("Leaving state3")     