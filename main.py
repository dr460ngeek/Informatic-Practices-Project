import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import DataHandler
import GraphMaker

##A simple function to avoid type error and pout of range inputs from user
def take_input(string,low,high):
    print()
    while True:
        try:
            value = int(input(string))
            if value>=low and value<=high:
                return value
            else:
                print('Value out of range please try again...')
        except ValueError as e:
            print('Invalid datatype, please enter a number ')

    
##The Welcoming lines
def title():
    print('\t\t',end='')
    for i in range (27): print('*',end='')
    print()
    print('\t\t*Welcome to Bill Mangement*')
    print('\t\t',end='')
    for i in range (27): print('*',end='')
    print('\n\n')

##A list of the writing ncessary in the program's front-end interface
def menu (index):
    print('\n\n')
    if index == 0:
        print('1. Upload CSV file')
        print('2. Help uploading CSV file')
        
    elif index == 1:
        print ('1.Analyze General Sales Perfomance')
        print ('2.Analyze Specific Category Sale Performance')
        print ('3.Analyze Customer preferances')
        print ('4.Quit Program')
        print('Enter 0 to return to back to  Main-Menu')
    elif index == 999:
        print ('The CSV file should be in format :',
               '\t1.Item_Category (Electronics,Grocery,Stationary,Clothing)',
               '\t2.Item_Name','\t3.Original Price','\t4.Selling Price',
               '\t5.Customer_Name','C\t6.ard_Type(VISA/MasterCard)',sep='\n')
        print ('Save the CSV file as \'sales.csv\'')
        print ('\nEnter to exit help menu...')
        

## To read CSV File From User
def read_csv():
    while True :
        menu(0)
        opt = take_input('Enter your option:',1,2)
        
        if opt == 1 :
            try :
                file_name = input('Enter File Name:\t')
                df = pd.read_csv(file_name)
                print('The CSV file has been read succesfully:')
                return df
            except Exception as e:
                print(e)
        elif  opt == 2:
                menu(999)
                input()
## To find all the differnt customers that have visited
def Find_Subjects(df,colmun):
    subjects = df.pivot_table(index=[colmun], aggfunc='size').index.tolist()
    return subjects

## To choose specific Subjects 
def Choose_Subjects(df,subjects):
    print('Choose customers you want to analyze:\n')
    x = 0
    for i in subjects:
        print(x,'. ',i,sep = '')
        x += 1
    print(x,'. For all Subjects',sep = '')
    print(x+1,'. To finish selection',sep = '')
    
    SubjectsChoosen = []
    string = str('Input Subject Index (Enter '+str(len(subjects)+1)+' to quit)')
    while True: 
        choice = take_input(string,0,len(subjects)+1)
        if choice == len(subjects):
            SubjectsChoosen = subjects
            print('You\'ve choosen all the subjects:\n',SubjectsChoosen)
            break
        elif choice ==  len(subjects)+1: break
        else:
            SubjectsChoosen.append(subjects[choice])
            print ('Subjects choosen for analysis is:',SubjectsChoosen)
    return SubjectsChoosen

## To retun table with only selected subjects
def Alter_Table (df,choosen,colmun):
    del_index = []
    print('You\'re choosen subjects are:',choosen)
    for key,value in df.iterrows():
        if not value[colmun] in choosen:
            del_index.append(key)
    NewDf = df.drop(del_index,axis=0)
    return NewDf
 



##Main Program
def main():
    title ()
    df = read_csv()
    print(df)
    while True:
        menu(1)
        opt = take_input('Enter your option:',0,4)
        if opt == 1:
            DataHandler.GenAnalysis(df)
            GraphMaker.GenAnalysis(df)
        elif opt ==2:
            sections = Find_Subjects(df,'Item_Category') #Find all categories
            choosen = Choose_Subjects(df,sections)  #Let user choose his subjects
            NewDf = Alter_Table(df,choosen,'Item_Category') #Creat a new dataframe with only the specifed subjects
            
            DataHandler.SectionAnalysis(NewDf,choosen)
            GraphMaker.SectionAnalysis(NewDf,choosen)
        elif opt==3:
            customers = Find_Subjects(df,'Customer') #Find all customers
            sections = Find_Subjects(df,'Item_Category')
            choosen = Choose_Subjects(df,customers)  #Let user choose his subjects
            NewDf = Alter_Table(df,choosen,'Customer') #Creat a new dataframe with only the specifed subjects

            DataHandler.CustomerAnalysis(NewDf,choosen)
            GraphMaker.CustomerAnalysis(NewDf,choosen,sections) #We need tp provide avliable item categories to plot grpah
        elif opt== 4:
            exit()
        elif opt == 0:
            main()
    
        

main()