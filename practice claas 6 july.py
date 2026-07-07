import numpy as np

ids, price , long , lat = np.genfromtxt('Week4/zameencom-property-data-By-Kaggle-short.csv', delimiter=';', usecols=(0,4,8,9), unpack=True, dtype=None,skip_header=1)

print(ids)
print(price)
print(long)
print(lat)

print(np.min(price))

# Zameen.com price  - statistics operations
print("Zameen.com Price mean: " , np.mean(price))
print("Zameen.com Price average: " , np.average(price))
print("Zameen.com Price std: " , np.std(price))
print("Zameen.com Price mod: " , np.median(price))
print("Zameen.com Price percentile - 25: " , np.percentile(price,25))
print("Zameen.com Price percentile  - 75: " , np.percentile(price,75))
print("Zameen.com Price percentile  - 3: " , np.percentile(price,3))
print("Zameen.com Price min : " , np.min(price))
print("Zameen.com Price max : " , np.max(price))

# Zameen.com price  - maths operations
print("zameen.com price sum:",np.sum(np.square (price)))
print("zameen.com price square root:",np.sqrt(np.sum(price)))
print("zameen.com price log:",np.log(np.sum(price)))
print("zameen.com price exp:",np.exp(np.sum(price)))
print("zameen.com price sin:",np.sin(np.sum(price)))
