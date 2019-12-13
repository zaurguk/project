import pandas as pd


data = pd.read_csv('features_data_with_churned_csv')
platforms = data['platform']
android = 0
IOS = 0
for i in platforms:
	if  i == "Android":
		android += 1
	if i == 'iOS':
		IOS += 1
churned = data['churned']
IOS_churned = 0
android_churned = 0
for i in range(5585):
	if churned

