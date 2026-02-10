# ========================
# IMPORT LIBRARIES
# ========================
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

sns.set()

# ========================
# NUMPY EXAMPLES
# ========================

# --- Creating arrays ---
python_list = [1,2,3,4,5]
numpy_array_from_list = np.array(python_list)
numpy_array_from_list_float = np.array(python_list, dtype=float)
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)

# --- Convert numpy to list ---
np_to_list = numpy_array_from_list.tolist()
two_dim_list_to_list = numpy_two_dimensional_list.tolist()

# --- Numpy from tuple ---
python_tuple = (1,2,3,4,5)
numpy_array_from_tuple = np.array(python_tuple)

# --- Shape and size ---
nums = np.array([1,2,3,4,5])
three_by_four_array = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

# --- Data type and conversion ---
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
numpy_int_arr = np.array([1,2,3,4], dtype='float')
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

# --- Mathematical Operations ---
arr = np.array([1,2,3,4,5])
print('Addition:', arr+10)
print('Subtraction:', arr-10)
print('Multiplication:', arr*10)
print('Division:', arr/10)
print('Modulus:', arr%3)
print('Floor Division:', arr//10)
print('Exponential:', arr**2)

# --- Multi-dimensional array access ---
two_dimension_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('First row:', two_dimension_array[0])
print('Second column:', two_dimension_array[:,1])
print('Slicing:', two_dimension_array[0:2,0:2])
print('Reverse rows/columns:', two_dimension_array[::-1,::-1])

# --- Missing values ---
two_dimension_array[1,1] = 55
two_dimension_array[1,2] = 44

# --- Zeros and Ones ---
numpy_zeroes = np.zeros((3,3), dtype=int)
numpy_ones = np.ones((3,3), dtype=int)
numpy_twos = numpy_ones * 2

# --- Reshape and flatten ---
first_shape = np.array([(1,2,3),(4,5,6)])
reshaped = first_shape.reshape(3,2)
flattened = reshaped.flatten()

# --- Horizontal and Vertical Stack ---
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print('Horizontal Append:', np.hstack((np_list_one,np_list_two)))
print('Vertical Append:', np.vstack((np_list_one,np_list_two)))

# --- Random Numbers ---
rand_float = np.random.random()
rand_floats = np.random.random(5)
rand_int = np.random.randint(0,10, size=(3,3))
rand_normal = np.random.normal(79,15,80)

# --- Statistics with numpy ---
two_dimension_array = np.array([[1,2,3],[4,55,44],[7,8,9]])
print('Min:', np.min(two_dimension_array))
print('Max:', np.max(two_dimension_array))
print('Mean:', np.mean(two_dimension_array))
print('Std:', np.std(two_dimension_array))
print('Row min:', np.amin(two_dimension_array, axis=1))
print('Column max:', np.amax(two_dimension_array, axis=0))

# --- Repeating sequences ---
a = [1,2,3]
print('Tile:', np.tile(a,2))
print('Repeat:', np.repeat(a,2))

# --- Dot Product ---
f = np.array([1,2,3])
g = np.array([4,5,3])
print('Dot product:', np.dot(f,g))

# --- Matrix multiplication ---
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
print('Matrix multiplication:', np.matmul(h,i))
print('Determinant of i:', np.linalg.det(i))

# --- Chessboard pattern ---
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

# --- Linear Equation ---
temp = np.array([1,2,3,4,5])
pressure = temp*2 + 5
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.show()

# --- Gaussian Normal Distribution ---
mu, sigma, samples = 28, 15, 100000
x = np.random.normal(mu, sigma, samples)
ax = sns.histplot(x, bins=50)
ax.set(xlabel="x", ylabel='Frequency')
plt.show()


# ========================
# PANDAS EXAMPLES
# ========================
# Reading hacker_news.csv
df = pd.read_csv('data/hacker_news.csv')

# Basic exploration
print(df.head())
print(df.tail())
print(df['title'])
print(df.shape)

# Filter titles
print(df[df['title'].str.contains('Python', case=False)])
print(df[df['title'].str.contains('JavaScript', case=False)])
