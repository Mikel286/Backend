import numpy as np

def generate_matrix(array):
    matrix = np.array(array)
    print(f"The array is: {matrix}" + "\n")
    print(f"The shape is: {matrix.shape}" + "\n")

if __name__ == "__main__":
    array_r = [[0,0,1],[-1,0,0],[0,-1,0]]
    array_t = [[0],[0],[-1]]
    generate_matrix(array_r)
    generate_matrix(array_t)