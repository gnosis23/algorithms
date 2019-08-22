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
  const pivot = arr[high];

  let i = low - 1;
  for (let j = low; j < high; j++) {
    if (arr[j] <= pivot) {
      i++;
      swap(arr, i, j);
    }
  }

  swap(arr, i + 1, high);
  return i + 1;
}

function swap(arr, i, j) {
  if (i == j) return;
  const t = arr[i];
  arr[i] = arr[j];
  arr[j] = t;
}

module.exports = qsort;
