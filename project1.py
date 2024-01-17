import numpy as np 
from cd import IntArray
import matplotlib.pyplot as plt

def display_results(df,order,salary_coefficient):
    company_data = df[order]
    # print(f"Type of df[order]: {type(df[order])}")
    # print(f"Type of company_data: {type(company_data)}")
    company = IntArray(company_data)
    company.salary_coefficient = salary_coefficient

    print(f"\nBasic results for Company {order + 1}:")
    print(f"Salary Coefficient: {salary_coefficient}")
    print(f"Total Products: " , np.sum(company_data))
    print(f"Individual Salaries: {company.salary()}")

def option_all_companies(df, salary_coefficient): 

    while True:
        print('Choose option: ')
        print('1. Effectiveness of companies')
        print('2. Total production ')
        choice = input("Enter your choice: ")
        if choice == '1': 
            while True:
                choice_1 =  input('Show the most (1) or the least (2) effective company') 
                if choice_1 == '1':
                    max_productivity(df)
                elif choice_1 == '2':
                    min_productivity(df)
                elif choice_1 == 'q':
                    break
                else:
                    print('Incorrect choice')
        if choice == '2':
            while True:
                total_production(df)
                break
        elif choice == 'q':
            return
                



    

def option_single_company(df,order,salary_coefficient):

    company = IntArray(df[order])
    company.salary_coefficient = salary_coefficient
        

    while True:
        print('Choose option: ')
        print("1. Sort company's products or salaries")
        print("2. Plots")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while True:
                choice_1 = input('Do you wanna see the sorted products (1) or salaries (2) of that company?: ')
                if choice_1 == '1':
                    df_sorted = np.sort(df[order])
                    print(df_sorted)
                elif choice_1 == '2':
                    gs = company.get_salaries()
                    gs_sorted = np.sort(gs)
                    print(gs_sorted)
                elif choice_1 == 'q':
                    break
                else:
                    print('Incorrect choice')
            
        elif choice == '2':
            while True:
                choice_2 = input('Do you wanna see the plots of employees rank to their amount od products/month (1) and their salaries or plots of deviations? (2)')
                if choice_2 =='1':
                    print(company.show_data())
                elif choice_2 == '2':
                    print(company.std_deviation_analysis())
                elif choice_2 == 'q':
                    break
                else:
                    print('Incorrect choice')

        elif choice == 'qq':
            break

        else:
            print('Incoorect choice')


    
# def summ(order,df):
#     return np.sum(df[order])

def max_productivity(df):
    best_index = np.argmax(np.sum(df, axis=1)) 
    num_of_products = np.sum(df[best_index])
    print(f'The best company is {best_index + 1} company with {num_of_products} products')



def min_productivity(df):
    worst_index = np.argmin(np.sum(df, axis=1)) 
    num_of_products = np.sum(df[worst_index])
    print(f'The worst company is {worst_index + 1} company with {num_of_products} products')

def total_production(df):
    total_prod = np.sum(df, axis=1)
    total_sum = np.sum(total_prod)
    print(f"Total production of all companies: {total_sum}")


def file_handling():

    lines = []

    with open('comp.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values]
            lines.append(int_values)

        df = np.array([np.array(row) for row in lines], dtype='object')
        return df
        

    
def main():

    df = file_handling()

    print('Choose analysis type: ')
    print('1. Analyze a single company')
    print('2. Analyze all companies')

    analysis_type = input("Enter your choice: ")
    if analysis_type == '1':
        
        try:
            company_index = int(input(f"Enter the company index (1 to {len(df)}): ")) - 1
            salary_coefficient = float(input("Enter the salary coefficient: "))
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid indices and coefficients.")
        

        if not (0 <= company_index <len(df)):
            print("Invalid company index. Please enter a valid index.")

        display_results(df,company_index,salary_coefficient)
        option_single_company(df,company_index,salary_coefficient)

    elif analysis_type == '2':

        try:
            salary_coefficient = float(input("Enter the salary coefficient: "))
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid indices and coefficients.")
        
        option_all_companies(df, salary_coefficient)

        

    else:
            print('Incoorect choice')
    
    


    # base = file_handling()
    # user_salary_coefficient = float(input('Enter the salary coefficient: '))
    # first_br = IntArray(base[0])
    # first_br.salary_coefficient = user_sa
    # lary_coefficient
    # first_br.display()
    # first_br.show_data()
    # print(first_br.salary())
    
    # max_productivity(base)
    # min_productivity(base)
if __name__ == '__main__':
    main()
