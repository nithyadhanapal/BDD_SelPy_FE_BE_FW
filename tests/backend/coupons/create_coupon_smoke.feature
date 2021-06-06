
Feature: Create coupon smoke

  @TCID-36
  Scenario Outline: Create coupon with minimum parameters should create coupon
    Given I create a '<discount_type>' coupon
    Then The coupon should exist in database

    Examples:
    |discount_type|
    |None         |
    |percent      |
    |fixed_cart   |
    |fixed_product|

