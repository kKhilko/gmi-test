def test_business_register_form_fieldsets_present(app):
    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()

    # scenario
    expected_fieldset = ['Company Information', 'Company Location', 'Personal Information']
    actual_fieldset = app.business_creation_page.get_form_fieldsets()

    # verification
    for i in expected_fieldset:
        assert i in actual_fieldset
    assert expected_fieldset == actual_fieldset
