def total_salary(path):
    salary_list = []
    total = 0
    try:
        with open(path, 'r', encoding='UTF-8') as fl:
            lines = fl.readlines()
            for line in lines:
                num = line.strip().split(',')
                salary_list.append(int(num[1]))
    except FileNotFoundError:
        print('File is not found')
    
    for salary in salary_list:
        total += salary
        average = int(total / len(salary_list))
    return total, average

total, average = total_salary('./salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
