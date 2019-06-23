import numpy as np

states = ["hongerig","tevreden","opgejaagd"]
transitionName = [["HH","HT","HO"],["TH","TT","TO"],["OH","OT","OO"]]
transitionMatrix = [[0.8,0.1,0.1],[0.4,0.5,0.1],[0.6,0.2,0.2]]

def activity_forecast(days):
    # begin van de staat
    activityToday = "hongerig"
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "hongerig":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "HH":
                prob = prob * 0.8
                activityList.append("hongerig")
                pass
            elif change == "HT":
                prob = prob * 0.1
                activityToday = "tevreden"
                activityList.append("tevreden")
            else:
                prob = prob * 0.1
                activityToday = "opgejaagd"
                activityList.append("opgejaagd")
        elif activityToday == "tevreden":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "TT":
                prob = prob * 0.5
                activityList.append("tevreden")
                pass
            elif change == "TH":
                prob = prob * 0.4
                activityToday = "hongerig"
                activityList.append("hongerig")
            else:
                prob = prob * 0.1
                activityToday = "opgejaagd"
                activityList.append("opgejaagd")
        elif activityToday == "opgejaagd":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "OO":
                prob = prob * 0.2
                activityList.append("opgejaagd")
                pass
            elif change == "OH":
                prob = prob * 0.6
                activityToday = "hongerig"
                activityList.append("hongerig")
            else:
                prob = prob * 0.2
                activityToday = "tevreden"
                activityList.append("tevreden")
        i += 1
    return activityList

list_activity = []
count = 0

for iterations in range(1,10000):
        list_activity.append(activity_forecast(2))

# eind van de staat
for smaller_list in list_activity:
    if(smaller_list[2] == "hongerig"):
        count += 1

percentage = (count/10000) * 100
print("The probability of starting at state:'' and ending at state:''= " + str(percentage) + "%")
