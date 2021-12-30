// The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

// maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4});
// //should be 6: {4, -1, 2, 1}
// Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is
// made up of only negative numbers, return 0 instead.

// Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

#include <vector>
using namespace std;
int maxSequence(const std::vector<int>& arr){
  if (arr.size() == 0) {
    return 0;
  }
  bool met_positive = false;
  for (unsigned int i = 0; i < arr.size(); i++) {
    if (arr[i] > 0) {
      met_positive = true;
      break;
    }
  }
  if (!met_positive) {
    return 0;
  }
  int max = arr[0];
  int sum_runner;
  
  for (unsigned int i = 0; i < arr.size(); i++) {
    for (unsigned int j = i; j < arr.size(); j++) {
      sum_runner += arr[j];
      if (sum_runner > max) {
        max = sum_runner;
      }
    }
    sum_runner = 0;
  }
  return max;
}
