const functionTest = require('./1-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
  it('ADDITION IS COMPLETE', () => {
    assert.strictEqual(functionTest('SUM', 1, 3), 4);
    assert.strictEqual(functionTest('SUM', 1, 3.7), 5);
    assert.strictEqual(functionTest('SUM', 1.2, 3.7), 5);
    assert.strictEqual(functionTest('SUM', 1.5, 3.7), 6);
    assert.strictEqual(functionTest('SUM', 1.4, 4.5), 6);
    assert.strictEqual(functionTest('SUM', 1.4, 0), 1);
    assert.strictEqual(functionTest('SUM', 0, 1.4), 1);
  });
});

describe('calculateNumber', () => {
  it('SUBTRACTION IS COMPLETE', () => {
    assert.strictEqual(functionTest('SUBTRACT', 1, 3), -2);
    assert.strictEqual(functionTest('SUBTRACT', 1, 3.7), -3);
    assert.strictEqual(functionTest('SUBTRACT', 1.2, 3.7), -3);
    assert.strictEqual(functionTest('SUBTRACT', 1.5, 3.7), -2);
    assert.strictEqual(functionTest('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(functionTest('SUBTRACT', 1.4, 0), 1);
    assert.strictEqual(functionTest('SUBTRACT', 0, 1.4), -1);
  });
});

describe('calculateNumber', () => {
  it('DIVISION IS COMPLETE', () => {
    assert.strictEqual(functionTest('DIVIDE', 9, 3), 3);
    assert.strictEqual(functionTest('DIVIDE', 12, 3), 4);
    assert.strictEqual(functionTest('DIVIDE', 60, 5), 12);
    assert.strictEqual(functionTest('DIVIDE', 24, 3), 8);
    assert.strictEqual(functionTest('DIVIDE', 144, 12), 12);
    assert.strictEqual(functionTest('DIVIDE', 30, 5), 6);
    assert.strictEqual(functionTest('DIVIDE', 0, 1.4), 0);
    assert.strictEqual(functionTest('DIVIDE', 1.4, 0), 'Error');
  });
});
