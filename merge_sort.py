#!/usr/bin/env python
"""
Merge sort is an O(n log n) comparison-based sorting algorithm.

Most implementations produce a stable sort, which means that the implementation
preserves the input order of equal elements in the sorted output. Mergesort is a
divide and conquer algorithm that was invented by John von Neumann in 1945.

Conceptually, a merge sort works as follows:
  1) Divide the unsorted list into n sublists, each containing 1 element
     (a list of 1 element is considered sorted).
  2) Repeatedly merge sublists to produce new sorted sublists until there
     is only 1 sublist remaining. This will be the sorted list.

                        +---+---+---+---+
 unsorted array         | 2 | 0 | 3 | 1 |
                        +---+---+---+---+
                               / \
                              /   \
                             /     \
                    +---+---+       +---+---+
                    | 2 | 0 |       | 3 | 1 |
                    +---+---+       +---+---+
                       / \             / \
                      /   \           /   \
                 +---+     +---+ +---+     +---+
                 | 2 |     | 0 | | 3 |     | 1 |
                 +---+     +---+ +---+     +---+
                      \   /           \   /
                       \ /             \ /
                    +---+---+       +---+---+
                    | 0 | 2 |       | 1 | 3 |
                    +---+---+       +---+---+
                         \              /
                          \            /
                           \          /
                        +---+---+---+---+
sorted array            | 0 | 1 | 2 | 3 |
                        +---+---+---+---+

wiki: https://en.wikipedia.org/wiki/Merge_sort
"""
import cProfile


def merge_sort(as_list):
  """Merge Sort.

  Args:
    as_list: list, a list of numbers.
  Returns:
    sorted list list of numbers.
  """
  lenght_of_as_list = len(as_list)
  # Return the list if it only has one or zero items.
  if lenght_of_as_list <= 1:
    return as_list

  # find the middle index of the array.
  middle = lenght_of_as_list // 2

  # Divide the list in half.
  left = as_list[:middle]
  right = as_list[middle:]

  # Recursively call this function with each half of the array.
  left = merge_sort(left)
  right = merge_sort(right)

  # Call 'merge' and return the sorted and merged halfs.
  return merge(left, right)


def merge(left, right):
  """Merge.

  Args:
    left: list, a list of numbers.
    right: list, a list of numbers.
  Returns:
    sort and merge the two list 'left' and 'right'.
  """
  result = []
  i = j = 0

  # While list index is in of range i and j.
  while left[i:] and right[j:]:
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Extend the list with any reminding elements.
  if left[i:]:
    result.extend(left[i:])
  if right[j:]:
    result.extend(right[j:])

  return result


def tests():
  assert merge_sort([5,4,1,8,7,2,6,3]) == [1, 2, 3, 4, 5, 6, 7, 8]


if __name__ == '__main__':
  cProfile.run('tests()')
