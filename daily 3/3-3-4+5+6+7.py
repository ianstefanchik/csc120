#3-3-4
guest_list = ["Tiger Woods", "Justin Thomas", "Rory McIlroy", "Jordan Spieth"]

message_one = f"Hi {guest_list[0]}, you are invited to a dinner party on January 24!\n"
message_two = f"Hi {guest_list[1]}, you are invited to a dinner party on January 24!\n"
message_three = f"Hi {guest_list[2]}, you are invited to a dinner party on January 24!\n"
message_four = f"Hi {guest_list[3]}, you are invited to a dinner party on January 24!\n"

print(message_one, message_two, message_three, message_four)

#3-3-5

print(f"Unfortunately, {guest_list[2]} can't make it to the dinner party.")

guest_list[2] = "Phil Mickelson"

message_one = f"Hi {guest_list[0]}, you are invited to a dinner party on January 24!\n"
message_two = f"Hi {guest_list[1]}, you are invited to a dinner party on January 24!\n"
message_three = f"Hi {guest_list[2]}, you are invited to a dinner party on January 24!\n"
message_four = f"Hi {guest_list[3]}, you are invited to a dinner party on January 24!\n"

#3-3-6
print("Hello everyone, we have found a bigger dinner table, so there will be more guests attending.")

guest_list.insert(0, "Jack Nicklaus")
guest_list.insert(2, "Arnold Palmer")
guest_list.append("Bryson DeChambeau")

message_one = f"Hi {guest_list[0]}, you are invited to a dinner party on January 24!\n"
message_two = f"Hi {guest_list[1]}, you are invited to a dinner party on January 24!\n"
message_three = f"Hi {guest_list[2]}, you are invited to a dinner party on January 24!\n"
message_four = f"Hi {guest_list[3]}, you are invited to a dinner party on January 24!\n"
message_five = f"Hi {guest_list[4]}, you are invited to a dinner party on January 24!\n"
message_six = f"Hi {guest_list[5]}, you are invited to a dinner party on January 24!\n"
message_seven = f"Hi {guest_list[6]}, you are invited to a dinner party on January 24!\n"

print(message_one, message_two, message_three, message_four, message_five, message_six, message_seven)

#3-3-7
print("We just found out that the bigger dinner table will not make it on time. We can only invite 2 guests.")

remove_guest = guest_list.pop()

print(f"Sorry {remove_guest}, but we do not have enough room for you at the dinner party.")

remove_guest = guest_list.pop()

print(f"Sorry {remove_guest}, but we do not have enough room for you at the dinner party.")

remove_guest = guest_list.pop()

print(f"Sorry {remove_guest}, but we do not have enough room for you at the dinner party.")

remove_guest = guest_list.pop()

print(f"Sorry {remove_guest}, but we do not have enough room for you at the dinner party.")

remove_guest = guest_list.pop()

print(f"Sorry {remove_guest}, but we do not have enough room for you at the dinner party.")

print(f"Hi {guest_list[0]}, you are still invited to the dinner party.")
print(f"Hi {guest_list[1]}, you are still invited to the dinner party.")

del guest_list[-1]
del guest_list[0]

print(guest_list)