import pandas as pd
import numpy as np
import math as m 


def dataRetrive():
    path = input("Enter the filename: ")
    df = pd.read_csv(path)
    df = df.drop(["Name"], axis = 1)
    return df

def checkVotes(results):
    print(results)
    if results[0] >= sum(results)/2+1: 
        print("The winner is candidate "+ str(results.keys()[0] + " with " + str(results[0])+" first-place votes"))
        return True
    elif results[0] == results[1]:
        print("No winner, there was a tie")
        return True
    else:   
        return False

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
    
def RCV(df):
    print(df)
    for x in range(len(df.columns)-1):
        results = df["Choice 1"].value_counts()
        tryed = checkVotes(results)
        if tryed == False:
            checkTies(results,df)
            reRank(results,df)
        else:
            break
        if x == len(df.columns)-2:
            print("This election has no winner.")

def main():
    df = dataRetrive()
    RCV(df)

main()