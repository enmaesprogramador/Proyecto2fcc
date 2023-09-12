import pandas as pd


url = "https://raw.githubusercontent.com/freetrv/demographic_data_analyzer/main/adult.data.csv"
data = pd.read_csv(url)


race_counts = data['race'].value_counts()


average_age_men = round(data[data['sex'] == 'Male']['age'].mean(), 1)


percentage_bachelors = round((data['education'] == 'Bachelors').mean() * 100, 1)


education_advanced = ['Bachelors', 'Masters', 'Doctorate']
percentage_advanced_earning_50k = round((data[data['education'].isin(education_advanced)]['salary'] == '>50K').mean() * 100, 1)


percentage_non_advanced_earning_50k = round((data[~data['education'].isin(education_advanced)]['salary'] == '>50K').mean() * 100, 1)


min_work_hours = data['hours-per-week'].min()


percentage_min_hours_earning_50k = round((data[data['hours-per-week'] == min_work_hours]['salary'] == '>50K').mean() * 100, 1)


country_highest_earning = data[data['salary'] == '>50K']['native-country'].value_counts().idxmax()
percentage_highest_earning = round((data[data['native-country'] == country_highest_earning]['salary'] == '>50K').mean() * 100, 1)


occupation_highest_earning_india = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts().idxmax()


print("Respuestas:")
print("Pregunta 1:", race_counts)
print("Pregunta 2:", average_age_men)
print("Pregunta 3:", percentage_bachelors)
print("Pregunta 4:", percentage_advanced_earning_50k)
print("Pregunta 5:", percentage_non_advanced_earning_50k)
print("Pregunta 6:", min_work_hours)
print("Pregunta 7:", percentage_min_hours_earning_50k)
print("Pregunta 8:", f"País con mayor porcentaje de >50K: {country_highest_earning} ({percentage_highest_earning}%)")
print("Pregunta 9:", f"Ocupación más popular en India entre los que ganan >50K: {occupation_highest_earning_india}")