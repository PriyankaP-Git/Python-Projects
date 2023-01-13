person = {"name" : "Priyanka", "age" : 30,}
#print(person["name"])
person["job"] = "Developer"
print(person)
for i in person:
    #print(i)
    #print(person[i])
    print(f"key: {i} = value: {person[i]}")