#this program should be a platform for aspiring engineers to network with each other
#the input is going to be what the user name is and what their password should be
#the output should be whatever the user asks for or if they answer a question that we give them
#This program/Social Media App is called Bridge

#import turtle
import math

class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.bridges = []

    def addBridge(self, bridge_id):
        self.bridges.append(bridge_id)

    def getUserName(self):
        return self.user_name

    def getBridges(self):
        return self.bridges

    def getUserID(self):
        return self.user_id

class Network:
    def __init__(self):
        self.users = []

    def numUsers(self):
        return len(self.users)

    def addUser(self, username):
        for user in self.users:
            if username == user.getUserName():
                print("Sorry, that name is taken. Try again.")
                return
        #If username wasn't taken, add user to the network
        user_id = len(self.users)
        self.users.append(User(username, user_id))

    def getUserID(self, username):
        user_id = -1
        for user in self.users:
            if username == user.getUserName():
                user_id = user.getUserID()
        return user_id                          #If user_id = -1, that means that the username is not there

    def addBridge(self, user1, user2):      #connections are both ways in this program
        user1_id = self.getUserID(user1)
        user2_id = self.getUserID(user2)

        user1 = self.users[user1_id]
        user2 = self.users[user2_id]

        if user1_id == -1 or user2_id == -1:
            print("Sorry, one or more username is not correct. Try again.")
            return False                           #Failure, one or other username is wrong
        elif user1_id == user2_id:
            print("Sorry, connections must be between two different users. Try again.")
            return False
        elif user2_id in user1.getBridges(): #They're already friends
            print("{} and {} are already connected!".format(user1.getUserName(), user2.getUserName()))
            return True
        else:
            #self.users[user1_id].addBridges(user2_id)
            self.users[user2_id].addBridge(user1_id)
            return True                               #Success

    def printUsers(self):
        print("Network Users:")
        for user in self.users:
            print("\tUser {}: {}".format(user.getUserID(), user.getUserName()))

    def printBridges(self, username):
        user = self.users[self.getUserID(username)]
        bridges = user.getBridges()
        print("{}'s bridges:".format(user.getUserName()))
        for friendID in bridges:
            friend = self.users[friendID]
            print("\t{}".format(friend.getUserName()))

def main():
    mynetwork = Network()
    done = False
    print("Welcome to Bridge, the blueprint for your future. This platform is the perfect place for aspiring engineers to get started in the industry!")
    while not done:
        action = input("""\nTo add a username and bio, press 'u.' To see all users, press 'p.'
        To create a bridge, press 'b.' To see all bridges, press 'pb.'To exit, press 'e.'""")
        if action == "p":
            mynetwork.printUsers()
        elif action == "u":
            username = input("What username? ")
            mynetwork.addUser(username)
        elif action == "pb":
            user = input("For which user? ")
            mynetwork.printBridges(user)
        elif action == "b":
            if mynetwork.numUsers() < 2:
                print("You need at least two users to make a bridge.")
                continue
            user1 = input("First username: ")
            user2 = input("Second username: ")
            #mynetwork.addBridge(user1, user2)
        elif action == "e":
            print("Sorry to see you go so soon!")
            break
        else:
            print("Sorry, I didn't understand that.")

if __name__ == '__main__':
    #main()
    #define the program flow for the user interface
