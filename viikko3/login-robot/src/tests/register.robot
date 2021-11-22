*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

# Register With Already Taken Username And Valid Password
#     Create User  paivi  paivi221
#     Create User  paivi  paivi221
#     Output Should Contain  User with username paivi already exists

# Register With Too Short Username And Valid Password
#     Create User  pa  paivi221
#     Output Should Contain 

# Register With Valid Username And Too Short Password
# # ...

# Register With Valid Username And Long Enough Password Containing Only Letters
# # ...

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123