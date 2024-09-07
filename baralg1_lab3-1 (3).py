#Gaurab Baral, DSC-200, Lab 3
import csv
import json
from xml.etree import ElementTree
from os.path import exists


class DscDataProcessor:

    def __init__(self,path1,path2,path3):           #this is the constructor
        self.csvFile = path1
        self.jsonFile = path2
        self.xmlFile = path3
        self.student_data = []
    def set_data(self,student_data):    #this is the setter for the list for question 1
        self.student_data = student_data

    def csvFileRead(self):  #question number 1
        with open(self.csvFile, 'w', newline='') as fptr:
            header = ['FirstName', 'LastName', 'ProgramName']
            writer = csv.writer(fptr)  # specify writer as the writer object
            writer.writerow(header) #write the header
            for data in self.student_data:  # this two lines set each list inside of the main list as a row for the csv file
                writer.writerow(data)
            fptr.close()    #close the file


    def jsonFileRead(self): #question number 2
        if exists(self.jsonFile):
            with open(self.jsonFile, 'r') as jsonFile:  # this opens the file as read-only-mode
                jsonData = json.load(jsonFile)  # this loads the json document
                number_of_objects = len(jsonData)  # this counts the number of objects
                print('Number of Objects in the JSON file:', number_of_objects)  # this prints the number of objects
                jsonFile.close()  # THIS CLOSES THE FILE
        else:
            raise FileNotFoundError("File not found. Please put the file in the correct folder.")

    def xmlFileExtract(self):   #question number 3
        if exists(self.xmlFile):
            tree = ElementTree.parse(self.xmlFile)
            root  = tree.getroot()  #this gets the root
            data = []
            for studentelement in root:
                studentobj = {}  #this is to store indivual object

                studCount = list(studentelement.attrib.keys())[0]
                type = list(studentelement.attrib.keys())[1]
                studCountValue = studentelement.attrib[studCount] #gets the studcount attribute
                typeValue = studentelement.attrib[type] #gets the type attribute
                studentobj[studCount] = studCountValue
                studentobj[type] = typeValue
                for field in studentelement: #this gets the child nodes
                    key = field.tag     #gets the tag
                    text = field.text   #gets the text
                    studentobj[key] = text
                data.append(studentobj) #add everything into a list
            return data
        else:
             raise("File not found. Please put the file in the correct filder") #raises that file is not found

    def xmlFileOutput(self, data):
        header = ['Student Count', 'Type', 'Program Name', 'Year Started', 'College Name']
        print("{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}".format(header[2],header[4], header[0], header[3], header[1])) #header output
        print("*****************************************************************************************************")
        for element in data:
            values_list = list(element.values())        #get all the values
            if values_list[1] == "Undergraduate":
                values_list[1] = "U"    #change to U
            if values_list[1] == "Graduate":
                values_list[1] = "G"    #change to G

            print("{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}".format(values_list[2],values_list[4], values_list[0], values_list[3], values_list[1])) #output all the list items



def function_choice1(newDsc):  #this part of the code is to check if the user wants to do task number 1
                    while True:
                        try:
                            Students_Number = int(input("Enter the number of students: "))
                            if type(Students_Number) == int:
                                break
                        except:
                            print("Invalid choice. Please enter an integer.") #check for integer

                    data = []
                    for i in range(1, Students_Number + 1):
                        FirstName = input("Enter the first name for student {:d}: ".format(i))
                        LastName = input("Enter the last name for student {:d}: ".format(i))
                        ProgramName = input("Enter the program name for student {:d}: ".format(i))
                        innerList = [FirstName, LastName, ProgramName]
                        data.append(innerList)
                    newDsc.set_data(data) #setdata setter method
                    newDsc.csvFileRead()#readcsv


def funciton_choice2(newDsc): #this part of the code is to check if the user wants to do task number 2
    newDsc.jsonFileRead()

def funciton_choice3(newDsc): #this part of the code is to check if the user wants to do task number 3
    data = newDsc.xmlFileExtract()
    newDsc.xmlFileOutput(data)


if __name__ == '__main__':
    newDsc = DscDataProcessor('data/baralg1_sample.csv', 'data/sampleData.json',
                              'data/NKU_Programs.xml')
    while True:
        try:
            choice = int(input("Enter which task you want to accomplish( 1 , 2 or 3)"))  #choose question
        except:
            print("Invalid choice. Please enter an integer.")
        if choice <1 or choice >3:
            print("Re-Enter with a value either 1 , 2 or 3")
            continue
        if type(choice) == int:
                if (choice == 1):#call task 1
                    function_choice1(newDsc)
                    print("A new file will be created! Terminate the program to view the file")
                elif (choice == 2):#call task 2
                    funciton_choice2(newDsc)
                elif (choice == 3):#call task 3
                    funciton_choice3(newDsc)
                print()
                choiceOfLoop = input("Enter R to restart the program, enter anything else to end the program: ")#Re-Start or not
                if (choiceOfLoop.lower() == "r"):
                    continue
                print("Thanks for Using our system! See you soon")
                exit()






