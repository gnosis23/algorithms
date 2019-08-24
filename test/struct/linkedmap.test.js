const LinkedMap = require('../../struct/linkedmap');

var m = new LinkedMap();
m.set('param1', 'A');
m.set('param2', 'B');
m.set('param3', 'C');
console.log(m.getKeys());

var c = new LinkedMap(5, true);
for (var i = 0; i < 10; i++) {
  c.set('entry' + i, false);
}
console.log(c.getKeys());

c.set('entry5', true);
c.set('entry1', false);
console.log(c.getKeys());
