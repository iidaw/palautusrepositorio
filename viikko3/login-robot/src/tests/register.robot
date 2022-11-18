*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  iida  i
    Output Should Contain  Password too short

Register With Valid Username And Password
    Input Credentials  iida  iida123
    Output Should Contain  New user registered

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  iida  iidaaaaa
    Output Should Contain  Password doesn't contain numbers

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command