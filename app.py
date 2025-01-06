# Menu of 3 items 
# - Typing Test
# - Leaderboard
# - Exit

# Typing test will put you in a randomly picked sentence for you to type,
# a timer will also start, and end once you finish typing the sentence and 
# display results
import time
import random
def bubble_sort(time_data : list) -> list:
    for n in range(len(time_data) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if time_data[i][0] < time_data[i + 1][0]:
                time_data[i], time_data[i + 1] = time_data[i + 1], time_data[i]
                swapped = True
            if time_data[i][0] == time_data[i + 1][0]:
                if time_data[i][1] > time_data[i + 1][1]:
                    time_data[i], time_data[i + 1] = time_data[i + 1], time_data[i]
                    swapped = True
        if not swapped:
            return time_data               
def menu_screen():
    print("Welcome to your typing test!")
    choice = input("\n1: Take the Test\n2: Leaderboards\n3: Exit\nChoose: ")
    if choice == '1':
        typing_test()
    elif choice == '2':
        leaderboard_times()
    elif choice == '3':
        print("Goodbye!")
    else:
        print("Choose something else!")
        menu_screen()
def leaderboard_times():
    bubble_sort(leaderboard_stats)
    if len(leaderboard_stats) > 0:
        print("\n1st: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[0][0], leaderboard_stats[0][1]))
    if len(leaderboard_stats) > 1:
        print("2nd: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[1][0], leaderboard_stats[1][1]))
    if len(leaderboard_stats) > 2: 
        print("3rd: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[2][0], leaderboard_stats[2][1]))
    if len(leaderboard_stats) > 3:    
        print("4th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[3][0], leaderboard_stats[3][1]))
    if len(leaderboard_stats) > 4:    
        print("5th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[4][0], leaderboard_stats[4][1]))
    if len(leaderboard_stats) > 5:    
        print("6th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[5][0], leaderboard_stats[5][1]))
    if len(leaderboard_stats) > 6:    
        print("7th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[6][0], leaderboard_stats[6][1]))
    if len(leaderboard_stats) > 7:    
        print("8th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[7][0], leaderboard_stats[7][1]))
    if len(leaderboard_stats) > 8:
        print("9th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[8][0], leaderboard_stats[8][1]))
    if len(leaderboard_stats) > 9:  
        print("10th: Accuracy: %.2f | Time: %.2f seconds" % (leaderboard_stats[9][0], leaderboard_stats[9][1]))
    input("\nEnter any key to leave. ")
    menu_screen()
def typing_test() -> list:
    randomizer = random.randint(0, 99)
    errors = 0
    start = time.time()
    typing_sentence = texts[randomizer]
    typing_result = input(typing_sentence + "\n")
    end = time.time()
    total_time = round(end - start, 2)
    if len(typing_result) == len(typing_sentence):
        for i in range(0, len(typing_result)):
            if typing_sentence[i] != typing_result[i]:
                errors += 1
    if len(typing_result) < len(typing_sentence):
        for i in range(0, len(typing_result)):
            if typing_sentence[i] != typing_result[i]:
                errors += 1
        errors = errors + (len(typing_sentence) - len(typing_result))
    if len(typing_result) > len(typing_sentence):
        for i in range(0, len(typing_sentence)):
            if typing_sentence[i] != typing_result[i]:
                errors += 1
        errors = errors + (len(typing_result) - len(typing_sentence))
    accuracy = round(((len(typing_sentence) - errors) / len(typing_sentence) * 100) , 2)
    leaderboard_stats.append([accuracy, total_time])
    print("\nHere are your results!")
    print("Errors: %d" % errors)
    print("Total Time: %.2f seconds" % total_time)
    print("Accuracy: " + str(accuracy) +'%')
    input("Enter any key to leave. ")
    menu_screen()
    return leaderboard_stats
texts = [
    "The quick brown fox jumps over the lazy dog every day.",
    "A journey of a thousand miles begins with a single step.",
    "To be, or not to be, that is the question we're asking.",
    "All that glitters is not gold, and we must be cautious.",
    "In the middle of difficulty lies opportunity and growth.",
    "She sells seashells by the seashore on a sunny morning.",
    "The best way to predict the future is to create it yourself.",
    "It is better to light a candle than to curse the darkness.",
    "A picture is worth a thousand words, but so is a story.",
    "An ounce of prevention is worth a pound of cure, they say.",
    "Time flies over us but leaves its shadow behind always.",
    "Actions speak louder than words, but both matter greatly.",
    "Imagination is more important than knowledge, they say.",
    "Knowledge is power, but wisdom is a guide to success.",
    "Success is not final, failure is not fatal, it's courage.",
    "Life is what happens when you're busy making other plans.",
    "Keep your friends close, but your enemies closer still.",
    "If you want to go fast, go alone. If you want to go far...",
    "When the going gets tough, the tough get going, they say.",
    "Do not go where the path may lead, go instead where there is no path.",
    "Success is not how high you have climbed, but how you.",
    "The harder you work, the luckier you get in the end.",
    "Wisdom begins in wonder, and ends in clarity of thought.",
    "Dream big, work hard, stay focused, and make it happen.",
    "Sometimes the smallest things take up the most room in our hearts.",
    "Happiness depends upon ourselves, not external forces.",
    "Be the change you wish to see in the world around you.",
    "It always seems impossible until it's done, don't give up.",
    "The only way to do great work is to love what you do.",
    "Success is not in what you have, but who you are inside.",
    "The secret of getting ahead is getting started, so begin.",
    "Life is 10% what happens to us and 90%% how we react.",
    "A good friend knows all your best stories, but a best.",
    "Don't wait for the perfect moment, take the moment and make it.",
    "In three words I can sum up everything I've learned about life.",
    "It's not about how bad you want it, it's about how hard.",
    "The only limit to our realization of tomorrow is our doubts.",
    "The pessimist sees difficulty in every opportunity, always.",
    "Life is really simple, but we insist on making it complicated.",
    "Strive not to be a success, but rather to be of value.",
    "The purpose of life is not to be happy, but to be useful.",
    "Challenges are what make life interesting, overcoming them.",
    "It does not matter how slowly you go as long as you do not stop.",
    "The best revenge is massive success, let them wonder.",
    "You miss 100%% of the shots you don't take, take them all.",
    "The mind is everything. What you think you become, always.",
    "Great things never come from comfort zones, step out.",
    "Do what you can, with what you have, where you are now.",
    "Nothing in life is to be feared, it is only to be understood.",
    "You can never cross the ocean until you have the courage.",
    "Life is like riding a bicycle, to keep your balance, keep.",
    "The only way to have a friend is to be one yourself.",
    "Be yourself; everyone else is already taken, just be you.",
    "Hardships often prepare ordinary people for an extraordinary.",
    "The only impossible journey is the one you never begin.",
    "There are no shortcuts to any place worth going, keep moving.",
    "We are what we repeatedly do. Excellence, then, is not an act.",
    "Success is how high you bounce when you hit bottom, always.",
    "Believe you can and you're halfway there, just believe.",
    "The only thing standing between you and your goal is...",
    "We do not remember days, we remember moments, cherish them.",
    "Don't watch the clock; do what it does, keep going forward.",
    "The best way to find yourself is to lose yourself in the service.",
    "What lies behind us and what lies before us are tiny matters.",
    "The journey of a thousand miles begins with one single step.",
    "Try not to become a man of success, but rather a man of value.",
    "Life isn't about waiting for the storm to pass, but learning.",
    "The future belongs to those who believe in the beauty of dreams.",
    "Hard work beats talent when talent doesn't work hard enough.",
    "It's never too late to be what you might have been.",
    "When you arise in the morning think of what a privilege it is.",
    "It's not the years in your life that count, but the life.",
    "You are braver than you believe, stronger than you seem.",
    "The way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today, focus forward.",
    "The only real mistake is the one from which we learn nothing.",
    "Everything has beauty, but not everyone sees it, look closely.",
    "Act as if what you do makes a difference, because it does.",
    "The best time to plant a tree was 20 years ago, plant today.",
    "You cannot swim for new horizons until you have courage.",
    "What you get by achieving your goals is not as important.",
    "When you stop chasing the wrong things, you give the right.",
    "Our lives begin to end the day we become silent about things.",
    "The most difficult thing is the decision to act, the rest.",
    "Never let the fear of striking out keep you from playing.",
    "Success usually comes to those who are too busy to be looking for it.",
    "We become what we think about, think good things always.",
    "Great minds discuss ideas, average minds discuss events.",
    "Do not wait to strike till the iron is hot, but make it hot.",
    "Don't be pushed around by the fears in your mind, control.",
    "The best way to cheer yourself is to try to cheer someone.",
    "Life is not measured by the number of breaths we take.",
    "The only person you are destined to become is the person you decide.",
    "If you don't build your dream, someone will hire you to help.",
    "Success is not the key to happiness, happiness is the key."
]
leaderboard_stats = []
menu_screen()

