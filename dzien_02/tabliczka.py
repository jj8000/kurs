
# for x in range(0, 11):
#     print("   ", end="")
#     print(x, end=" ")
#     for y in range(0,11):
#         print(x*y, sep=" ", end="")


for i in range(10):
    for j in range(10):
        print(f"{i*j:3}", end = ' ')

    print()