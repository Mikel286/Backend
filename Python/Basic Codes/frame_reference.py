import numpy as np

def change_fr(Point):

    r_matrix = np.array([[0,0,1],[-1,0,0],[0,-1,0]])
    traslate_vector = np.array([[0],[0],[-1]])

    A_vector = r_matrix @ Point + traslate_vector

    print("Las coordenadas de P en el marco {b} son:", A_vector)

def inverse_matrix():

    r_matrix = np.array([[0,0,1],[-1,0,0],[0,-1,0]])
    traslate_vector = np.array([[0],[0],[-1]])

    # Union of [r_matrix traslate_vector]
    homogenean_matrix = np.hstack((r_matrix, traslate_vector.reshape(3, 1)))
    homogenean_matrix = np.vstack((homogenean_matrix, np.array((0, 0, 0, 1)))) # Complete the matrix 4x4

    # Calculamos la matriz inversa
    inv_matrix = np.linalg.inv(homogenean_matrix)

    inv_rmatrix = inv_matrix[:3, :3]
    inv_tmatrix = inv_matrix[:3, 3]

    print("La matriz de rotacion R_b_s es:\n", inv_rmatrix, "\n")
    print("El vector de traslacion t_b_s es:", inv_tmatrix, "\n")

    # return of the inverse matrix of rotation (R^T) (t^T)
    return inv_rmatrix, inv_tmatrix

if __name__ == "__main__":

    change_fr((1,0,0))