#Group 8, Gaurab Baral and Aditya Khanal
import pandas as pd
import numpy as np
# Defining a function named Question1 to solve the first task
def Question1():
    #file paths for the input CSV files
    file1_path = "pollution_us_2000_2016.csv"
    file2_path = "Monthly_Counts_of_Deaths_by_Select_Causes__2014-2019.csv"
    file3_path = "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv" #not essential just checking to see if it is good or not
    file4_path = "data-table.csv"
    # Read data from CSV files into DataFrames
    file1 = pd.read_csv(file1_path)
    file2 = pd.read_csv(file2_path)
    file3 = pd.read_csv(file3_path)
    file4 = pd.read_csv(file4_path)
    # Prepare and modify file1 DataFrame
    modified_file1 = file1.set_index("State")  # Set index as "State"
    modified_file1 = modified_file1[["CO Mean", "NO2 Mean", "SO2 Mean", "Date Local"]]  # Select specific columns
    modified_file1['Year'] = pd.to_datetime(modified_file1['Date Local']).dt.year
    modified_file1 = modified_file1.drop("Date Local", axis=1)
    modified_file1 = modified_file1[(modified_file1['Year'] >= 2014) & (modified_file1['Year'] <= 2019)]
    file1_last = modified_file1.groupby(['State', 'Year'])[['CO Mean', 'NO2 Mean', 'SO2 Mean']].mean()
    file1_last.reset_index(inplace=True)
    # Prepare and modify file2 DataFrame
    modified_file2 = file2[["Year", "All Cause", "Diseases of Heart"]] #keeping the essential columns
    modified_file2 = modified_file2.set_index("Year") #set index as the
    modified_file2 = modified_file2.groupby("Year")[["All Cause", "Diseases of Heart"]].sum() #sum all the months 
    file2_last = modified_file2 #this contains the total number of people that dies every year in USA cause of Heart Disease.
    # Prepare and modify file3 DataFrame
    modified_file3 = file3.set_index("LocationAbbr")
    file3_last = modified_file3.groupby(["LocationAbbr", "Year"])[["Data_Value"]].mean() #find the mean value based on different year for a state
    file3_last = file3_last.reset_index() #moves "StateName" and "ReportYear" back from the index to regular columns
    file3_last['Data_Value'] = file3_last['Data_Value'].round(2)
    file3_last['RATE'] = file3_last['Data_Value'] / 100000
    file3_last = file3_last[file3_last['LocationAbbr'] != 'US']
    state_abbr_to_name = { # A dictionary to map state abbreviations to their full names
        'AL': 'Alabama',
        'AK': 'Alaska',
        'AZ': 'Arizona',
        'AR': 'Arkansas',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'IA': 'Iowa',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'ME': 'Maine',
        'MD': 'Maryland',
        'MA': 'Massachusetts',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MS': 'Mississippi',
        'MO': 'Missouri',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NV': 'Nevada',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NY': 'New York',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West Virginia',
        'WI': 'Wisconsin',
        'WY': 'Wyoming',
        'AS': 'American Samoa',
        'GU': 'GUAM',
        'MP': 'Northern Mariana Islands',
        'VI': 'Virgin Islands',
        'PR': 'Puerto Rico',
        'DC': 'District of Columbia'
    }
    file3_last['StateName'] = file3_last['LocationAbbr'].replace(state_abbr_to_name)
    file3_last = file3_last.drop(columns=['LocationAbbr'])
    # Prepare and modify file4 DataFrame
    file4 = file4.drop(columns=['URL'])
    file4['StateName'] = file4['STATE'].replace(state_abbr_to_name)
    file4 = file4.drop(columns=['STATE'])
    file4 = file4.set_index("StateName")  # Set the index as the year
    file4_last = file4[(file4['YEAR'] >= 2014) & (file4['YEAR'] <= 2016)].copy()
    file4_last.rename(columns={'YEAR': 'Year'}, inplace=True) #rename columns to help merge
    file4_last.reset_index(inplace=True)  # Reset the index
    # Merge data from file4_last and file2_last
    merged_data = file4_last.merge(file2_last, on='Year') #we merged 2 and 4
    merged_data.rename(columns={'All Cause': 'Total Deaths' , 'Diseases of Heart': 'Death by Heart Disease'}, inplace=True) # Rename columns for clarity
    # Merge final data by combining file1_last, file2_last, and file4_last
    final_data = merged_data.merge(file1_last, left_on=['StateName', 'Year'], right_on=['State', 'Year'])
    final_data = final_data.drop('State', axis=1)
    final_data = final_data.drop('Total Deaths', axis=1)
    print(final_data)
    final_data.to_csv("Question1mergedfile.csv", index=False)

def Question2():
    data_file = pd.read_csv("Lab6Data.csv", header=None) #get it in a dataframe
    avg_num_features = int((data_file.shape[1]))
    data_file.columns = data_file.iloc[0] #drop the first column
    data_file = data_file[1:].reset_index(drop=True) #reset the index to 0
    print("----------------------------------------------------------------------")
    print("Before Cleaning: ")
    print(f"Number of features (columns) in both files: {avg_num_features}")
    print(f"Number of observations (rows) in both files: {data_file.shape[0]}")
    print("----------------------------------------------------------------------")
    data_file.loc[:, 'workclass'] = data_file['workclass'].replace(' ?', np.nan) #replace with nan
    data_file.loc[:, 'occupation'] = data_file['occupation'].replace(' ?', np.nan)
    data_file.loc[:, 'native-country'] = data_file['native-country'].replace(' ?', np.nan)
    df = data_file #get a copy of the dataset
    df.dropna(how='any',inplace=True) #drop the row that contain at least one NAN VALUE
    df.drop_duplicates(inplace=True)
    df = df.drop(['educ_num'], axis=1) #as educational-num is similar to education column, so we can drop this.
    df['income_flag']=df['salary'].map({' <=50K':0,' >50K':1})  #Mapping '<=50K.' to 0 and '>50K.' to 1
    df['fnlwgt'] = pd.to_numeric(df['fnlwgt'], errors='coerce').astype('float64') #INVALID PARSING WILL BE Nan
    df['capital-gain'] = pd.to_numeric(df['capital-gain'], errors='coerce').astype('float64')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce').astype('float64')
    df['capital-loss'] = pd.to_numeric(df['capital-loss'], errors='coerce').astype('float64')
    df['workclass'] = df['workclass'].astype('category') #set type to category to help python run faster
    print("----------------------------------------------------------------------")
    print("After cleaning:")
    print(f"Number of features in cleaned file(columns): {df.shape[1]}")
    print(f"Number of observations in cleaned file(rows): {df.shape[0]}")
    print("----------------------------------------------------------------------")
    df.to_csv('question2_file.csv', index=False)
    #income_Flag of 0 means less than or equals to 50k .
    #income flag of 1 means the income is more than 50k.2

if __name__ == "__main__":
    while True:
        try:
            a = int(input("Welcome to LAB 6. What would you like to do?\n Press 1 to run the first task(Merge datasets)! \n Press 2 to run the second task(Clean datasets)!\n Press any other number to exit the program! "))
            if a == 1:
                Question1()
            elif a == 2:
                Question2()
            else:
                break
        except:
            print("Please enter a valid integer")

