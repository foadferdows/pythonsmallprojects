import re
import csv
import requests
from bs4 import BeautifulSoup

# in this program we want to read the data of projects posted in ponisha.ir
# for this action we need request and bs4 for reading data , re for pick out
# our important section
# and te data.txt for write datas on it

txt = 'https://ponisha.ir/search/projects/page/{0}'
i = 0
old_project = []
with open("./data.txt" , 'r')as f :

    for line in f:
        line = re.sub(r"\s",'',line)
        i +=1
        print(i)
        name , skill , price = line.split(",")
        old_project.append(name)

f.close()
with open("./data.txt" , 'a', encoding='UTF8')as f :

    for i in range(1,40):

        site_address = requests.get(txt.format(i))
        soup = BeautifulSoup(site_address.text , 'html.parser')

        link = soup.find_all('a' , attrs={'class' :'absolute right0 left0 width-90 min-h-100 zx-900' })
        for j in link:
            li = str(j)
            li = re.sub(r"\<.+\=" ,' ', li)
            li = re.search(r'\"(.+)\"' , li)
            add = str(li.group(0))[1:-2]
            project_address = requests.get(add)
            soup = BeautifulSoup(project_address.text , 'html.parser')
            pro_name = soup.find_all('h1', attrs={'class': 'h3'})
            pro_name = re.sub(r'\<.+\>' , '', str(pro_name))
            pro_name = re.sub(r'\,' , '', str(pro_name))
            pro_name = pro_name.split()
            pro_name = ' '.join(pro_name)
            pro_name = pro_name[1:-2]
            pro_name = re.sub(r'\"' , '' , pro_name)
            if pro_name in old_project:
                continue


            c = soup.find_all('div' , attrs={'class' : 'border-a border-color-3 pv ph+ border-rad-md border-thick text-center mv mh- flip pull-left'})
            skills = []
            for w in c:
                d = str(w)
                d = re.search(r'\<.+\>\s(.*)' , d)
                skills.append(d.group(1).strip())

            c = soup.find('div' , attrs={'class' : 'row pv+++'})
            price = re.search(r'\"(\d+\d)\"' , str(c))
            price = int(price.group(1))
            skill = (' ').join(skills)
            f.write(str(pro_name)+','+(' ').join(skills)+','+str(price)+'\n')
            # print(str(pro_name)+','+(' ').join(skills)+','+str(price))

            print("- - - - - - - -")
        print("||||||||||||| page {0} Done |||||||||||||".format(i))

f.close()