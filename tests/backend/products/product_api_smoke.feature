
@products_smoke @smoke
Feature: Product API Smoke

  @TCID-24
  Scenario: Verify 'get all products' returns the expected number of products
    Given I get the number of available products from db
    When I get the number of avaiable products from api
    Then The total number of products in api should be same as in db

  @TCID-25
  Scenario: Verify 'product/id returns a product with the given id
    Given I get '1' random product from database
    Then I verify product api returns the correct product by id