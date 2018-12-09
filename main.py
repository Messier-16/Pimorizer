
with open('pi.txt','r') as file:
  pi=file.readline()

def test():
  for i in range (1,13):
    a=10*(i-1)
    b=10*i
    print(pi[a:b],"\n")
  ans = (input("\nList the digits of pi! Three point... \nPi = 3."))
  if (ans).isdigit() == False:print("Oops! Numbers only!")
  counter1=0
  for i in range(0,(len(ans))):
      if ans[i] == pi[i]:
          counter1+=1
      else: break
  next = pi[counter1:counter1+4]
  if counter1==1: article=""
  else: article="s"
  print("\nYou got {0} digit{1}. \n\nPi = 3. {2}\n{3}\n".format(counter1, article, pi[0:counter1], (' '*(counter1+9))+next))
  
  test()

test()
