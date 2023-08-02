import pandas as pd

patientsdf=pd.read_csv("patients.csv")
doctorsiddf=pd.read_csv("doctors.csv")
patientsdoctorsdf=pd.read_csv("pd.csv")
table1=pd.merge(patientsdf,patientsdoctorsdf,on="patientid")
table2=pd.merge(table1, doctorsiddf, on="doctorsid")