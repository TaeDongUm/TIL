# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요

word = input()
dic={}
for i in word:
    if i not in dic:
        dic[i]  = 1
    else:
        dic[i] +=1

for alphabet, num in dic.items():
    print(alphabet, num)



