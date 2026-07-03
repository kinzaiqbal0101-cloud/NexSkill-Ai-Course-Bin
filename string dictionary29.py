fruits={
    "fruit1":"apple",
    "fruit2":"banana",
    "fruit3":"mango",
}

fruits["fruit4"]="orange"
print(fruits)
print(fruits["fruit2"])
print(type(fruits))
print(len(fruits))

for key,value in fruits.item():
    print(key,":",value)