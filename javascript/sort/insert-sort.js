/**
 * 插入排序
 */
function insertSort(arr) {
  for (let i = 1; i < arr.length; ++i) {
    let val = arr[i];
    let j;
    for (j = i - 1; j >= 0; --j) {
      if (arr[j] > val) {
        arr[j + 1] = arr[j];
      } else {
        break;
      }
    }
    arr[j + 1] = val;
  }
}

module.exports = insertSort;
