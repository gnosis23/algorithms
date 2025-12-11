/**
 * quick sort algorithm
 */
function qsort(arr) {
  quickSort(arr, 0, arr.length - 1);
}

function quickSort(arr, low, high) {
  // at least length = 2
  if (low < high) {
    const pi = partition(arr, low, high);

    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}

// take last element as pivot
function partition(arr, low, high) {
  let pivot = Math.floor(Math.random() * (high - low)) + low;
  swap(arr, pivot, high);

  let orderedIndex = low;
  for (let i = low; i < high; ++i) {
    if (arr[i] <= arr[high]) {
      swap(arr, orderedIndex, i);
      orderedIndex++;
    }
  }

  swap(arr, orderedIndex, high);
  return orderedIndex;
}

function swap(arr, i, j) {
  if (i == j) return;
  const t = arr[i];
  arr[i] = arr[j];
  arr[j] = t;
}

module.exports = qsort;
