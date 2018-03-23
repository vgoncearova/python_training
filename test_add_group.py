# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture

def test_add_group(self):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="sgdgs", header="hdfhdhd", footer="shshd"))
    app.logout()

def test_add_empty_group(self):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

