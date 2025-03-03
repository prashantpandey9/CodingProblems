"""Polymorphism is the ability of an object to take on multiple forms.
"""

class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement this")


class PDF(Document):
    def show(self):
        print("PDF")
        
        
class Word(Document):
    def show(self):
        print("WORD")

docs = [PDF(), Word()]
for i in docs:
    i.show()