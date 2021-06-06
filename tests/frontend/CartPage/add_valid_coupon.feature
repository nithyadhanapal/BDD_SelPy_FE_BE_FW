
  @cart @coupon @coupon_fe
  Feature: Add Valid coupon to cart

    @TCID-44
    Scenario: Adding 50% off cart should discount the whole cart by 50%

      Given I go to 'home' page
      When I add '3' random item to cart from the homepage
      And I click on cart in the top nav bar and verify cart page opens
      And I get the total amount of the cart
      And I get a valid 50% off coupon
      And I apply coupon on the cart
      Then The total should be reduced by 50%