# Created by karimonward at 30/12/2024
Feature: Test for cart functionality

  Scenario: Scenario: User can click on the cart icon
    Given Open target page
    When click on cart icon
    Then Verify “Your cart is empty” is shown



    Scenario: user can add a product to cart
      Given Open target page
      When search for tea
      And click on add to cart
      And confirm add to cart button from side navigation
      And open cart page
      Then Verify cart has 1 item(s)




