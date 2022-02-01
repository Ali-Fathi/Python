# # 2-3 Personal Message
# name = "Eric"
# print(f"Hello {name}, would like to learn some Python today?")

# # 2-4 Name Cases
# name = "Eric"
# print(f"{name}!".title())
# print(f"{name}!".upper())
# print(f"{name}!".lower())

# # 2-5 Famous Quote
# author = "Nelson Mendala"
# quote = "Education is the most powerful weapon which you can use to change the world."
# print(f"{author} once said, {quote}")

# # 2 - 6
# famous_person = "Nelson Mendala"
# message = "Education is the most powerful weapon which you can use to change the world."
# print(f"{famous_person} once said, {message}")

# # 2 -8 
# print(2 + 6)
# print(10 - 2)
# print(16 / 2)
# print(2 * 4)

# 2 - 9 Favorite Number
#favorite_number = 9
#message = f"My favorite number is {favorite_number}!"
#print(message)

# 3-1 Names
#names = ["Jim", "Kim", "Ben", "Jen"]
#print(names[0])
#print(names[1])
#print(names[2])
#print(names[3])

#  3-2 Greetings
#print(f"Hello {names[0]}.")
#print(f"Hello {names[1]}.")
#print(f"Hello {names[2]}.")
#print(f"Hello {names[3]}.")

# 3-3 Your own list
#wish_list = ["Mercedes AMG", "Nice house", "MD"]
#print(f"One day I will own {wish_list[0]}.")
#print(f"One day I will own {wish_list[1]}.")
#print(f"One day I will be {wish_list[2]}.")

# 3-4 Guess List
# guess_list = ['Jim', 'Kim', 'Ben', 'Jen']
# print(f"Hello {guess_list[0].title()}!\nYou are Invited to the party.")
# print(f"Hello {guess_list[1].title()}!\nYou are Invited to the party.")
# print(f"Hello {guess_list[2].title()}!\nYou are Invited to the party.")
# print(f"Hello {guess_list[3].title()}!\nYou are Invited to the party.")


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

# guess_list = ['Jim', 'Kim', 'Ben', 'Jen']
# print(guess_list)
# # replace jim with jimmy
# guess_list[0] = "Jimmy"
# print(guess_list)

# #3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

from mimetypes import guess_type


guess_list = ['Jim', 'Kim', 'Ben', 'Jen']
# print(guess_list)
# replace jim with jimmy
guess_list[0] = "Jimmy"
# print(guess_list)
guess_list.insert(0, 'Jimmo')
# print(guess_list)
guess_list.insert(3, "Jenny")
# print(guess_list)
guess_list.append('Kimmy')
# print(guess_list)

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
print(len(guess_list))
guess_list.pop()
print(guess_list, len(guess_list))
guess_list.pop()
guess_list.pop()
guess_list.pop()
guess_list.pop()
print(guess_list, len(guess_list))
del guess_list[0:2]
# del guess_list[0]
print(guess_list, len(guess_list))