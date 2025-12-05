import numpy as np

def main():
    """print(f"0 * np.nan is {0 * np.nan}")
    print(f"np.nan == np.nan is {np.nan == np.nan}")
    print(f"np.inf > np.nan is {np.inf > np.nan}")
    print(f"np.nan - np.nan is {np.nan - np.nan}")
    print(f"np.nan in set([np.nan]) is {np.nan in set([np.nan])}")
    print(f"0.3 == 3 * 0.1 is {0.3 == 3 * 0.1}")"""
    
    """matrix_a = np.diag([1, 2, 3, 4], k=-1)
    print(matrix_a)"""

    """elem = np.diag([1, 1])
    chessfield = np.tile(elem, (4, 4))
    print(chessfield)"""

    """a = np.random.rand(5, 3)
    b = np.random.rand(3, 2)
    print(a.dot(b))"""

    #print(np.arange('2016-07', '2016-08', dtype='datetime64[D]'))

    #print(np.random.randint(0, 4, (5, 5)))

    #print(np.random.rand(10))

    """int_types = [np.int8, np.int16, np.int32, np.int64, np.uint, np.uint8, np.uint16, np.uint32, np.uint64]
    for elem in int_types:
        print(f"type: {elem}, min_value: {np.iinfo(elem).min}, max_value: {np.iinfo(elem).max}")"""
    """matrix = np.random.randint(-3, 3, (3, 3))
    print(matrix)
    n = 2
    sorted_indices = np.argsort(matrix[:, n])
    matrix = matrix[sorted_indices]
    print(matrix)"""

    """a = np.array([[0, np.nan, 6],
                 [9, np.nan, np.nan]])

    nan_mask = np.isnan(a)
    print(np.any(np.all(nan_mask, axis=0)))"""



if __name__ == "__main__":
    main()