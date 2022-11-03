Feature: Signup
  Scenario Outline: User should be able to Signup the into the application
    Given Open the chrome browser enter the valid URL
    When enter the first name "<f_name>"
    And enter the last name "<l_name>"
    And enter the email_id "<email_id>"
    And re_enter the conform_emailid "<conform_emailid>"
    And enter the pwd "<pwd>"
    And click the day
    And click the month
    And click the year
    And click on the gender female radio button
    And click on the Signup button
    Then close chrome browser
    Examples:
      |f_name|l_name|email_id |conform_emailid |pwd|
      |varalakshmi |dande |dandevaralakshmi410@gmail.com|dandevaralakshmi410@gmail.com|VaraLak@410|
      |lakshmi     |dande |dandevaralakshmi@gmail.com   |dandevaralakshmi@gmail.com   |lakshmi111 |
      |madhu sree  |sree  |madhu@gmail.com              |madhu                        |madhu876   |
      |thanu       |karidi|thanu                        |thanu@gmail.com              |@ghjjm87   |
      |krishna sree|dande |dandekrishn@gmail.com        |dandekrishna@gmail           |345679     |