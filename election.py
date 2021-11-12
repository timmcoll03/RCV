import pandas as pd
import numpy as np
import math as m


def dataRetrive():
    path = input("Enter the filename:")
    df = pd.read_csv(path)
    df = df.drop(["Name"], axis = 1)
    return df

def checkVotes(results,df):
    if len(df[df.columns[0]])==1:
        result = ("The winner is candidate "+ str(df[df.columns[0]][0]) + " with 1 first-place votes.")
        return [0,result]
    if results[0] >= int(sum(results)/2)+1:
        #print("The winner is candidate "+ str(results.keys()[0] + " with " + str(results[0])+" first-place votes"))
        result = ("The winner is candidate "+ str(results.keys()[0]) + " with " + str(results[0])+" first-place votes.")
        return [0,result]
    elif results[0] == results[1]:
        #print("This election has no winner.")
        result = ("This election has no winner.")
        return [0,result]
    else:
        return [1,""]

def scrub(df):
    for y in range(len(df.columns)-1):
        for x in range(len(df[df.columns[0]])):
            if isinstance(df[df.columns[y]][x], str) != True:
                if m.isnan(df[df.columns[y]][x]) == True:
                    df[df.columns[y]][x] = df[df.columns[y+1]][x]
                    df[df.columns[y+1]][x] = np.NaN

def reRank(results,df):
    for y in range(len(df.columns)-1):
      for x in range(len(df[df.columns[0]])):
        if results.keys()[len(results)-1] == df[df.columns[y]][x]:
              df[df.columns[y]][x] = np.NaN

    for  x in range(len(df.columns)-1):
        scrub(df)

def checkTies(results,df):
    for x in range(len(results)-1):
        if results[len(results)-1] == results[len(results)-1-x]:
            for y in range(len(df[df.columns[0]])):
                for z in range(len(df.columns)):
                    if df[df.columns[z]][y] == results.keys()[len(results)-1-x]:
                        df[df.columns[z]][y] = np.NaN

def cleanResults(df):
    checkFor0Votes(df["Choice 1"].value_counts(),df)

def checkFor0Votes(results, df):
    checkList = []
    for z in range(len(results)):
        checkList.append(results.keys()[z])
    for y in range(len(df.columns)-1):
      for x in range(len(df[df.columns[0]])):
          if df[df.columns[y]][x] not in checkList:
              df[df.columns[y]][x] = np.NaN

    for x in range(len(df.columns)-1):
        scrub(df)


def RCV(df):
    for x in range(len(df.columns)-1):
        results = df["Choice 1"].value_counts()
        cleanResults(df)
        result = checkVotes(results,df)
        if result[0] == 1:
            checkTies(results,df)
            reRank(results,df)
        else:
            return result
        if x == len(df.columns)-2:
            return ("This election has no winner.")
    return result[1]
#1 Call your program 'election.py' before submitting

#
#
# your imports and your functions are up here above main(), like usual
#
#

def main(filename): #2

    # filename = input("Enter your filename: ")  <- #3 delete or comment out this line
    df = pd.read_csv(filename)
    df = df.drop(["Name"], axis = 1)

    return RCV(df)[1]        #4
                             # result needs to be the string that you want to print
                             # which is either "The winner is candidate etc.." or
                             # "This election has no winner."


"""

Some modifications to your program that you must do before submitting:

1. Your program must be called: election.py
2. Your main function must accept filename as a parameter
3. Get rid of the line of code that accepts user input
4. Your main function must return, not print, the appropriate string
5. Remove your call to main()
"""
