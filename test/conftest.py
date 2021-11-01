import importlib

import pytest
from fixture.application import Application

fixture = None


###############################  Session set up ##########################################
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')      # initialize a browser from terminal/command prompt or configure it in IDE
    if fixture is None or not fixture.session.is_valid():    # check if session does not exist or invalid when session start
        fixture = Application(browser=browser)
    return fixture


##############################   Session teardown ########################################
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.session_destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='')


##############################   Data generation  ########################################


def pytest_generate_tests(metafunc):
    """ Generating parameters combination, depending on test_case args.
        1. Taking parameters from test data file (data/<path>)
        2. Load data from generator file
        3. Call parameters one by one for test session

    :param metafunc: set og parameters which we calling in test method

    """
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data"):
            modul = get_module(fixture)
            testdata = load_from_module(modul)
            metafunc.parametrize(fixture, testdata)


def get_module(data):
    return '' + '.'.join(data.split('_'))


def load_from_module(module):
    return importlib.import_module('%s' % module).testdata



