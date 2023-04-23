class Phone():
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []        
    
    def call(self, other_phone):
        appel = self.phone_number,"\U0001F4DE a téléphoné",other_phone
        self.call_history.append(appel)
    
 
        
        
    def show_call_history(self):
        for item in self.call_history:
            print(item)
            
            
    
    def send_message(self, other_phone, contenue):
        message_envoyé = {}
        message_envoyé['from'] = self.phone_number
        message_envoyé['to'] = other_phone
        message_envoyé['contenu'] = contenue
        self.messages.append(message_envoyé)
        
        
        message_reçu = {}
        message_reçu['from'] = other_phone
        message_reçu['to'] = self.phone_number
        message_reçu['contenu'] = contenue
        self.messages.append(message_reçu)
        
        
    
    def show_outgoing_messages(self):
        print("show_outgoing_messages")
        for item in self.messages:
            if item["from"] == self.phone_number:
                print(item)
        
        
    def show_incoming_messages(self, other_phone):
        print("show_incoming_messages")
        for item in self.messages:
            if item["to"] == self.phone_number :
                print(item)
        
        
    def show_messages_from(self, other_phone):
        for item in self.messages:
            if (item["to"] == other_phone and item["from"] == self.phone_number):
                print(item)
        
            
b = Phone(20200)
b.call(566875)
b.call(166875)
b.call(266875)
b.show_call_history()
b.send_message(458175, "Rappel moi s'il te plaît")
b.send_message(166875, "préparation pour le dîner de ce soir")
b.send_message(266875, "déménagement")
print(b.messages)
b.show_outgoing_messages()
b = Phone(77758)
b.show_incoming_messages(266875)
b.show_messages_from(166875)
