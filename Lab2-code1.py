import os
file_path = r"c:\Users\Jimmy\Desktop\Recommender_Systems\UN201301.txt"
data=dict()
hotlines=dict()
sentences=0
with open(file_path, mode="r", encoding="utf-8") as f :
   for line in f.readlines():
       line = line.split(",")
       #計算日期次數
       if line[1] not in data.keys():
           data[line[1]] = 1
       else:
           data[line[1]] = data[line[1]]+1
       #計算熱線條數
       if line[2] not in hotlines.keys():
           hotlines[line[2]] = line[2]
       #計算 。 次數
       if "。" in line[9]:
           split_line = line[9].split("。")
           new_line =[x for x in split_line if x.strip()!='']
           sentences = sentences + len(new_line)
#sorted_data => list  dict(sorted_data) => dict
sorted_data = sorted(data.items(), key=lambda x:x[1], reverse=True)
print( "Q1: Which date has the most news stories? {ans} ".format(ans=sorted_data[0][0]) )
print( "Q2: How many distinct hotlines? {ans} ".format(ans=len(hotlines)) )
print( "Q3: How many sentences (separated by a period) in all news documents?  {ans} ".format(ans=sentences) )

