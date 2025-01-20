import pandas as pd

#intro to dataframes 

df = pd.DataFrame([[1,3,3],[2,3,4],[3,4,5]],index=['x' , 'y' , 'z'] ,columns=['A' , 'B' , 'C'])

#so basically a dataframe is like a self made sheet...the sheet is defined maunally same as the rows and the columns....its declared by a tuple then each row is a list....the make more rows we have to make the list a list of lists (yes lol) the name the columns accordingly as seen above

print(df.head()) #this prints the first five lines of the data frame (table)

print('')

print(df.head(2)) #first two rows and so on

print('')

print(df.tail()) #bottom five rows

print(df.tail(2))  #bottom two rows ad so on 

#its is possible to accesss the index of the rows to list method

print(df.index.tolist()) #there are 3 rows x,y,z

#to see the info of the dataframe 
# print(df.info())

#to inspect the statistical analysis of number based dataframes, we use the .describe method to do so

print(df.describe())
print()


#so irl,self defined dataframes cant be used for real data analysis...hence, already prepped data is imported into pandas dataframes and the can be analysed appropriately
#hence we read csv files into the script using the built in pyhton method

coffee_sales = pd.read_csv('pandas/coffee_sales.csv')
#other file formats such as .xls .parquet can be used in the same might as a .csv file...just change the word after the '.read_' to the required file format
# print(coffee_sales)

print()

# #filtering dataframe by rows and columns
# #locating items rather

print(coffee_sales.loc[[1,3,5] , 'Coffee']) #filtering based on index and coffee type ###--> The column index rather

print()

print(coffee_sales.loc[1:]) #filtering based on just index...this is immensely similar to indexing in lists

print((coffee_sales.loc[[1,2,4]])) #just indexes

print()

print(coffee_sales.loc[[1,5,8,4] ,['Units' , 'Sales($)']]) #showing the indexes and some selected columns

# #------------------>>> Iloc is kinda the same just that instead of passing the name of the column to be filtered in, we use the column index...this helps to reduce keyerrors in case of typos

print(coffee_sales.loc[[1,5,8,4] ,['Units' , 'Sales($)']]) #showing the indexes and some selected columns --> instead of this

print()

print(coffee_sales.iloc[[1,5,8,4] , [1,2]])

# #another fun thing that can be done is assigning the indexes of the rows to a columns
# #e.g 
#coffee_sales.index = coffee_sales.Coffee #now the names of the coffee is also the horizontal index


#accessing data in the dataframe 

# print(coffee_sales)

data1 = coffee_sales.iloc[0,0]

# #changing values individually

coffee_sales.iloc[0,0] = 'Latte de Italia'
# print(coffee_sales)


#the .at and .iat are also used to get specific values from the dataframe

print(coffee_sales.iat[0,0]) #this only works for specific item in the dataframe

print()

#--->accessing columns 
print(coffee_sales['Coffee']) #or

print()

# print(coffee_sales.Coffee) #if the column name is just one word


#sorting values 

print(coffee_sales.sort_values(['Coffee',"Sales($)"],ascending=[True , False])) #toggling between true and false specifies whether itll be in ascending or descending order ----> please note the order of ascension should correlate with the values to be sorted


## looping through 







































