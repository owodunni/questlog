# QuestLog
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
