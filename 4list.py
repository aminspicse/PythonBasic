x = ["Apple", "Mango","Orange","Stroberry"]
print(x)
print(x[0])
print(x[1:4])
x[1] = "Lecce"
print(x)

x.insert(2,"Banana")
print(x)
x.append("cherry")
print(x)

x = ["Apple", "Mango","Orange","Stroberry"]
x.remove("Mango")
print(x)
x.pop()
print(x)
x.clear()
print(x)

# LIst loop
x = ["Tommato","Apple", "Mango","Orange","Stroberry"]
for a in x:
    print(a)

print(x)
y = []
for a in x:
    if "Mango" in a:
        y.append(a)

print(y)
print(x)
x.sort();
print(x)
x.append(y)
print(x)