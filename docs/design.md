# Design

This integration testing tool is implemented in Python, utilizing selenium via the Python selenium client, and webdriver manager to automatically download and utilize drivers for Chrome and Firefox.

The selection of Python was based on two primary factors:

- it is familiar to KBase developers; this tool is intended for testing KBase user interfaces
- it is simpler to use than, say, Javascript; primarily because the JS libraries expose the asynchronous nature of the selenium API, which complicates the code tremendously, and Python hides it behind a synchronous api.
 
Selenium is the defacto standard for providing a single api to mutiple browsers across multiple operating systems.

## Custom Methods

Tests are all contained in test classes, which must have a suffix of `Test` and be contained in a file prefixed by `test_`. Each test class must extend either unittest.TestCase, or another class which has unittest.TestCase as an ancestor class.

In actual usage, TestBase.py is the only class which extends unittest.TestCase, and serves as a base class for all tests. Some sets of tests may define their own testing base class.

This cascading class design allows us to provide a broad set of shared functionality as well as functionality of specific utility for certain sets of tests.

This allows our tests to be relatively free of direct webdriver api calls, and to focus on test abstract logic. Generally, whenever we find ourselves using the same pattern more then once, we want to make it available in the closest base class shared by all users of it. 