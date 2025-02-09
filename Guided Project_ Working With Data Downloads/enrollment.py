import pandas as pd
data=pd.read_csv("data/CRDC2013_14.csv")
data["total_enrollment"]=data["TOT_ENR_M"]+data["TOT_ENR_F"]
gender_race=['SCH_ENR_HI_M','SCH_ENR_HI_F','SCH_ENR_AM_M','SCH_ENR_AM_F','SCH_ENR_AS_M','SCH_ENR_AS_F','SCH_ENR_HP_M','SCH_ENR_HP_F','SCH_ENR_BL_M','SCH_ENR_BL_F','SCH_ENR_WH_M','SCH_ENR_WH_F','SCH_ENR_TR_M','SCH_ENR_TR_F']
HI=data['SCH_ENR_HI_M']+data['SCH_ENR_HI_F']
AM=data['SCH_ENR_AM_M']+data['SCH_ENR_AM_F']
AS=data['SCH_ENR_AS_M']+data['SCH_ENR_AS_F']
HP=data['SCH_ENR_HP_M']+data['SCH_ENR_HP_F']
BL=data['SCH_ENR_BL_M']+data['SCH_ENR_BL_F']
WH=data['SCH_ENR_WH_M']+data['SCH_ENR_WH_F']
TR=data['SCH_ENR_TR_M']+data['SCH_ENR_TR_F']
all_enrollment=data["total_enrollment"].sum()
for gr,x in enumerate(gender_race):
    print(x+":"+str((gr/all_enrollment)))
    