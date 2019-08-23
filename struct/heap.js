/**
 * Heap struct
 * a forked version: https://github.com/google/closure-library/blob/master/closure/goog/structs/heap.js
 * 
 * smaller keys rise to the top
 */
const Node = require('./node');

class Heap {
  constructor({ cmp, defaultValue }) {
    this._nodes = [];
    this._cmp = cmp ? cmp : (a, b) => a < b;
    if (defaultValue) {
      this.insertAll(defaultValue);
    }
  }

  insert(key, value) {
    const node = new Node(key, value);
    const nodes = this._nodes;
    nodes.push(node);
    this._moveUp(nodes.length - 1);
  }

  insertAll(heap) {    
    if (heap instanceof Heap) {
      const nodes = heap._nodes;
      for (let i = 0; i < heap._nodes.length; ++i) {
        this.insert(nodes[i].getKey(), nodes[i].getValue());
      }
    } else {
      Object.keys(heap).forEach(key => {
        this.insert(key, heap[key]);
      });
    }
  }

  remove() {
    const nodes = this._nodes;
    const count = nodes.length;
    const rootNode = nodes[0];
    if (count <= 0) {
      return undefined;
    } else if (count === 1) {
      this.clear();
    } else {
      nodes[0] = nodes.pop();
      this._moveDown(0);
    }
    return rootNode.getValue();
  }

  peek() {
    const nodes = this._nodes;
    if (nodes.length === 0) {
      return undefined;
    }
    return nodes[0].getValue();
  }

  _moveDown(index) {
    const nodes = this._nodes;
    const count = nodes.length;

    const node = nodes[index];
    // has a child
    while (index < (count >> 1)) {
      const leftChildIndex = this._getLeftChildIndex(index);
      const rightChildIndex = this._getRightChildIndex(index);

      const smallerChildIndex = rightChildIndex < count  && 
        this._cmp(nodes[rightChildIndex].getKey(), nodes[leftChildIndex].getKey()) ?
        rightChildIndex :
        leftChildIndex;
      
      if (!this._cmp(nodes[smallerChildIndex].getKey(), node.getKey())) {
        break;
      }

      nodes[index] = nodes[smallerChildIndex];
      index = smallerChildIndex;
    }
    nodes[index] = node;
  }

  _moveUp(index) {
    const nodes = this._nodes;
    const node = nodes[index];

    while (index > 0) {
      const parentIndex = this._getParentIndex(index);
      if (!this._cmp(nodes[parentIndex].getKey(), node.getKey())) {
        nodes[index] = nodes[parentIndex];
        index = parentIndex;
      } else {
        break;
      }
    }
    nodes[index] = node;
  }

  _getLeftChildIndex(index) {
    return index * 2 + 1;
  }

  _getRightChildIndex(index) {
    return index * 2 + 2;
  }

  _getParentIndex(index) {
    return (index - 1) >> 1;
  }

  containsValue(val) {
    return this._nodes.some(x => x.getValue() === val);
  }

  containsKey(key) {
    this._nodes.some(x => x.getKey() === key);
  }

  getCount() {
    return this._nodes.length;
  }

  isEmpty() {
    return this._nodes.length === 0;
  }

  clear() {
    this._nodes = [];
  }
}

module.exports = Heap;
