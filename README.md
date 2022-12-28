# time_calculator

Write a function named add_time that takes in two required parameters and one optional parameter:

    1. a start time in the 12-hour clock format (ending in AM or PM)
    2. a duration time that indicates the number of hours and minutes
    3. (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

![image](https://user-images.githubusercontent.com/89969262/209778717-0a32c6a1-c91d-4555-ba2e-23ddeef023d3.png)
