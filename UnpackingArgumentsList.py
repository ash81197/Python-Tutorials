def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate*2) - (cigs_smoked*10)
    print("Your Age Left is:", answer)


my_data = [18, 1, 2]

health_calculator(my_data[0], my_data[1], my_data[2])
health_calculator(*my_data)