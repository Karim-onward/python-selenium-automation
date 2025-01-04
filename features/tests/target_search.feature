# Created by karimonward at 26/12/2024
Feature: Tests for cart icon

  Scenario: User can click on the cart icon
    Given Open target page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: User can navigate to sign in
    Given Open target main page
    When click sign in from the main page
    And click sign in
    Then Verify sign In form open