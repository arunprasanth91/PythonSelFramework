Feature: Login page feature

  # Scenario outline and Scenario template are same.


  Scenario Outline: Login check with different data set
    Given I login to the URL "https://loginfeaturetest.com/"
    When I enter the credentials
    And I click on login button
    Then validate user is successfully logged in and "welcome" message is displayed

    Examples: Successful login
    |username|password|
    |guest   |guest   |
    |guest1  |guest1  |


