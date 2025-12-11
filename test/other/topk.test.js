const topk = require('../../javascript/other/topk');

console.log(topk([4, 0, 0, 8, 1, 2, 3, 1, 2, 3], 5));
console.log(topk([4, 0, 0, 8, 1, 2, 3, 1, 2, 3], 4));
console.log(topk([4, 0, 0, 8, 1, 2, 3, 1, 2, 3], 3));
console.log(topk([4, 0, 0, 8, 1, 2, 3, 1, 2, 3], 2));
console.log(topk([4, 0, 0, 8, 1, 2, 3, 1, 2, 3], 1));

console.log(topk([1], 1));
console.log(topk([1], 2));

