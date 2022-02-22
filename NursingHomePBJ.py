import pandas as pd
import glob

NursingHomeData2020 = glob.glob('C:/Users/bobom/Desktop/Coursera/Nursing_Home_Data/NHomeData2020/*.csv')

nursing_df = pd.DataFrame()

for files in NursingHomeData2020: #This is returning an empty df.....
        df = pd.read_csv(files, error_bad_lines=False, encoding='unicode_escape') #Not sure what to do here... https://www.roelpeters.be/solved-dtypewarning-columns-have-mixed-types-specify-dtype-option-on-import-or-set-low-memory-in-pandas/
        nursing_df = pd.concat([nursing_df, df], ignore_index=True)

print('Concatenation Done')

### 2/21/2022 ###
# read in provider numbers using ~ pd.read_csv ~ and saved to "Provider_Num"
# converted "Provider_Num" to a list using  ~ Provider_Num.values.tolist() ~ to compare to the "Federal Provider Numbers" column in nursing_df
# renamed the "Federal Provider Numbers" column to "Provider_Number" using ~ nursing_df.rename(columns={'Federal Provider Numbers':'Provider_Number'}, inplace=True) ~ make it easier to call on/reference
# used the lambda function to compare each element in the "Provider_Number" column against the list elements in "Provider_Num" ~ nursing_df.Provider_Number.apply(lambda x: x == Provider_Num) ~
# Need to now remove all provider numbers not associated to ensign.
######


