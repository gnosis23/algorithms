/**
 * LinkedMap
 * 
 * forked: https://github.com/google/closure-library/blob/master/closure/goog/structs/linkedmap.js
 * 
 */

class LinkedMap {
  constructor(optMaxCount, optCache) {
    this._maxCount = optMaxCount || null;

    this._cache = !!optCache;

    this._map = new Map();

    this._head = new _Node('', undefined);
    this._head.next = this._head.prev = this._head;
  }

  get(key, optVal) {
    const node = this._findAndMoveToTop(key);
    return node ? node.value : optVal;
  }

  peekValue(key, optVal) {
    const node = this._map.get(key);
    return node ? node.value : optVal;
  }

  set(key, value) {
    let node = this._findAndMoveToTop(key);
    if (node) {
      node.value = value;
    } else {
      node = new _Node(key, value);
      this._map.set(key, node);
      this._insert(node);
    }
  }

  peek() {
    this._head.next.value;
  }

  peekLast() {
    return this._head.prev.value;
  }

  pop() {
    this._popNode(this._head.prev);
  }

  remove(key) {
    const node = this._map.get(key);
    if (node) {
      this.removeNode(node);
      return true;
    }
    return false;
  }

  removeNode(node) {
    node.remove();
    this._map.delete(node.key);
  }

  getCount() {
    return this._map.size;
  }

  isEmpty() {
    return this._map.size === 0;
  }

  getKeys() {
    return this.map((val, key) => key);
  }

  getValues() {
    return this.map((val) => val);
  }

  map(f, optObj) {
    const rv = [];
    for (let n = this._head.next; n != this._head; n = n.next) {
      rv.push(f.call(optObj, n.value, n.key, this));
    }
    return rv;
  }

  contains(key) {
    return this._map.has(key);
  }

  clear() {
    this._truncate(0);
  }

  _findAndMoveToTop(key) {
    const node = this._map.get(key);
    if (node) {
      if (this._cache) {
        node.remove();
        this._insert(node);
      }
    }
    return node;
  }

  _insert(node) {
    if (this._cache) {
      node.next = this._head.next;
      node.prev = this._head;

      this._head.next = node;
      node.next.prev = node;
    } else {
      node.prev = this._head.prev;
      node.next = this._head;

      this._head.prev = node;
      node.prev.next = node;
    }

    if (this._maxCount != null) {
      this._truncate(this._maxCount);
    }
  }

  _truncate(count) {
    while (this.getCount() > count) {
      const toRemove = this._cache ? this._head.prev : this._head.next;
      this.removeNode(toRemove);
    }
  }

  _popNode(node) {
    if (this._head != node) {
      this.removeNode(node);
    }
    return node.value;
  }
}

class _Node {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }

  remove() {
    this.prev.next = this.next;
    this.next.prev = this.prev;
    this.prev = null;
    this.next = null;
  }
}

module.exports = LinkedMap;
