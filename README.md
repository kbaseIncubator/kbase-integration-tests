# KBase Integration Tests

Run integration tests against KBase user interfaces with Python. Tests currently support kbase-ui, kbase-ui plugins, a bit of Narratives Navigator.

## Quick Start

Tests are run on your host machine, against an instance of a KBase user interface running locally or remotely.

This project is Python 12 based, and uses [poetry](./docs/using-poetry.md) to manage and install dependencies,
and to run the tool itself.

In order to use this project you will need [poetry](https://python-poetry.org/docs/),
which itself requires Python. Installation of poetry [is
documented](./docs/using-poetry.md), but if things get sticky, you should
consult the upstream [poetry docs](https://python-poetry.org/docs/)

Once poetry is installed, from the repo root:

```shell
poetry shell
poetry install
```

then  

```shell
 PYTHONPATH="$PWD" KBASE_TOKEN=<KBaseToken> poetry run pytest ./tests
 ```

where:

- `PYTHONPATH` should be set to repo root directory
- `KBASE_TOKEN` is a KBase Login, Dev, or other auth token for the account for which test data has been generated

Note that currently the test data is owned by the user `kbaseuitest` and is not public. This account has no additional authorization scopes, so the only token available for this account is a Login token. Please ask the UI team for a token for this account.

This will run the tests against `https://ci.kbase.us`. If you are not running a local
copy of kbase-ui with `ci.kbase.us` proxied to it, the tests will run against the actual `ci`
runtime managed by the [KBase project](https://www.kbase.us).

### Fine Tuning Tests

For repeated test runs, it is recommended to export environment variables one time.

```shell
 export PYTHONPATH="$PWD"
 export KBASE_TOKEN=<KBaseToken> 
  ```

then to run tests separately

```shell
 poetry run pytest ./tests
```

To focus tests you may simply narrow the scope for discovery, even down to the
individual file. E.g. this will run just the dataview plugin tests:

```shell
 poetry run pytest ./tests/plugins/dataview
```

or this will run just the feeds plugin tests:

```shell
 poetry run pytest ./tests/plugins/test_feeds.py
```

### Optional environment variables

- `GH_TOKEN` is a GitHub Personal Access Token (PAT); although optional, it is required if you run many tests and hit the rate limiting imposed by GitHub
- `KBASE_ENV` is the KBase deployment environment, `ci`, `next`, `appdev`, `narrative-dev` or `prod`; defaults to ci
- `HEADLESS` if set to `t` will run the browser headless, set to `f` it will open the actual browser ui; defaults to `t`
- `BROWSER` if set will determine the browser to run tests in, `firefox` and `chrome` are available; defaults to `chrome`
- `TIMEOUT` if set indicates the test timeout in seconds; defaults to `30`.

> NOTE: `KBASE_ENV` is not fully supported yet.

For example, it is common when debugging tests to run non-headless:

```shell
HEADLESS=f poetry run pytest ./tests/kbase_ui/plugins/test_feeds.py
```

or to run in a different browser, for perspective:

```shell
BROWSER=firefox HEADLESS=f poetry run pytest ./tests/kbase_ui/plugins/test_feeds.py
```

### GitHub Token

If you run tests repeatedly, you may begin to have test failures due to GitHub rate limiting. The tests rely upon  [`webdriver_manager`](https://github.com/SergeyPirogov/webdriver_manager), which eases the process of test configuration by automatically downloading the latest browser for the current platform. It downloads them from the browsers from their published locations, which is predominantly, if not wholly, GitHub. GitHub rate-limits public downloads. The rate is approximately 60/hour, but it may vary and GitHub does make any promises about the rate limit. To get around this limitation and potential for aggravation, a GitHub Token may be used. For a developer, this means creating a Personal Access Token (PAT) from their GitHub account. The PAT just needs to have `public_repo` scope.

## Running against local or remote

When working on adding, updating, or fixing tests it is most efficacious to run the tests against a local instance of the interface being evaluated.

For kbase-ui this is quite natural, as kbase-ui development includes a proxy to any KBase deployment environment, including proxying all other KBase user interfaces.

When tests are not under development, and are being used to verify kbase-ui or other another interface prior to release, tests should be run against the remote. I would recommend running the tests against a deployment of the pre-release image, and also after the release image is built. This is especially useful if the tests have been updated for new features, and would fail if run against the previous version of the interface.

## Instability of test targets

Integration tests rely up on user interfaces being populated data outside of their control. Data sources include KBase services, e.g. workspace, and third party services, e.g. pubmed. These data source are not static, and therefore, on occasion tests will fail for no good reason other than that data having changed. In such circumstances, the data should be investigated, resulting most likely in changes to test data to get tests passing again. When one does this, please take care to visually verify the data changes in situ.

For example, pubmed records may be changed. In one instance the publications table for the Genome landing page broke when an author name was modified. This was for a relatively recent publication (within the last year), but this does indicate that these records are not considered immutable once published.

### Workspace data

All workspace data should be owned by the test user, `kbaseuitest`, and only shared with other test user accounts.

## Running tesAts from a container

It is preferable to run code like these tests from inside a Docker container. This provides the optimal isolation, reproducibility, and is easier on developers and for us to support.

However, experiments so far are not encouraging. The primary problem seems to be the reliability of browsers available within a container. I suspect that once we solve the problem of reliably using headless browsers inside a container this will be the preferred or at least default way to run tests.

Nevertheless, some local host support will be required to run tests since this gives the best control over browsers, e.g. running non-headless.

Here is how I can begin to get tests running in a container. So far, I've managed to get tests running for Firefox, with 5 tests failing (have not repeated, so I'm sure that number will vary).

1. First start the container

    ```shell
    docker compose run tests  
    ```

    Currently, the container just starts `bash`, to ease the manual process described here.

2. From inside container, get the ip of the internal network which is that of the host

   ```shell
   python tools/hostname-ip.py host.docker.internal
   ```

3. then add this to /etc/hosts

   ```shell
   apt-get install vim
   vi /etc/hosts
   ```

   and add the line

   ```text
   IP_ADDRESS ci.kbase.us
   ```

   where `IP_ADDRESS` was the address returned from step 2.

## Running against a testing service

In order to perform cross-browser, cross-browser-version, and cross-os testing, a testing service (or a small army of QA testers) is required.

Although we've set up integration testing through a testing service, this has not been implemented in this project yet.
