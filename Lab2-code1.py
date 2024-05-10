import os 
file_path = r"c:\Users\Jimmy\Desktop\Recommender_Systems\UN201301.txt"
d = {"data": "" ,"hotlines": 0, "sentences": 0 }
data=dict()
hotlines=dict()
sentences=0
with open(file_path, mode="r", encoding="utf-8") as f :
    for line in f.readlines():
        line = line.split(",")
        if line[1] not in data.keys():
            data[line[1]] = 1
        else:
            data[line[1]] = data[line[1]]+1
        if line[2] not in hotlines.keys():
            hotlines[line[2]] = line[2]
        if "。" in line[9]:
            l = line[9].split("。")
            sentences = sentences + len(l)
#sorted_data => list  dict(sorted_data) => dict 
sorted_data = sorted(data.items(), key=lambda x:x[1], reverse=True)

print( "Q1: Which date has the most news stories? {ans} ".format(ans=sorted_data[0][0]) )
print( "Q2: How many distinct hotlines? {ans} ".format(ans=len(hotlines)) )
print( "Q3: How many sentences (separated by a period) in all news documents?  {ans} ".format(ans=sentences) )

