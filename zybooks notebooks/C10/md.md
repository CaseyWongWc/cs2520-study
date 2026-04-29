## 11.12 LAB: Dates

### LAB ACTIVITY: LAB: Dates

Complete the code to implement the following operations:
- Complete read_date():Read an input string representing a date in the format yyyy-mm-dd.- Create a date object from the input string.- Return the date object.- Call read_date() four times to read four (unique) date objects and store the date objects in a list.- Call sorted() to sort the list of date objects, earliest first. Store the sorted dates in a new list.- Output the sorted_dates, in the format mm/dd/yyyy.Hint: Use strftime() to format the date outputs. (See resource below.)- Output the number of days between the last two dates in the sorted list as a positive number.- Output the date that is 3 weeks from the most recent date in the format "July 4, 1776".Hint: Use timedelta() to set a duration of time for the arithmetic on date objects. (See resources below.)
Ex: timedelta(days=50, seconds=27, hours=8, weeks=2) will define a duration of 50 days + 27 seconds + 8 hours + 2 weeks.- Output the full name of the day of the week of the earliest day.Ex: If the input is:

```
2022-01-27
2022-07-04
2020-12-31
2022-07-29
```
the output is:

```
12/31/2020
01/27/2022
07/04/2022
07/29/2022
25
August 19, 2022
Thursday
```
Resources on datetime module can be found here:
Examples of using date objects
Format output of date objects with strftime()
Examples of using timedelta()

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `2022-01-27\n2022-07-04\n2020-12-31\n2022-07-29\n` | `12/31/2020\n01/27/2022\n07/04/2022\n07/29/2022` | 2 |
| 2 | `1099-01-06\n2022-07-04\n1094-08-01\n2021-01-01\n` | `08/01/1094\n01/06/1099\n01/01/2021\n07/04/2022\n549` | 2 |
| 3 | `2022-01-01\n2022-01-01\n2022-01-01\n2022-01-01\n` | `01/01/2022\n01/01/2022\n01/01/2022\n01/01/2022\n0\nJanuary 22, 2022` | 2 |
| 4 | `1999-05-05\n1999-06-05\n1999-06-07\n1999-07-05\n` | `05/05/1999\n06/05/1999\n06/07/1999\n07/05/1999\n28\nJuly 26, 1999\nWednesday` | 2 |
| 5 | `2050-12-01\n2050-11-01\n2050-10-01\n2050-01-01\n` | `01/01/2050\n10/01/2050\n11/01/2050\n12/01/2050\n30\nDecember 22, 2050\nSaturday` | 2 |
*Total: 10 points*

___

```python  ```