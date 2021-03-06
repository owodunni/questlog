# QuestLog
![build workflow](https://github.com/owodunni/questlog/actions/workflows/build.yml/badge.svg)
[![codecov](https://codecov.io/gh/owodunni/questlog/branch/main/graph/badge.svg?token=BS9JKHF65X)](https://codecov.io/gh/owodunni/questlog)
[![CodeFactor](https://www.codefactor.io/repository/github/owodunni/questlog/badge?s=d329caeaaf26b5eb59b20e109715684ba7476416)](https://www.codefactor.io/repository/github/owodunni/questlog)

When your party embarks on a quest it is best to keep a log of what to bring.



## Development

### Requirements

The following requirements are needed for development and not handled by this repo:
* JDK - gradle
* Python - development and sanitation
* Docker - CI

If you want to use a virtualenv run:

```
./gradlew venv && source .venv/bin/activate
```

### Setup

When starting to develop for the first time it is recommended to run:

```
./gradlew initialize
```

This will setup the following:

* pip
* commitizen
* pre-commit

### Commit style

We use [Commitizen](https://commitizen-tools.github.io/commitizen/) to lint our commits.
This is done with a pre-commit hook. ´cz´ is a helpful tool for getting the correct
commit style. To commit run:

```
cz c
```

### Formatting

We try to be strict with formatting, believing that clean code starts with a
uniform code base. To help we have two commands:

```
./gradlew spotlessCheck
./gradlew spotlessApply
```

The first command lints and the second command fixes.

## Develop

To build QuestLog simply run:

```
./gradlew assemble
```

This will assemble all projects and lint them.
