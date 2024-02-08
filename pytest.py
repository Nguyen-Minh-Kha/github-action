from average import calculate_average  # Replace "your_module" with the actual module name

def test_calculate_average_with_positive_numbers():
  """Tests the function with positive numbers."""
  result = calculate_average(10, 20)
  assert result == 15.0, "Average should be 15.0"

def test_calculate_average_with_negative_numbers():
  """Tests the function with negative numbers."""
  result = calculate_average(-5, -3)
  assert result == -4.0, "Average should be -4.0"

def test_calculate_average_with_zero():
  """Tests the function with one zero."""
  result = calculate_average(0, 10)
  assert result == 5.0, "Average should be 5.0"

def test_calculate_average_with_both_zeros():
  """Tests the function with both numbers as zero."""
  result = calculate_average(0, 0)
  assert result == 0.0, "Average should be 0.0"

def test_calculate_average_with_floats():
  """Tests the function with float numbers."""
  result = calculate_average(2.5, 4.3)
  assert result == 3.4, "Average should be 3.4"

def test_calculate_average_with_large_numbers():
  """Tests the function with large numbers."""
  result = calculate_average(1000000, 2000000)
  assert result == 1500000, "Average should be 1500000"
