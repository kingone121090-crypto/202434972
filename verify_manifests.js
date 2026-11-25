// Checks fixture consistency only; does NOT run a vulnerability scanner.
const fs = require('node:fs');
const assert = require('node:assert/strict');
const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
const lock = JSON.parse(fs.readFileSync('package-lock.json', 'utf8'));
assert.equal(lock.lockfileVersion, 3);
for (const [name, version] of Object.entries(pkg.dependencies)) {
  assert.equal(lock.packages[''].dependencies[name], version);
  assert.equal(lock.packages['node_modules/' + name].version, version);
}
console.log('npm manifest/lockfile versions match.');
