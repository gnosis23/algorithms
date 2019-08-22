const quickSort = require('../../sort/quick-sort');
let arr = [4, 0, 0, 8, 1, 2, 3, 1, 2, 3];
quickSort(arr);
console.log(arr);

arr = [0];
quickSort(arr);
console.log(arr);

arr = [1, 0];
quickSort(arr);
console.log(arr);
