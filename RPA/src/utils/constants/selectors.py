"""Seletores CSS do automationexercise.com compartilhados entre os casos de teste."""

HEADER = {
    "home": 'a[href="/"]',
    "products": 'a[href="/products"]',
    "login": 'a[href="/login"]',
    "logout": 'a[href="/logout"]',
    "delete_account": 'a[href="/delete_account"]',
    "contact_us": 'a[href="/contact_us"]',
    "test_cases": 'a[href="/test_cases"]',
    "logged_in_as": "a:has(> i.fa-user)",  # "Logged in as <nome>"
}

LOGIN_FORM = {
    "title": "div.login-form h2",  # "Login to your account"
    "email": "input[data-qa='login-email']",
    "password": "input[data-qa='login-password']",
    "button": "button[data-qa='login-button']",
    "error": "div.login-form form p",  # "Your email or password is incorrect!"
}

SIGNUP_FORM = {
    "title": "div.signup-form h2",  # "New User Signup!"
    "name": "input[data-qa='signup-name']",
    "email": "input[data-qa='signup-email']",
    "button": "button[data-qa='signup-button']",
    "error": "div.signup-form form p",  # "Email Address already exist!"
}

# Formulário "Enter Account Information" (segunda etapa do cadastro)
ACCOUNT_FORM = {
    "title": "div.login-form h2 b",
    "gender": "input#id_gender1",
    "password": "input[data-qa='password']",
    "birthday": "select[data-qa='days']",
    "birthmonth": "select[data-qa='months']",
    "birthyear": "select[data-qa='years']",
    "newsletter": "input#newsletter",
    "offers": "input#optin",
    "firstname": "input[data-qa='first_name']",
    "lastname": "input[data-qa='last_name']",
    "company": "input[data-qa='company']",
    "address": "input[data-qa='address']",
    "address2": "input[data-qa='address2']",
    "country": "select[data-qa='country']",
    "state": "input[data-qa='state']",
    "city": "input[data-qa='city']",
    "zipcode": "input[data-qa='zipcode']",
    "mobile_number": "input[data-qa='mobile_number']",
    "create_button": "button[data-qa='create-account']",
}

ACCOUNT_STATUS = {
    "created": "h2[data-qa='account-created']",
    "deleted": "h2[data-qa='account-deleted']",
    "continue": "a[data-qa='continue-button']",
}
