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
        print('(q) Quit to main menu')
        choice = input("Enter your choice: ")
        if choice == '1': 
            while True:
                choice_1 =  input('(1) Show the most effective company\n(2) Show the least effective company\n(q) Quit to the preious choice\nEnter your choice:  ') 
                if choice_1 == '1':
                    max_productivity(df)
                elif choice_1 == '2':
                    min_productivity(df)
                elif choice_1 == 'q':
                    break
                else:
                    print('Incorrect choice')
        if choice == '2':
            total_production(df)
        elif choice == 'q':
            break
                
   

def option_single_company(df,order,salary_coefficient):

    company = IntArray(df[order])
    company.salary_coefficient = salary_coefficient
        

    while True:
        print('Choose option: ')
        print("(1) Sort company's products or salaries")
        print("(2) Plots")
        print('(q) Quit to main menu')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while True:
                choice_1 = input('(1) Sorted products of that company\n(2) Sorted salaries of that company: \n(q) Quit to the previous choice\nEnter your choice: ')
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
                choice_2 = input('(1) Plots of employees rank to their amount od products/month and their salaries\n(2) Plots of deviations\n(q) Quit to the previous choice\nEnter your choice: ')
                if choice_2 =='1':
                    print(company.show_data())
                elif choice_2 == '2':
                    print(company.std_deviation_analysis())
                elif choice_2 == 'q':
                    break
                else:
                    print('Incorrect choice')

        elif choice == 'q':
            break

        else:
            print('Incoorect choice')


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
    while True:
        print('Choose analysis type: ')
        print('(1) Analyze a single company')
        print('(2) Analyze all companies')
        print('(q) Quit program')

        analysis_type = input("Enter your choice: ")
        if analysis_type == '1':
            while True:            
                try:
                    company_index = int(input(f"Enter the company index (1 to {len(df)}): ")) - 1
                    if 0 <= company_index <len(df):
                        break
                    else:
                        print("Invalid company index. Please enter a valid index.")

                except (ValueError, IndexError):
                    print("Invalid input. Please enter valid indices")
                    continue

            while True:            
                try:
                    salary_coefficient = float(input("Enter the salary coefficient: "))
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Please enter valid coefficients.")
                    continue
            

            display_results(df,company_index,salary_coefficient)
            option_single_company(df,company_index,salary_coefficient)

        elif analysis_type == '2':
            while True:
                try:
                    salary_coefficient = float(input("Enter the salary coefficient: "))
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Please enter valid indices and coefficients.")
                    continue
                
            option_all_companies(df, salary_coefficient)
        
        elif analysis_type =='q':
            break
            

        else:
                print('Incoorect choice')
    

if __name__ == '__main__':
    main()
