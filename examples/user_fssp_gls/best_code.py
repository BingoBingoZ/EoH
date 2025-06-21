import numpy as np
def get_matrix_and_jobs(current_sequence, time_matrix, m, n):
    execution_time_ratio = np.max(time_matrix, axis=1) / np.min(time_matrix, axis=1)
    random_perturb_jobs = np.random.choice(n, m // 2, replace=False)
    ratio_based_perturb_jobs = np.argsort(execution_time_ratio)[-m // 2:]
       
    perturb_jobs = np.concatenate((random_perturb_jobs, ratio_based_perturb_jobs))
    new_matrix = time_matrix.copy()
    for job in perturb_jobs:
        perturbation = np.random.uniform(-0.2, 0.2) * new_matrix[job]
        new_matrix[job] += perturbation
    return new_matrix, perturb_jobs




# def get_matrix_and_jobs(current_sequence, time_matrix, m, n):
#     execution_time_ratio = np.max(time_matrix, axis=1) / np.min(time_matrix, axis=1)
#     random_perturb_jobs = np.random.choice(n, m // 2, replace=False)
#     ratio_based_perturb_jobs = np.argsort(execution_time_ratio)[-m // 2:]
    
#     perturb_jobs = np.concatenate((random_perturb_jobs, ratio_based_perturb_jobs))
#     new_matrix = time_matrix.copy()
#     for job in perturb_jobs:
#         perturbation = np.random.uniform(-0.2, 0.2) * new_matrix[job]
#         new_matrix[job] += perturbation
#     return new_matrix, perturb_jobs