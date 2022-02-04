import re

from sklearn import tree


# in this program we want make a model for machine learning to know , in the ponisha.ir
# people already how mush spent for project that included our skils
# for machine learning we use sklearn and DecisionTreeClassifier function 
# but in the first we ask user to write skills



pro_names = []
prices = []
skills_list = []

s_l = []
total_skills = dict()
j = 1
with open("./data.txt" , 'r')as f :
    for line in f:
        for name , skill , price in line.split(','):
            pro_names.append(name)
            prices.append(str(price))
            s_l = []
            to = skill[1:-2]
            to_list = to.split(',')
            for skil in to_list:
                match = skil
                match = re.sub(r"\'" , "" , match)
                total_skills[j] = match
                s_l.append(j)
                j +=1

            if len(s_l) < 5:
                for i in range(5-len(s_l)):
                    s_l.append(0)

            skills_list.append(s_l)

f.close()

for i in range(1,j):
    print(total_skills[i] + ' : ' + str(i))

input_sl = -1
input_sls = []
i = 0
while (i != 5):
    input_sl = input('please enter code of skills (for finish enter not digit char , and please enter %s skill) : '% (5-i))
    if input_sl.isdigit() and int(input_sl) <= j and 0 < int(input_sl):
        input_sls.append(int(input_sl))
        i+=1
    else:
        input_sl = input("wrong type , you want exit (y/n) ? ")
        if input_sl == 'y':
            break
        else:
            continue

clf = tree.DecisionTreeClassifier()

clf.fit(skills_list , prices)
a = []
a.append(input_sls)
answer = clf.predict(a)
print(answer)