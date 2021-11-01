def test_dropdown_selection(app, data_dropdownOptions):
    # testdata
    option = data_dropdownOptions
    dropdown_field = 'Company type'
    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()
    else:
        app.session.reload_a_page()  # clean up test date

    # scenario
    app.business_creation_page.open_dropdown_menu(field_label=dropdown_field)
    app.business_creation_page.select_dropdown_option(option=option)

    # verification
    assert option == app.business_creation_page.get_dropdown_value_by_field(dropdown_field)

def test_dropdown_check_invalid_option(app):
    # testdata
    invalid_option = 'testdata'
    valid_option = 'Operating Company'

    dropdown_field = 'Company type'
    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()
    else:
        app.session.reload_a_page()  # clean up test date

    # scenario
    app.business_creation_page.open_dropdown_menu(field_label=dropdown_field)
    dropdown_menu_all_options = app.business_creation_page.get_all_dropdown_menu_options()

    # verification
    assert valid_option in dropdown_menu_all_options
    assert invalid_option not in dropdown_menu_all_options
