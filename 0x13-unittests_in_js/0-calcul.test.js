const functionTest = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
  it('returns rounded sum', () => {
    assert.strictEqual(functionTest(1, 3), 4);
    assert.strictEqual(functionTest(1, 3.7), 5);
    assert.strictEqual(functionTest(1.2, 3.7), 5);
    assert.strictEqual(functionTest(1.5, 3.7), 6);
    assert.strictEqual(functionTest(1.4, 4.5), 6);
    assert.strictEqual(functionTest(1.4, 0), 1);
    assert.strictEqual(functionTest(0, 1.4), 1);
  });
});
