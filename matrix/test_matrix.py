from matrix import build_matrix, find_sequence_by_column, find_sequence_by_row

def get_matrix():
  matrixList = []
  matrixList.append(
    {'matrix':[[3,3,7,8,9],[3,3,7,9,9],[4,3,4,5,6],[5,5,3,11,5],[6,5,3,5,5]],
    'expected_col_seq':[[[1, 0], [4, 0]]],
    'expected_row_seq':[[[2, 1], [2, 4]]]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[1,1,1,1,1],[2,2,2,2,2],[1,1,1,1,1]],
    'expected_col_seq':[],
    'expected_row_seq':[]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[3,5,3,9,8],[4,4,7,8,9],[0,0,0,0,0]],
    'expected_col_seq':[[[0, 0], [3, 0]]],
    'expected_row_seq':[]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[1,2,3,4,4],[2,2,2,2,2],[1,1,1,1,1]],
    'expected_col_seq':[],
    'expected_row_seq':[[[2, 0], [2, 3]]]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[1,2,3,4,5],[2,2,2,2,2],[1,1,1,1,1]],
    'expected_col_seq':[],
    'expected_row_seq':[[[2, 0], [2, 3]],[[2, 1], [2, 4]]]})
  return matrixList

def test_build_matrix_dimension():
  matrix = build_matrix()
  number_of_rows = len(matrix)
  assert 5 == number_of_rows, f"Expected 5 rows but got {number_of_rows}"
  for row in matrix:
    number_of_columns = len(row)
    assert 5 == number_of_columns, f"Expected 5 columns but got {number_of_columns}"

def test_build_matrix_type_values():
  matrix = build_matrix()
  for row in matrix:
    for element in row:
      assert isinstance(element, int), f"Expected matrix elements to be int but got {type(element)}"

def test_find_sequence_by_column():
  for e in get_matrix():
    matrix = e['matrix']
    expected = e['expected_col_seq']
    ouput = find_sequence_by_column(matrix)
    assert ouput == expected, f"Expected column sequence to be {expected} but got {ouput} for matrix {matrix}"

def test_find_sequence_by_row():
  for e in get_matrix():
    matrix = e['matrix']
    expected = e['expected_row_seq']
    ouput = find_sequence_by_row(matrix)
    assert ouput == expected, f"Expected row sequence to be {expected} but got {ouput} for matrix {matrix}"
