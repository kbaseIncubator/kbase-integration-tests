# Testing Philosophy

The core tenet of these integration tests is to ensure that the user interfaces they interact with are behaving as intended, from the user's point of view.

We aim to have tests rely as much as possible on external behavior and appearance. 

We want to minimize any reliance on internal structure.

We want the tests resilient across implementations of the interface, as much as possible.

Why? 

Internal structure is not something that users are generally aware of. It is also an internal implementation detail that may change at any time, either due to intentional changes, or even changes in external libraries.

We do want to utilize certain aspects of apparent structure. This is because this is how users perceive the interface. When a tab is opened, content appears in a specific area. We should test the assertion that the content which should appear does appear, and in the desired area of the display. 

So we can set up tests that rely on tabs, panels, tables of various sorts, that click buttons and links. All of these interface pieces have a sort of structure that is recognized by users, and implemented in some way internally.

Unfortunately there are no high level concepts in web browsers that capture these abstractions. So we must rely on some general rules for semantic structure. Note that we try to utilize _semantic_ structure and not _implementation details_. But we are practical, too, and sometimes we must do both.

For example, tabs. Tabs have many implementations, but common behavior across all. It is not always appropriate to utilize the same implementation everywhere, even in the same codebase. Sometimes a framework we use requires too much overriding to provide some situational layout or behavior.

For a commonly used library like Bootstrap, we can rely on it's published structure, including class names. We don't necessarily want to bind to such details, but we often must because we may not have enough control over individual elements (see next paragraph.) 

For our own components, however, we can utilize either semantic tags, role attributes, or even data- attributes. We can also try to retrofit these onto frameworks which do not already support them.

Taking the tabs example, our tabs implementation should use role="tablist" for the tab container, role="tab" for an individual tab selection button thing, and role="tabpanel" for the tab content area. This allows our testing code to navigate through the tabs without binding to specific dom node pathways, classes, or other implementation details.

## Status

Currently the codebase is a mixture of behavioral and semantic tests and implementation-detail dependent tests. The goal is to have them all move away from relying upon implementation details.



