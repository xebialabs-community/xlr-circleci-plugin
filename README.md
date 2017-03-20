# xlr-circleci-plugin

This plugin offers an interface from XL Release to Circle CI. 

# CI status #

[![Build Status][xlr-circleci-plugin-circleci-image]][xlr-circleci-plugin-circleci-url]
[![Build Status][xlr-circleci-plugin-travis-image]][xlr-circleci-plugin-travis-url]
[![Codacy Badge][xlr-circleci-plugin-codacy-image] ][xlr-circleci-plugin-codacy-url]
[![Code Climate][xlr-circleci-plugin-code-climate-image] ][xlr-circleci-plugin-code-climate-url]

[xlr-circleci-plugin-circleci-image]: https://circleci.com/gh/xebialabs-community/xlr-circleci-plugin.svg?style=shield
[xlr-circleci-plugin-circleci-url]: https://circleci.com/gh/xebialabs-community/xlr-circleci-plugin
[xlr-circleci-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-circleci-plugin.svg?branch=master
[xlr-circleci-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-circleci-plugin
[xlr-circleci-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/a76c515de76640fc9e1f282575382937
[xlr-circleci-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xlr-circleci-plugin
[xlr-circleci-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xlr-circleci-plugin/badges/gpa.svg
[xlr-circleci-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xlr-circleci-plugin

# Development #

* Start XLR: `./gradlew runDockerCompose`

# Type definitions #
+ `circleci.Server`: Defines your Circle CI endpoint to be used.
    + `username`: Use this property to define the token as described in [Authentication](https://circleci.com/docs/api/#authentication)
+ `circleci.GetUser`: Provides information about the signed in user
    + Implements the api call as described in [User](https://circleci.com/docs/api/#user)
+ `circleci.TriggerBuild`: Triggers a build of the specified project and branch.
    + Implements the api call as described in [Trigger a new Build with a Branch](https://circleci.com/docs/api/#new-build-branch)
    
# References #
[Circle CI api](https://circleci.com/docs/api/)

