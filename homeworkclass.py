class books:
    def __init__(self, author, subject, colour, size, amount):
        self.author = author
        self.subject = subject
        self.colour = colour
        self.size = size
        self.amount = amount

    #Getters function
    def getauthor(self):
        return self.author

    #Setters
    def setsubject(self,newsubject):
        self.setsubject= newsubject

    def increase_amount(self):
        self.amount = self.amount + 1
        print(self.amount)

    def showbooks(self):
        print(f"This book has {self.author} as the author, {self.subject} as the subject of the book, it is {self.colour} in colour, is {self.size} in size, and {self.amount} can be bought under $100")

GiftedHands = books("Ben Carson", "motivation", "black", "medium", 6)
GiftedHands.showbooks()
GiftedHands.increase_amount()
GiftedHands.setsubject("mathematics")
GiftedHands.showbooks()