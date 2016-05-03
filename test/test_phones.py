


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homenumber == contact_from_edit_page.homenumber
    assert contact_from_home_page.mobilenumber == contact_from_edit_page.mobilenumber
    assert contact_from_home_page.worknumber == contact_from_edit_page.worknumber
    assert contact_from_home_page.faxnumber == contact_from_edit_page.faxnumber