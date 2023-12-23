x = 100

#while (True):

   #line = input("enter q to quit")

  #if (line == 'q'):break

  #print(x)

fruits = ["apple", "banana", "mango", "orange"]

fruits_len = len(fruits)

fruit_found = False

index = 0

while(index < fruits_len):
    if fruits[index] == 'strawberry':
        fruit_found = True 
        print("strawberry is available")
        break
    index += 1
if not fruit_found:
    print('no strawberry')
    

# infine while loop