#from _future_ import with_statement

class Solution:
   def solve(self, s):
      s = list(s[::-1])

      def get_value():
         sign = 1
         if s and s[-1] == "-":
            s.pop()
            sign = -1
         value = 0
         while s and s[-1].isdigit():
            value *= 10
            value += int(s.pop())
         return sign * value

      def get_term():
         term = get_value()
         while s and s[-1] in "*/":
            op = s.pop()
            value = get_value()
            if op == "*":
               term *= value
            else:
               term = 1.0 * term / value
         return term

      ans = get_term()
      while s:
         op, term = s.pop(), get_term()
         if op == "+":
            ans += term
         else:
            ans -= term
      return ans

ob = Solution()




file = open('TMW_large.txt','r')

tdata = list(file.read().split('\n'))
data=[] 
size = int(tdata[0])
for i in range(1,len(tdata)):
    temp = list([j for j in tdata[i][0:len(tdata[i])].split()])
    data.append(temp)

help_dict = {'zero': '0','one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9',
             'eleven':'11','twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fifteen':'15','sixteen':'16', 'seventeen':'17',
             'eighteen':'18', 'nineteen':'19',
             'plus':'+','substract':'-','multiple':'*','division':'/','equals':'='
}
ones = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}
tens = { 'twenty': '20', 'thirty': '30', 'forty': '40', 'fifty': '50', 'sixty': '60', 'seventy': '70', 'eighty': '80', 'ninety': '90'}

newList = []
for i in range(len(data)-1):
   # print(data[i])
   temp = []
   tensFlag = False
   for j in range(len(data[i])):
      if tensFlag:
         tensFlag = False
         continue
      if data[i][j] in help_dict:
         if data[i][j+1] == 'hundred':
            # data[i][j] = int(help_dict[data[i][j]]) * 100
            temp.append(str(int(help_dict[data[i][j]]) * 100))
         else:
            temp.append(help_dict[data[i][j]])

      elif data[i][j] in tens:
         if data[i][j+1] in ones:
            temp.append(tens[data[i][j]][0] + ones[data[i][j+1]])
            tensFlag = True
         else:
            temp.append(tens[data[i][j]])
      elif data[i][j] in  {'and'}:
         # temp.append("and-hundred")
         temp.append('+')
      elif data[i][j] in {'hundred'}:
         continue

      else:
         temp.append(data[i][j])   
   newList.append(temp)

string = []
for i in range(len(newList)):
   # print(newList[i])
   mystring=''.join(newList[i][:len(newList[i])-2])
   string.append(mystring)

ans =[]
for i in range(len(newList)):
   temp = newList[i][len(newList[i])-1]
   ans.append(temp)

solution=[]
for i in range(len(string)):
   solution.append(ob.solve(string[i]))


# with open('output_small.txt', 'w') as f:
#     for i in range(len(string)):
#       abc=str(str(ob.solve(string[i]))==ans[i])
#       f.write('Case #'+str(i)+':'+abc'\n')


writeFile = open("output_large.txt", "w")
for i in range(len(string)):

   abc=str(str(ob.solve(string[i]))==ans[i])
   writeFile.write('Case #'+str(i)+':'+abc +'\n')
   print('Case #'+str(i)+':'+abc)





# for i in string:
#     print(i)

# for i in range(len(solution)):
#     print(solution[i] , ans[i])