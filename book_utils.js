// Illustrative library UI helpers. Vulnerable package versions are declared
// in the root npm lockfile for SCA evaluation. No exploit examples are included.
const _ = require('lodash');
const minimist = require('minimist');

function normalizeTitles(books) {
  return _.sortBy(books.map(({ title }) => title.trim()), value => value.toLowerCase());
}

function parseLibraryOptions(argv) {
  return minimist(argv, { string: ['search'], boolean: ['all'] });
}

module.exports = { normalizeTitles, parseLibraryOptions };
