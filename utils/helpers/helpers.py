import threading

def message_change(component_message, text):

    def get_message(message):
        message["text"] = ""
        return message["text"]

    def get_message_error(message):
       return message["text"]

    component_message["text"] = text
    timer = threading.Timer(1.5, lambda :  get_message(component_message))
    timer.start()
    timer2 = threading.Timer(1.5,  lambda : get_message_error(component_message))
    timer2.start()