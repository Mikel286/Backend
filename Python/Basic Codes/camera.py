import numpy as np
from frame_reference import inverse_matrix

def frame_camera(P_array):

    inv_rmatrix, inv_tmatrix = inverse_matrix()
    frame_camera_points = P_array @ inv_rmatrix + inv_tmatrix

    mask = frame_camera_points[:,2]>0
    filtered_points = frame_camera_points[mask]
    print(filtered_points.shape)

if __name__ == "__main__":

    

    ## Open the file data/points_all.npy
    lidiar_points = np.load("data/points_all.npy")
    print(lidiar_points.shape)
    frame_camera(lidiar_points)