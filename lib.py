def average_positive_values(values):
  """
  Calcule la moyenne des valeurs positives contenues dans une liste.

  Args:
    values: Une liste de nombres.

  Returns:
    La moyenne des valeurs positives de la liste, ou 0 si aucune valeur n'est positive.
  """
  positive_values = [value for value in values if value > 0]
  if positive_values:
    return sum(positive_values) / len(positive_values)
  else:
    return 0

