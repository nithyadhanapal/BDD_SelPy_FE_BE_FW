
  @smoke @user_api_smoke
  Feature: User API Smoke

    @TCID-29
    Scenario: Verify 'POST/Customers' create user
      Given I generate random email and password
      When I call 'create customer' api
      Then customer should be created
