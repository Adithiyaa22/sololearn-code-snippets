siblings = int(input())
popsicles = int(input())

total_even_popsicles = popsicles/siblings 
 
# total popsicles is divided to get equal   no. of popsicles to every siblings 

count = int(total_even_popsicles)* siblings 

#conversion of total_even_popsicles to int to get the correct count 

if (count == popsicles ):
   print("give away")
else:
   print("eat them yourself")