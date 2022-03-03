# Coding Challenge #1: For each State that we operate in, on which [week_ending] did the average of our healthcare personal with a completed vaccination exceed 80%?

# Coding Challenge #2: For each of Our Providers, what is their longest streak (# of weeks) of residents not testing positive for Covid-19 ([residents_weekly_confirmed_covid_19])?

# Bonus Challenge: If the goal for each of the states we are in is to get all of our providers above 80% vaccination for both residents and patients — Draw mockups of the dashboard(s) you would propose in order to achieve this goal for each state.


# test[['Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time', 'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week']]




import pandas as pd
import glob
import traceback2 as tb
import os

#NursingHomeData2020 = glob.glob(r'\\irvdcna01\home$\PThompson\Documents\Covid Project\NHomeData2021\*.csv')
NursingHomeData2021 = glob.glob(r'C:\Users\bobom\Desktop\Coursera\Nursing_Home_Data\NHomeData2021\*.csv')

nursing_df = pd.DataFrame()

for files in NursingHomeData2021:
        try:
            Nursing_Home_Data_Filtered = pd.read_csv(files, usecols=['Federal Provider Number', 'Week Ending', 'Provider Name', 'Provider State', 'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time', 'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week'], on_bad_lines='warn', encoding='unicode_escape')
            nursing_df = pd.concat([nursing_df, Nursing_Home_Data_Filtered], ignore_index=True)
        except Exception:
            tb.print_exc()
            continue


print('Concatenation Done')

nursing_df.rename(columns={'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time':'Vaccinated Personnel'}, inplace=True)

nursing_df.rename(columns={'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week':'Total Personnel'}, inplace=True)
    # Changed the column names to something less long...

EnsignsProviderNumbers = pd.read_csv(r'C:\Users\bobom\Desktop\Coursera\Nursing_Home_Data\OurProviderNumbers.csv')
    # Read in EnsignsProvidernumbers so we can filter out facilities that don't fall under Ensign.

    # Tried using <nursing_df['Federal Provider Number'].isin(EnsignsProviderNumbers)> but there doesn't seem to be any matching Provider Numbers when checking to see if Ensigns Provider Numbers are in nursing_df.

    # Used <nursing_df['Federal Provider Number'].isin(EnsignsProviderNumbers).value_counts> to verify that all results came back as false from the previous query.

    # <nursing_df.dtypes> and <EnsignProviderNumbers.dtypes> have the columns set as objects...
#

EnsignsProviderNumbers = EnsignsProviderNumbers.to_numpy().tolist()
    # Figured it would be better to convert to a list and check again based on the descriptions given here https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html

EnsignsProviderNumbers = [val for sublist in EnsignsProviderNumbers for val in sublist]
    #Used this to get rid of the brackets in the list. The brackets were being read as part of the element.
#
EnsignIsIn = nursing_df['Federal Provider Number'].isin(EnsignsProviderNumbers)
EnsignIsIn.value_counts()
    # Result:
    # False    30470931
    # True       430262
    #Looking back at it now, I didn't originally assign <nursing_df['Federal Provider Number'].isin(EnsignsProviderNumbers).value_counts> to a variable....Maybe I didn't need to convert  EnsignsProviderNumbers to a numpy array then to a list?
#
EnsignNursingHomeData = nursing_df.assign(Affiliate=EnsignIsIn)
    # Adding in this column to later drop all rows that have a value of False in this column
#
RowsDropped = EnsignNursingHomeData[EnsignNursingHomeData['Affiliate'] == False].index
EnsignNursingHomeData.drop(RowsDropped, inplace=True)
    # Dropped like flies....
#
EnsignNursingHomeData.reset_index(drop=True, inplace=True)
    # Just to reorganize and make everything look nice and neat.
#
EnsignNursingHomeData.to_pickle(r'C:\Users\bobom\Desktop\EnsignNursingHomeData2021.pkl')
    # Pickling now that the data is nice and organized. Saved on github
# NursingHomeData = pd.read_pickle(r'C:\Users\bobom\Documents\nursing_df.pkl')





























#-------------------------------------------------------------------------------------------------------------------
# NursingHomeData = pd.read_pickle(r'C:\Users\bobom\Documents\nursing_df.pkl') #Now that I've created a pkl file for the data I need.....
# OurProviderNumbers = pd.read_csv(r'C:\Users\bobom\Desktop\Coursera\Nursing_Home_Data\OurProviderNumbers.csv')
#
#
# #Next, identify if there are any provider numbers that match Ensign's provider numbers
# ### flattened = [val for sublist in OurProviderNumbersList for val in sublist] used this to get rid of the brackets after turning OurProviderNumbers
# ### into a a numpy array then to a list.
# ### Created a series containing only the 'Federal Provider Number' column called NursingHomeDataisin.
# ### NursingHomeDataisin = NursingHomeData['Federal Provider Number'].isin(flattened)
# ### Used NursingHomeDataisin.value_counts() to identify how many of OurProviderNumbers were in the series.
