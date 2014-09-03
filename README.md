Bouncer Tests for download.allizom.org

Thank you for checking out Mozilla's Bouncer test suite. Mozilla and Web QA team are grateful for the help and hard work of many contributors like yourself. The following contributors have submitted pull requests to Bouncer-Tests:

https://github.com/mozilla/Bouncer-Tests/contributors
Getting involved as a contributor

We love working with contributors to fill out the test coverage for Bouncer-Tests, but it does require a few skills. You will need to know some Python and you will need some basic familiarity with Github

If you need to brush up on programming but are eager to start contributing immediately, please consider helping us find bugs in Mozilla Firefox or find bugs in the Mozilla web-sites tested by the WebQA team.

To brush up on Python skills before engaging with us, Dive Into Python is an excellent resource. MIT also has lecture notes on Python available through their open courseware.The programming concepts you will need to know include functions, working with classes, and some object oriented programming basics.
Questions are always welcome

While we take pains to keep our documentation updated, the best source of information is those of us who work on the project. Don't be afraid to join us in irc.mozilla.org #mozwebqa to ask questions about Bouncer Tests. Mozilla also hosts the #mozillians chat room to answer your general questions about contributing to Mozilla.
How to Set up and Build Bouncer Tests Locally

This repository contains tests suite used to test the mozilla's Bouncer

Mozilla maintains a guide to running Automated tests on our QMO website:

https://quality.mozilla.org/docs/webqa/running-webqa-automated-tests/
You will need to install the following:
Git

If you have cloned this project already then you can skip this! GitHub has excellent guides for Windows, MacOSX and Linux.
Python

Before you will be able to run these tests you will need to have Python 2.6 installed.

Install pip (for managing Python packages):

sudo easy_install pip

Installing dependencies

If you are using virtualenv, create and activate the virtualenv, then run the following in the project root:

pip install -r requirements.txt

If you are not using virtualenv, run the following in the project root to install dependencies globally:

sudo pip install -r requirements.txt

For more information on virtualenv, see below.
Running tests locally

To run these tests, use:

py.test --baseurl="http://download.allizom.org"

Use -k to run a specific test. eg : py.test -k test_that_checks_redirect_using_incorrect_query_values --baseurl="http://download.allizom.org"

The mozwebqa plugin has advanced command line options for reporting and using browsers. To see the options available, try running:

py.test --help

Also see the documentation on davehunt's pytest-mozwebqa Github project page.
Virtualenv and Virtualenvwrapper (Optional/Intermediate level)

While most of us have had some experience using virtual machines, virtualenv is something else entirely. It's used to keep libraries that you install from clashing and messing up your local environment. After installing virtualenv, installing virtualenvwrapper will give you some nice commands to use with virtualenv.

For a more detailed discussion of virtualenv and virtualenvwrapper, check out our quickstart guide and also this blog post.
Moz-grid-config (Optional/Intermediate level)

We recommend git cloning the repository for a couple of reasons:

Writing Tests

If you want to get involved and add more tests then there's just a few things we'd like to ask you to do:

    Use an existing file from this repository as a template for all new tests and page objects
    Follow our simple style guide
    Fork this project with your own GitHub account
    Add your test into the "tests" folder and the necessary methods for it into the appropriate file in "pages"
    Make sure all tests are passing and submit a pull request with your changes

License

This software is licensed under the MPL 2.0:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

