# This is parametrized test (runs a two testdata inputs with different values)
def test_business_name_field(app, data_businessNameValidFormat):
    testdata = data_businessNameValidFormat

    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()

    # scenario
    value_before = app.business_creation_page.get_field_value(input_field='company.legalName')
    app.business_creation_page.complete_business_name_input_field(value=testdata)
    value_after = app.business_creation_page.get_field_value(input_field='company.legalName')

    # verification
    assert testdata == value_after
    assert value_before != value_after
    app.session.reload_a_page()


# This is parametrized test (check each input field by field name)
def test_each_input_field_valid_value(app, data_allInputFields):
    # testdata
    testdata = data_allInputFields
    field_value = testdata.split('.')[-1]

    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()

    # scenario
    value_before = app.business_creation_page.get_field_value(input_field=testdata)
    app.business_creation_page.complete_input_field(field_name=testdata, value=field_value)
    value_after = app.business_creation_page.get_field_value(input_field=testdata)

    # verification
    assert field_value == value_after
    assert value_before != value_after


def test_all_input_fields(app):
    # testdata
    testdata = {'company.legalName': 'Company Inc',
                'personal.legalName.firstName': 'Firstname',
                'personal.legalName.lastName': 'Lastname',
                'personal.email': 'test@gmail.com'}
    filled_labels = []

    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()
    else: app.session.reload_a_page() # clean up a testdate

    # scenario
    for field in testdata:
        app.business_creation_page.complete_input_field(field_name=field, value=testdata[field])
        label = app.business_creation_page.get_input_field_label(input_field=field).text
        filled_labels.append(label)
    app.business_creation_page.click_continue()
    alerts = app.business_creation_page.get_alert_content()
    error_highlighted_fields = app.business_creation_page.get_all_error_input_labels()

    # verification
    for label in filled_labels:
        assert label+' is required.' not in alerts
    assert (error is None for error in error_highlighted_fields)


def test_empty_input_fields(app):
    # testdata
    testdata = {'company.legalName': '',
                'personal.legalName.firstName': '',
                'personal.legalName.lastName': '',
                'personal.email': ''}
    filled_labels = []

    # pre-conditions
    if not app.business_creation_page.is_business_register_page_open():
        app.business_creation_page.open_business_registration_form()
    else:
        app.session.reload_a_page()  # clean up a testdate

    # scenario
    for field in testdata:
        app.business_creation_page.complete_input_field(field_name=field, value=testdata[field])
        label = app.business_creation_page.get_input_field_label(input_field=field).text
        filled_labels.append(label)
    app.business_creation_page.click_continue()
    alerts = app.business_creation_page.get_alert_content()
    error_highlighted_fields = app.business_creation_page.get_all_error_input_labels()

    # verification
    for label in filled_labels:
        assert label+' is required.' in alerts
    assert len(error_highlighted_fields) == len(testdata)
