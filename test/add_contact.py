# -*- coding: utf-8 -*-
import pytest

from fixture.application_contact import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.add_new_contact(Contact(firstname="Pavel", lastname="Shchukin", nickname="Junior", mobile="Email", email="schukinp@gmail.com"))
        app.logout()

