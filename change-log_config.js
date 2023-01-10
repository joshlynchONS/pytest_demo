'use strict'
const config = require('conventional-changelog-conventionalcommits');

module.exports = config({
    "types": [
        { type: 'added', section: 'New Features' },
        { type: 'fixed', section: 'Bugs' }
    ]
})
