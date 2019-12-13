import pandas as pd
data = pd.read_csv('equity_value_data.csv')

churned = []
groupby_name = data.groupby('user_id')
for user in groupby_name:

    count = 0
    data = user[1].iterrows()
    data = list(data)
    for line in data:
        if float(line[1]["close_equity"]) < 100:
            count += 1
    if count >= 28:
        churned.append(user[0])
features_data = pd.read_csv('features_data.csv')
users = features_data["user_id"]
all_churned = []
for i in users:
	if i in churned:
		all_churned.append(1)
	else:
		all_churned.append(0)
print(all_churned)
features_data['churned'] = all_churned
features_data.to_csv("features_data_with_churned.csv", Index=False)
