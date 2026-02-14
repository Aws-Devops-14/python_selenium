Feature: Banking Flow

  Scenario: Complete banking workflow
    Given user launches the application
    When user registers a new account
    And user logs in
    And user opens a new account
    And user transfers funds
    Then transaction should be successful
    And user logs out
