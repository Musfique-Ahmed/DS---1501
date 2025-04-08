# grade = 50
# if grade == 100:
#     print("Golden A+")
# if grade >= 90:
#     print("A")

# elif grade >= 80:
#     print("B")
# if grade == 50:
#     print('About to fail')
# else:
#     print("F")




# age = 20

# if age > 18:
#     print("You are an adult.")

# if age > 21:
#     print("You can drink alcohol in some countries.")

# if age > 24:
#     print("You are eligible for car rental in many places.")




# cart_total = 550

# if cart_total > 500:
#     print("You get a 10% discount!")

# if cart_total > 1000:
#     print("You get a free gift!")

# if cart_total > 2000:
#     print("You qualify for free shipping!")
# age = 25
# # status = "adult" if age >= 18 else "minor"


# if age >= 18:
#     status = "adult"

# else:
#     status = "minor"


# print(status)





# lst = [1,2,3]

# for num in lst:
#     print(num+2)




# for i in range(0, 5, 2): #(start, stop, skip)
#     print(i)

# for musfique in range(1,5): #(start, stop), default skip = 1
#     print(musfique)

# for i in range(3):#(stop), default start = 0, default skip = 1
#     print(i)


# lst = [2,3,71,5,7]
# sum = 0#5

# for num in lst:
#     # sum = sum + num
#     sum += num
#     # print(sum)

# print(sum)


# # sum += 1
# lst = [2,3,71,5,7]
# count = 0

# for num in lst:
#     if num % 2 == 1:
#         count += 1
    
# print(count)

# lst = [2,3,71,5,7]
# for i in range(0, len(lst)):#0,1,2,3,4
#     if i == 2:
#         lst[i] = 10

# print(lst)

# lst = [2,3,71,5,7]
# lst2 = [1,2,3,5,7]
# for i in range(0, len(lst)):
#     if lst[i] == lst2[i]:
#         print(i)

    
# for i in lst:
#     ind = lst.index(i)#0,1,2,3,4
#     if i == lst2[ind]:#2 == lst2[0](1)
#         print(ind)


# print(lst.index(5))


# num = 0

# while num<5:
#     print(num)
#     num += 1

# usr = input()

# while usr != "q":
#     usr = input()


# usr = input()
# while True:
#     # usr = input()
#     if usr == "q":
#         break


# num = 0

# while True:
#     num += 1
#     if num == 100:
#         break
#     if num == 20:
#         continue
#     print(num)


# my_list = [1, 2, 3, 4, 5]
# index = 0
# while index < len(my_list): #while index < 5:
#     print(my_list[index])
#     print(f"index: {index}")
#     index += 1

# colors = ["red", "green", "blue", "yellow", "purple"]
# index = 0

# while index < len(colors):
#       # while index < 5:
#     if index == 2:
#         index += 1
#         continue
#     print(colors[index])
#     print(f"index: {index}")
#     index += 1

# counter = 1

# while counter <= 10:
#     print(counter)
#     counter += 1


color = ['red', 'blu', 'yelo', 'grin']
index = 0

while index<len(color)-1:

    color[index+1] = color[index]
    index += 1

print(color)