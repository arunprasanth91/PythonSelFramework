from behave import *

@given(u'I login to the URL "https://loginfeaturetest.com/"')
def step_impl(context):
    #assert context.failed is False
    pass



@when(u'I enter the credentials')
def step_impl(context):
    for row in context.table:
        print(row['username'])
        print(row['password'])


@when(u'I click on login button')
def step_impl(context):pass



@then(u'validate user is successfully logged in and "welcome" message is displayed')
def step_impl(context):pass