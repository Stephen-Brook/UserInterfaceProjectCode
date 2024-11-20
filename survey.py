import csv
import os

def executeSurvey():
    data = []

    while True:

        #collect the required data from each person in a main loop
        name = input("Enter name, or input 'done' to end survey: ")
        if name.lower() =='done':
            break
        #collect all of the required data using the methods below
        person = {"Name": name}
        person["Difficulty"] = difficulty()
        person["Time"] = time()
        person["Inputs"] = inputs()
        person["Errors"] = errors()
        person["Failures"] = failures()

        #add each person and their data to an array 
        data.append(person)

    #write the array to a csv file
    writeToCSV(data)

def difficulty():
    return input("How difficult was it to complete the required tasks? Least->most difficult, 1->10: ")

def time():
    return input("How long did it take to complete the required task (in seconds): ")

def inputs():
    return input("How many times did you have to provide input to the program (how many clicks): ")

def errors():
    return input("How many errors did you encounter: ")

def failures():
    return input("Were there any pages that failed to function or show (y/n)").lower() == 'y'

def writeToCSV(data):
    #check to see if the data file already exists
    exists = os.path.isfile('data.csv')
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        #if the data file doesn't exist, create a new one and add the header
        if not exists:
            header = ["Name", "Difficulty", "Time", "Inputs", "Errors", "Failures"]
            writer.writerow(header)

        #write all of the data collected to the csv file
        for person in data:
            writer.writerow([
                person["Name"], person["Difficulty"], person["Time"],
                person["Inputs"], person["Errors"], person["Failures"]
            ])

def main():
    executeSurvey()

if __name__ == "__main__":
    main()