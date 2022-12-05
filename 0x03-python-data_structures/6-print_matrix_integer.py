x_integer(matrix=[[]]):
    for element in matrix:
        print(" ".join("{:d}".format(value) for value in element))
