
@my_account_smoke @smoke
  Feature: My account smoke test

    @TCID-10
    Scenario: Valid user should be able to login

      Given I go to 'my account' page
      When I type 'admin' into the username of login form
      And I type 'nithya123' into the password of login form
      And I click on 'login' button
      Then User should be logged in

    @TCID-11
    Scenario: User with wrong password should get correct error

      Given I go to 'my account' page
      When I type 'admin' into the username of login form
      And I type 'nithya' into the password of login form
      And I click on 'login' button
      Then error message with username 'admin' should be displayed

    @TCID-12
    Scenario: User with non-existing username should get correct error

      Given I go to 'my account' page
      When I type 'nonexisting' into the username of login form
      And I type 'nonpassword' into the password of login form
      And I click on 'login' button
      Then error message with 'Unknown username' should be displayed