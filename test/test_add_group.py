# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture

def test_add_group(self):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="sgdgs", header="hdfhdhd", footer="shshd"))
    app.session.logout()

def test_add_empty_group(self):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

