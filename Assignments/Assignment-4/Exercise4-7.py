def computegrade(score):
    try:
        score = float(score)
    except:
        print("Bad Score")
        quit()
    if score > 1.0:
        print("Bad Score")
        quit()
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

score = input("Enter Score: ")
computegrade(score)