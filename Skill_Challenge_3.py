class Contact:
    def __init__(self, name, last_name, phone_number=None, email=None, display_mode='masked'):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if (self.email != None and self.email == other.email) or (self.phone_number != None and self.phone_number == other.phone_number):
            return True
        
        return self.name == other.name and self.last_name == other.last_name
    
    @staticmethod
    def _obfuscate(text):
        half_length = len(text) // 2
        return text[:half_length] + '*' * (half_length + 1)
        
    def __repr__(self):
        if self.display_mode == 'masked':
            return f"Contact(name ='{self._obfuscate(self.name)}', last_name='{self._obfuscate(self.last_name)}')"

        return f"Contact(name ='{self.name}', last_name='{self.last_name}', phone='{self.phone_number}', email='{self.email}')"
    
    def __format__(self, format_spec):
        if format_spec != 'masked':
            return f"Contact(name ='{self.name}', last_name='{self.last_name}', phone='{self.phone_number}', email='{self.email}'"

        return repr(self)
        
c1 = Contact("Andy", "Bek")
c2 = Contact("Andy", "Bek", "12345678")
c3 = Contact("Andy", "Bek", "12345678", 'hey@andybek.com')
c4 = Contact("Andy", "Bek", "12345678", 'hey@andybek.com', display_mode='unmasked')

print(c1)
print(c2)
print(c3)
print(c4)