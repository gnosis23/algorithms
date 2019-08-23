const Heap = require('../../struct/heap');

const heap = new Heap({
  cmp: (a, b) => a > b,
  defaultValue: {
    '4': 4,
    '0': 0,
    '8': 8,
    '1': 1,
    '2': 2,
    '3': 3,
  }
});

console.log(heap._nodes);
while(!heap.isEmpty()) {
  console.log(heap.peek());
  heap.remove();
}