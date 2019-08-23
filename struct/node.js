/**
 * Node struct
 */

class Node {
  constructor(key, value) {
    this._key = key;
    this._value = value;
  }

  getKey() {
    return this._key;
  }

  getValue() {
    return this._value;
  }

  clone() {
    return new Node(this._key, this._value);
  }
}

module.exports = Node;
