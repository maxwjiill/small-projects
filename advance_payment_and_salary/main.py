def get_salary(monthly_salary: float) -> float:
    percent_for_advanced_payment = 0.35
    percent_for_salary = 0.65

    salary_after_tax = monthly_salary*0.87

    print(f'Advanced payment - {salary_after_tax*percent_for_advanced_payment}\nSalary - {salary_after_tax*percent_for_salary}')



if __name__ == '__main__':
    # salary before tax
    monthly_salary = float(input())

    get_salary(monthly_salary=monthly_salary)