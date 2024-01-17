import numpy as np
import matplotlib.pyplot as plt


class IntArray:

    def __init__(self,int_array):        
        if not isinstance(int_array, (list, np.ndarray)) or not all(isinstance(val, int) for val in int_array):
            raise ValueError('Input must be a list or NumPy array of integers')
        self._salary_coefficient = None
        self.int_array = int_array

    @property
    def salary_coefficient(self):
        if self._salary_coefficient is None:
            raise ValueError('Salary coefficient must be set before accessing it')
        return self._salary_coefficient
    
    @salary_coefficient.setter
    def salary_coefficient(self,val):
        if not isinstance(val, (int,float)):
            raise ValueError('Salary coefficient must be a number')
        self._salary_coefficient = val
   
    def display(self):
        print(self.int_array)

    def salary(self):
        array_shape = self.int_array.shape
        money_per_product = np.full(array_shape, self.salary_coefficient)
        salaries = self.int_array * money_per_product
        return f'People made {np.array2string(self.int_array)} products an their salaries are {salaries}'
    
    def get_salaries(self):
        array_shape = self.int_array.shape
        money_per_product = np.full(array_shape, self.salary_coefficient)
        salaries = self.int_array * money_per_product
        return salaries

    
    def show_data(self):
        x = np.arange(len(self.int_array))
        y1 = self.int_array
        y2 = self.get_salaries()

        plt.subplot(1, 2, 1)
        plt.plot(x, y1, marker='o')
        plt.xlabel('Rank of employee')
        plt.ylabel('Products/month')
        plt.grid()
        plt.title('Employee - Products') 

        plt.subplot(1, 2, 2)
        plt.plot(x, y2, marker='o')
        plt.xlabel('Rank of employee')
        plt.ylabel('Salaries')
        plt.grid()
        plt.title('Employee - Salaries')
        
        plt.show()

    def std_deviation_analysis(self):
        x = np.arange(len(self.int_array))
        y1 = self.int_array
        y2 = self.get_salaries()

        plt.subplot(1, 2, 1)
        plt.plot(x, y1, marker='o')
        plt.xlabel('Rank of employee')
        plt.ylabel('Products/month')
        plt.axhline(np.mean(y2), color='red', linestyle='dashed', linewidth=2, label='Mean amount of products')
        plt.axhline(np.mean(y2) + np.std(y2), color='blue', linestyle='dashed', linewidth=2, label='Mean + Std Dev')
        plt.axhline(np.mean(y2) - np.std(y2), color='blue', linestyle='dashed', linewidth=2, label='Mean - Std Dev')
        plt.grid()
        plt.title('Employee - Products') 

        plt.subplot(1, 2, 2)
        plt.plot(x, y2, marker='o')
        plt.xlabel('Rank of employee')
        plt.ylabel('Salaries')
        plt.axhline(np.mean(y2), color='red', linestyle='dashed', linewidth=2, label='Mean Salary')
        plt.axhline(np.mean(y2) + np.std(y2), color='green', linestyle='dashed', linewidth=2, label='Mean + Std Dev')
        plt.axhline(np.mean(y2) - np.std(y2), color='green', linestyle='dashed', linewidth=2, label='Mean - Std Dev')
        plt.grid()
        plt.title('Employee - Salaries')

        plt.show()


    
  
        
    