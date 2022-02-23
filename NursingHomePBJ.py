import pandas as pd
import glob
import traceback2 as tb
NursingHomeData2020 = glob.glob(r'\\irvdcna01\home$\PThompson\Documents\Covid Project\NHomeData2021\*.csv')

nursing_df = pd.DataFrame()

for files in NursingHomeData2020:
        try:
                Nursing_Home_Data_Filtered = pd.read_csv(files, usecols=['Federal Provider Number', 'Week Ending', 'Provider Name', 'Provider State', 'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time'], on_bad_lines='warn', encoding='unicode_escape')
                nursing_df = pd.concat([nursing_df, Nursing_Home_Data_Filtered], ignore_index=True)
        except Exception:
                tb.print_exc()
                continue


print('Concatenation Done')


### 2/21/2022 ###
# read in provider numbers using ~ pd.read_csv ~ and saved to "Provider_Num"
# converted "Provider_Num" to a list using  ~ Provider_Num.values.tolist() ~ to compare to the "Federal Provider Numbers" column in nursing_df
# renamed the "Federal Provider Numbers" column to "Provider_Number" using ~ nursing_df.rename(columns={'Federal Provider Numbers':'Provider_Number'}, inplace=True) ~ make it easier to call on/reference
# used the lambda function to compare each element in the "Provider_Number" column against the list elements in "Provider_Num" ~ nursing_df.Provider_Number.apply(lambda x: x == Provider_Num) ~
# Need to now remove all provider numbers not associated to ensign.
######


OurProviderNumbers = pd.read_excel(r'\\irvdcna01\home$\PThompson\Documents\Covid Project\OurProviderNumbers.xlsx')
OurProviderNumbers = OurProviderNumbers.values.tolist()

Nursing_Home_Data_Filtered.rename(columns={'Federal Provider Numbers':'Provider_Number'}, inplace=True)

Provider_Number_Bool = Nursing_Home_Data_Filtered.Provider_Number.apply(lambda x: x == OurProviderNumbers)

for boolean_false in Provider_Number_Bool:

##Create a new column with the boolean value and delete the rows based off of that