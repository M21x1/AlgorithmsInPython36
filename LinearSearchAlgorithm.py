## Linear Search + finding duplicates

# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

## Finding the Maximum Value

# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

## including a wrong code (-1)

def linearSearch(searchList, targetValue):
  for i in range(len(searchList)):
    if (searchList[i] == targetValue):
      return i
  return -1

numberList = [ 1, 10, 23, 94, 23, 67 ]
linearSearch(numberList, 23)

## hich searches for elements in searchList that have values greater than targetValue

def greaterSearch(searchList, targetValue):
  result = []
  for i in range(len(searchList)):
    if (searchList[i] > targetValue):
      result.append(searchList[i])
  return result

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    # print(search_list[idx])
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index
    #if search_list[idx] == target_value:
    #  return idx
  #raise ValueError("{0} not in list".format(target_value))

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)

## simple linear search

# A list of the ingredients for tuna sushi
recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "tuna" #"avocado"

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

print(linear_search(recipe, target_ingredient))