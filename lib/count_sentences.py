#!/usr/bin/env python3

class MyString:
    
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        word = [letters for letters in self.value]
        if word[-1] == ".":
            return True
        else:
            return False
        
    def is_question(self):
        word = [letters for letters in self.value]
        if word[-1] == "?":
            return True
        else:
            return False
    
    def is_exclamation(self):
        word = [letters for letters in self.value]
        if word[-1] == "!":
            return True
        else:
            return False
        
    def count_sentences(self):
      value = self.value
      for punc in ['!','?']:
        value = value.replace(punc, '.')
    
      sentences = [s for s in value.split('.') if s]
    
      return len(sentences)
      
