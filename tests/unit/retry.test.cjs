const test = require('node:test');
const assert = require('node:assert/strict');


test('retry helper resolves successful callback', async () => {
  const { retry } = require('../../utils/retry');
  let attempts = 0;
  const value = await retry(async () => {
    attempts += 1;
    if (attempts < 2) throw new Error('transient');
    return 'ok';
  }, { attempts: 3, delayMs: 1 });
  assert.equal(value, 'ok');
  assert.equal(attempts, 2);
});

test('env loader merges defaults', () => {
  const { buildRuntimeConfig } = require('../../utils/env');
  const config = buildRuntimeConfig({ BASE_URL: 'http://localhost:4723' });
  assert.equal(config.baseUrl, 'http://localhost:4723');
  assert.equal(config.platforms.android.parallel, true);
});
