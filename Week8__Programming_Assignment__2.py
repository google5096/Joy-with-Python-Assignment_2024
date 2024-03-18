def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"
 
    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    del M[i]
    for m in range(len(M)):
      del M[m][j]
    return(M)