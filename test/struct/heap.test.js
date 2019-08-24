const Heap = require('../../struct/heap');

const heap = new Heap({
  comparator: (a, b) => -(a - b),
});

for (let i of [[4, 4], [0, 0], [0, 0], [8, 8], [1, 1], [2, 2], [3, 3]]) {
  heap.insert(i[0], i[1]);
}

console.log(heap._nodes);

while(!heap.isEmpty()) {
  console.log(heap.peek());
  heap.remove();
}
