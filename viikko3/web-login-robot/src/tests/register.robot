*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Create User


*** Test Cases ***
Register With Valid Username And Password
    Set Username  iida
    Set Password  iida1234
    Set Confirmation  iida1234
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  i
    Set Password  iida12345
    Set Confirmation  iida12345
    Submit Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  iida
    Set Password  iida
    Set Confirmation  iida
    Submit Register
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  iida
    Set Password  iida1234
    Set Confirmation  iida12345
    Submit Register
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  iida
    Set Password  iida1234
    Set Confirmation  iida1234
    Submit Register
    Register Should Succeed
    Go To Login Page
    Set Username  iida
    Set Password  iida1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  iida
    Set Password  iida123
    Set Confirmation  iida123
    Submit Register
    Go To Login Page
    Set Username  iida
    Set Password  iida123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Go To Register Page And Create User
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
