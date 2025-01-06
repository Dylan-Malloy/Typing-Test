# Menu of 3 items 
# - Typing Test
# - Leaderboard
# - Exit

# Typing test will put you in a randomly picked sentence for you to type,
# a timer will also start, and end once you finish typing the sentence and 
# display results
import time
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
    errors = 0
    start = time.time()
    typing_sentence = "The quick brown fox jumps over the lazy dog."
    typing_result = input(typing_sentence + "\n")
    end = time.time()
    total_time = round(end - start, 2)
    for i in range(0, len(typing_result)):
        if typing_sentence[i] != typing_result[i]:
            errors += 1
    if len(typing_result) < len(typing_sentence):
        errors = errors + (len(typing_sentence) - len(typing_result))
    if len(typing_result) > len(typing_sentence):
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
leaderboard_stats = []
menu_screen()

