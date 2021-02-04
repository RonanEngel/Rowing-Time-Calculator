start = input("Logging Data or Getting Info(Log/Get): ")
SPMLst = []
PaceLst = []
SPMsum = 0
Pacesum = 0


def avg_pace_recall(GetLst, Pacesum):
    """
    Will find the Average Pace of a Category in seconds, then convert them to minutes
    :param GetLst: List used
    :param Pacesum:
    :return AvgPace:
    """
    for GetLst2 in GetLst:
        IndvLst = GetLst2.split(" ")
        PaceLst.append((IndvLst)[1])
    for PaceFinal in PaceLst:
        Pacesum += float(PaceFinal)
    PaceAvgSec = float(Pacesum / len(PaceLst))
    if ((float(PaceAvgSec) % 60)) < 10:
        PaceAvg = '{:1.0f}:0{:1.1f}'.format((int(PaceAvgSec) / 60), (float(PaceAvgSec) % 60))
        return PaceAvg
    elif ((float(PaceAvgSec) % 60)) >= 10:
        PaceAvg = '{:1.0f}:{:2.1f}'.format((int(PaceAvgSec) / 60), (float(PaceAvgSec) % 60))
        return PaceAvg


def spm_avg_finder(GetLst, SPMsum):
    """
    Will find the average strokes per minute of a given category
    :param SPMLst:
    :param SumOfSPM:
    :return SPMAvg:
    """
    for GetLst2 in GetLst:
        IndvLst = GetLst2.split(" ")
        SPMLst.append((IndvLst)[2])
    for SPMFinal in SPMLst:
        SPMsum += int(SPMFinal)
    SPMAvg = (int(SPMsum / len(SPMLst)))
    return (SPMAvg)


def AvgPaceConverter(AvgPace):
    """
    Converts AvgPace from minutes to seconds
    :param AvgPace:
    :return new_pace:
    """
    new_pace_lst = AvgPace.split(":")
    new_pace = (float(new_pace_lst[0]) * 60) + float(new_pace_lst[1])
    return new_pace


# Begining of funtioning code that interacts with the user
# Logging Half of Code
if start == 'Log':
    i = 0
    Amount = input("How many times do you have to log: ")
    while i < int(Amount):
        LogCat = input("Category(Aa/A/E): ")
        AvgPace = input("Avg Pace: ")
        Meters = input("Total Meters Traveled: ")
        SPM = input("Average Stokes per Minute: ")
        if LogCat == 'Aa':
            with open('Anaerobic.txt', 'a') as aa:
                aa.write('{} {} {} \n'.format(Meters, AvgPaceConverter(AvgPace), SPM))
        elif LogCat == 'A':
            with open('Aerobic.txt', 'a') as a:
                a.write('{} {} {} \n'.format(Meters, AvgPaceConverter(AvgPace), SPM))
        elif LogCat == 'E':
            with open('Endurance.txt', 'a') as e:
                e.write('{} {} {} \n'.format(Meters, AvgPaceConverter(AvgPace), SPM))
        else:
            print("Category must be:\nAa- Anaerobic\nA - Aerobic\nE - Endurance")
        i = i + 1


# Getting half of code
elif start == 'Get':
    GetCat = input("Category(Aa/A/E): ")
    if GetCat == 'Aa':
        with open('Anaerobic.txt', 'r') as Aa:
            GetLst = Aa.readlines()
            print('Average SPM: ' + str(spm_avg_finder(GetLst, SPMsum)))
            print('Average Pace: ' + avg_pace_recall(GetLst, Pacesum))
    elif GetCat == 'A':
        with open('Aerobic.txt', 'r') as a:
            GetLst = a.readlines()
            print('Average SPM: ' + str(spm_avg_finder(GetLst, SPMsum)))
            print('Average Pace: ' + avg_pace_recall(GetLst, Pacesum))
    elif GetCat == 'E':
        with open('Endurance.txt', 'r') as e:
            GetLst = e.readlines()
            print('Average SPM: ' + str(spm_avg_finder(GetLst, SPMsum)))
            print('Average Pace: ' + avg_pace_recall(GetLst, Pacesum))
    else:
        print("Category must be:\nAa- Anaerobic\nA - Aerobic\nE - Endurance")
