def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age


for i in range(17, 50):
    age_limit = allowed_dating_age(i)
    if i <= 20:
        print("Age Of Dating the Girl for", i, " years Old Boy is", age_limit)
    else:
        print("Age Of Dating the Girl for", i, " years Old Man is", age_limit)