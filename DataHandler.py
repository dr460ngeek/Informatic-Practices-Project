import pandas as pd
import numpy as np

def GenAnalysis(df):
    
    print('Wlecome to general analysis')
    total_sale = df['Price'].sum()
    cnt_customers = len(df.pivot_table(index=['Customer'], aggfunc='size')) #We use pivot_table with aggregate function as
    avg_sale = total_sale/cnt_customers                                     #size to find number of non-duplicates customers 
    items_sold = df['Item_Name'].count()
    df_card = df.pivot_table(index =['Card_Type'],aggfunc = 'count')['Price']
    best_card = df_card.loc[df_card == df_card.max()]

    #Print Results
    print ('Total Number of Customers visted:',cnt_customers)
    print ('Total Sale :',total_sale,'Dhs')
    print ('The average sale per customer:',avg_sale,'Dhs')
    print ('Number of Items Sold:',items_sold)
    print ('Most Popular card today:',best_card.index.tolist(),'Used:',best_card.tolist(),'times')
    print('Press Enter to continue:')
    input()


def SectionAnalysis(df,sections):
    print('Wlecome to section wise analysis')

    ##Looping across all possible item cateogry
    for value in sections:
        print('Categotry Wise Analysis for',value,'Section:')
        df_section = df.loc[df['Item_Category'] == value]

        #Compute Aggregates
        total_sale = df['Price'].sum()
        cnt_customers = len(df.pivot_table(index=['Customer'], aggfunc='size')) #We use pivot_table with aggregate function as
        avg_sale = total_sale/cnt_customers                                     #size to find number of non-duplicates customers 
        items_sold = df['Item_Name'].count()
        #Pivot the table of a specific customer by categories and aggreagte function count to obtain money spent on each category
        df_items = df_section.pivot_table(index=['Item_Name'],aggfunc = 'count')['Price']
        #Use loc method find the category 
        best_item = df_items.loc[df_items == df_items.max()]
                

        #Printing Aggregates
        print ('\tTotal Number of Customers:',cnt_customers)
        print ('\tTotal Sale :',total_sale,'Dhs')
        print ('\tThe average sale per customer:',avg_sale,'Dhs')
        print ('\tNumber of Items Sold:',items_sold)
        print ('\tBest Selling item:',best_item.index.tolist(),'sold',best_item.tolist()) #I use tolist function if there are multiple values
        print ()
    print('Press Enter to continue:')
    input()

def CustomerAnalysis(df,customers):
    
    ## Loop through choosen customers
    for key in customers:
        print('Customer-wise analysis for',key)
        df_customer = df.loc[df['Customer'] == key]

        #Computing Aggragates
        total_sale = df_customer['Price'].sum()
        items_sold = df_customer['Item_Name'].count()
        avg_sale = total_sale/items_sold
        #Pivot the table of a specific customer by categories and aggreagte function sum to obtain money spent on each category
        df_category = df_customer.pivot_table(index=['Item_Category'],aggfunc = 'sum')['Price']
        #Use loc method find the category 
        fav_category = df_category.loc[df_category == df_category.max()]

        #Printing results
        print ('\tTotal Sale :',total_sale,'Dhs')
        print ('\tThe average expenditure',avg_sale,'Dhs')
        print ('\tNumber of Items bought:',items_sold)
        print ('\tFavourite category is:',fav_category.index.tolist(),'spent',fav_category.tolist(),'dhs') #Note since we pivoted the table the categories bceome the index
        print ()

    print('Press Enter to continue:')
    input()
##GenAnalysis(df = pd.read_csv('sales_Day1.csv'))

