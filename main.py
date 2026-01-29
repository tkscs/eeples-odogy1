song = input("What is your original sentence: ")

varible_i_got_no_name_ideas2 = input("How many times do you want each character to multiply: ")
varible_i_got_no_name_ideas3 = int(varible_i_got_no_name_ideas2)
song2 = ""
rep = input("What do you want to replace: ")
t1 = input("What is the first thing you want to replace it with? ")
t2 = input("What is the second thing you want to replace it with? ")
t3 = input("What is the third thing you want to replace it with? ")
t4 = input("What is the fourth thing you want to replace it with? ")
t5 = input("What is the fith thing you want to replace it with? ")






def sing():
    print(song)
    print(song.replace(rep, t1))
    print(song.replace(rep, t2))
    print(song.replace(rep, t3))
    print(song.replace(rep, t4))
    print(song.replace(rep, t5))

sing()

for character in song:
    song2 = song2 + character*varible_i_got_no_name_ideas3

print(song2)
#I like to eat, eat, eat, apples and bananas.