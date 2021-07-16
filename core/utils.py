import base64
import requests
import json
import keys

def encodeToB6(val):
    return base64.b64encode( bytes(val,'utf8')).decode('utf8')

def getAuthHeader(credentials):

    auth = f'{credentials["api_key"] }:{credentials["api_secret"]}' 
    auth = encodeToB6(auth)
    return f'Basic {auth}'

def initiateRequest( payload):
    url = "https://checkout.beem.africa/v1/checkout"

    api_creds = {
        "api_key" : keys.API_KEY,
        "api_secret" : keys.API_SECRET
    }
  
    authorization_header = getAuthHeader( api_creds )
    headers = {
        "Authorization": authorization_header
    }

  

    try:
        return requests.get(url, headers=headers, params=payload)
    except Exception as e:
        print(e.args)
        return False




# form validations


def is_greater_than(value, num):
    return len(value) >= num


def my_validator(value, validate_funcs):
    errors = []
    for func in validate_funcs:
        error = func(value)
        if error:
            errors.append(error)
    return errors

# Validators


def should_be_string(value):
    if not isinstance(value, str):
        return "Should be a string"


def should_be_greater_than_3(value):
    if not is_greater_than(value, 3):
        return "Should have three letters or more"

def should_be_greater_than_12(value):
    if not is_greater_than(value, 12):
        return "Including '255...' your number should include twelve digits"



def validator_executor(field_name, value, validators=[]):
    res = {}
    validation_errors = my_validator(
        value, validators)

    if len(validation_errors):
        res[field_name] = validation_errors
    return res


def validate_post_data(request):
    mobile = request.POST.get('mobile')
    amount = request.POST.get('amount')
    donator = request.POST.get('donator')


    errors = []

    form_data = [
        {'mobile': mobile, 'validators': [
            should_be_string, should_be_greater_than_12]},
        {'amount': amount, 'validators': [
            should_be_string, should_be_greater_than_3]},
        {'donator': donator, 'validators': [
            should_be_string, should_be_greater_than_3 ]},
    ]

    for fd in form_data:
        args = list(fd.keys())
        field_name = args[0]
        field = fd[args[0]]
        validators = fd[args[1]]
        res = validator_executor(field_name,
                                 field, validators)
        if len(res.items()):
            errors.append(res)

    cleanValues = {
        "amount": amount,
        "donator": donator,
        "mobile": mobile,
    }

    return errors, cleanValues

# helpers

def extract_redirect(res):
    res_content = res.content.decode('utf8')
    
    try:
        return json.loads(res_content)['src']
    except Exception as e:
        print(e.args)
        return False

   


    