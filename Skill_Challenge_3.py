class Contact:
    def __init__(self, name, last_name, phone_number=None, email=None, display_mode='masked'):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if self.email != None and self.phone_number != None:
            return self.phone_number == other.phone_number or self.email == other.email
        elif self.name !=None and self.last_name != None:
            return self.name == other.name or self.last_name == other.last_name
        
    def __repr__(self):
        if self.display_mode == 'masked':
            string1 = "First Name:" + {self.name[:2]} + '*' * {len(self.name) - 2} + '&' + 'Last name: ' + {self.last_name[:2]} + '*' * {len(self.last_name) - 2}
            return string1
        else:
            string1 = "First Name:" + {self.name} + '& Last Name:' + {self.last_name}
            return string1
    
    def __str__(self):
        return "" + self.last_name[:len(self.last_name) - 2] + "" + self.name[:len(self.name) - 3]
    
    def __format__(self, format_spec):
        if format_spec == 'masked':
            pass
        else:
            string1 = "First Name: " + {self.name} +' & Last Name:' + {self.last_name}
            return string1
        
c1 = Contact("Andy", "Bek")
c2 = Contact("Andy", "Bek", "12345678")
c3 = Contact("Andy", "Bek", "12345678", 'hey@andybek.com')
c4 = Contact("Andy", "Bek", "12345678", 'hey@andybek.com', display_mode='show')

print(c1)
print(c2)
print(c3)
print(c4)