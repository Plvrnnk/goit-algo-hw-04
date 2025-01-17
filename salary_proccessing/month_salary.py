def total_salary(path):
    salary_list = []
    total = 0
    try:
        with open(path, 'r', encoding='UTF-8') as fl:
            lines = fl.readlines()
            for line in lines:
                num = line.strip().split(',')
                salary_list.append(float(num[1]))
    except FileNotFoundError:
        print('File is not found')
    except ValueError:
        print('ValueError in the file')
    if len(salary_list) >= 1:
        for salary in salary_list:
            total += salary
        average = total / len(salary_list)
    return total, average
total, average = total_salary('./salary_proccessing/salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
