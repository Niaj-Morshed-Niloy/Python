#Write a class Trail which has methods to book a
#  ticket,get status (no of seats) and get fare 
# information of train running under indian railways.

from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no:{self.trainNo} is running on time.")

    def getfare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}")

t=Train(12339)
t.book("Mumbai","Delhi")
t.getstatus()
t.getfare("Mumbai","Kolkata")