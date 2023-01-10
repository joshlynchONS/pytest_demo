'use strict'
const config = require('conventional-changelog-conventionalcommits');

module.exports = config({
    "types": [
        { type: 'add', section: 'New Features' },
        { type: 'fix', section: 'Bugs' }
    ]
})
