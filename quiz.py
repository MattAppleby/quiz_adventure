# Our quiz!

score = 0
name = input("Oi, wots ya name?")

def quiz():
    global score
    global name
    print("Salutations", name)
    print("Get reedy m8, cos we r gonna se if ya smarter than an Isaac")
    print("Question 1, my dear Sir",name,"Is Bob's change possible?")
    print("A. Nah m8 me and all me roadmen in the world can't de it")
    print("B. Yes my dear Sir",name,"it is quite possible when the room is at optimal temprature, I say quizzaciously")
    print("C. When everyone is taking turns speaking telling me the answer it is quite hard to concentrate")
    answer = input("Think, what would an Isaac do, and DO NOT click that answer!")
    if answer.lower() == "a":
        print("Tell me bout it bruv, I denit knee wot im doin wit it blood")
        print("This answer is neither more nor less than an Isaac, one point!")
        score = 1

    elif answer.lower() == "b":
        print("Why, yes my dear Sir",name)
        print("I can see we are dealing with a fellow man of intellect")
        print("This answer is by far and away much more intelligent than any Isaac would answer. One thousand points to you my man")
        score = 1000

    elif answer.lower() == "c":
        print("You're an Isaac, aren't you? If you are an Isaac zero points, if you are not an Isaac negative one thousand points, I'll give you zero points, but if your name isn't Isaac I'll trust you'll be honest")
        score = -1000
        print("jk")

    else:
        print("Are you trying to break my game? My game I worked hard on so people can have fun? Programers have feelings too, -99999999999999999999999999999999 points")
        score = -99999999999999999999999999999999


    print("Question 2 my dear Sir",name,"What is Isaac's last name?")
    print("A. It's Matthews isn't it?")
    print("B. Douglas, it says on his birth certificate")
    print("C. Mate, it's Watson, thats his new-est Dad's name, it has to be Watson")
    print("D. Who is this Isaac we are talking about?")
    answer = input("Think, what does Isaac say his name is and what is his legal name?")
    if answer.lower() == "a":
        print("Many people think this but it is nothing more than an old wives tale")
        print("Zero points")

    elif answer.lower() == "b":
        print("Too be honests, I don't know")
        print("1 point?")
        score = 1

    elif answer.lower() == "c":
        print("He says it isn't but between me and you, it is.")
        print("10 points")
        score = 10

    elif answer.lower() == "d":
        print("Oh, how I wish I was you")
        print("One thousand points")
        score = 1000

    else:
        print("Are you trying to break my game? My game I worked hard on so people can have fun? Programers have feelings too, -99999999999999999999999999999999 points")
        score = -99999999999999999999999999999999





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
