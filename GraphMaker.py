import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def GenAnalysis(df):
    
    #Sale BoxPlot
    plt.subplot(1,2,1)
    plt.boxplot(df['Price'])
    plt.title('Price per item sold')    

    #CardGraph
    plt.subplot(1,2,2)
    df_card = df.pivot_table(index =['Card_Type'],aggfunc = 'count')['Price']
    x = np.arange(len(df_card))
    plt.bar(x,df_card)
    plt.title('Most poular card in use')
    plt.show()
    


def SectionAnalysis(df,sections):
    total_sale = []
    cnt_customers = []
    items_sold = []
    i = 0
    
    for value in sections:
        df_section = df.loc[df['Item_Category']==value]
        
        total_sale.append(df_section['Price'].sum())
        cnt_customers.append(len(df_section.pivot_table(index=['Customer'], aggfunc='size')) )
        items_sold.append(df_section['Item_Name'].count())
        #Pivot the table of a specific item by categories and aggreagte function count to obtain money spent on each category
        df_items = df_section.pivot_table(index=['Item_Name'],aggfunc = 'count')['Price']
        
        # Graph for ecah item sold in each category
        i += 1
        plt.figure(1)
        plt.subplot(2,2,i)
        x = np.arange(len(df_items))
        plt.bar(x,df_items.tolist())
        plt.title('Sale of items in '+value)
        plt.ylabel('Items Sold')
        plt.xticks(x,df_items.index.tolist())
        
        
    x = np.arange(len(sections))
    #Graph for total sale
    plt.figure(2)
    plt.subplot(2,2,1)
    plt.bar(x,total_sale)
    plt.title('Total Sale across all the sections')
    plt.ylabel('Sale in Dhs.')
    plt.xticks(x,sections)

    #Graph for number of customers visted
    plt.subplot(2,2,2)
    plt.bar(x,cnt_customers)
    plt.title('Number of vistors')
    plt.xticks(x,sections)
    plt.ylabel('No.of people')
    
    #Graph for number items sold
    plt.subplot(2,2,3)
    plt.bar(x,items_sold)
    plt.title('Number of items sold')
    plt.xticks(x,sections)

    #Graph for 
    plt.show()

def CustomerAnalysis(df,customers,sections):
    #Find names of customers using pivot_table and loop their purchases
    df_customer_sections = pd.DataFrame(index = sections)

    for key in customers:
        df_customer = df.loc[df['Customer'] == key]
        total_sale = []
        #Computing Aggragates
        total_sale.append(df_customer['Price'].sum())
        #Pivot the table of a specific customer by categories and count to obtain money spent on each category
        df_category = df_customer.pivot_table(index=['Item_Category'],aggfunc = 'count')['Price']
        #Add this pivoted table to a record of different customers
        df_customer_sections[key] = df_category
    
    ##Print the 'dfCustomerSectionsCount' datframe as a bar graph 
    shift = 0
    bar_size = len(customers)/100 
    for key ,value in df_customer_sections.iteritems() :
        x = np.arange(len(sections))
        plt.bar(x+shift,value,width = bar_size,label = key)
        plt.xticks(x,sections)
        plt.legend(loc = 'upper right')
        shift += bar_size
    plt.show()
    print('Press Enter to continue:')
    input()
    
##CustomerAnalysis(pd.read_csv('sales_day5.csv'),['Mukesh Mandal', 'Muhammad Aftab', 'Pratham Agarwal'],['Clothing', 'Grocery', 'Stationary'])
