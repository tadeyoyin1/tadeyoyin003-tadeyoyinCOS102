from tabulate import tabulate

girls = ['EVELYN:' , 'JESSICA:' , 'SOMTO:', 'EDITH:', 'LIZA:','MADONNA:', 'WAJE:', 'TOLA:','AISHA:','LATIFFA:']
age_girl = [17, 16,17, 18, 16,18, 17 , 20, 19,17]
height_girl = [5.5,6.0, 5.4, 5.9, 5.6, 5.5,6.1, 6.0, 5.7, 5.5]
scores_girl = [80, 85, 70, 60, 76, 66, 87, 95, 50,49]
boys =['CHINEDU:', 'LIAM:', 'WALE:', 'GBENGA:', 'ABIOLA:', 'KOLA:', 'KUNLE:', 'GEORGE:','THOMAS:','WESLEY']
age_boy = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19 ]
height_boys = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 6.8, 5.7]
scores_boys = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

names = girls+boys
ages= age_girl+age_boy
heights= height_girl + height_boys
scores= scores_boys+scores_girl
table = []
for i in range(len(names)):
    table.append([names[i], ages[i], heights[i], scores[i]])

# Print table
headers = ["Name", "Age", "Height", "Score"]
print(tabulate(table, headers=headers, tablefmt='grid'))


