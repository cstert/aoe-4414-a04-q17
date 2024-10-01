# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converts date from year, month, day, hour, minute, second to fractional Julian date
# Parameters:
# year: year of date
# month: month of date
# day: day of date
# hour: hour of date
# minute: minute of date
# second: second of date
# Output:
# Prints fractional Julian date
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.
# import Python modules
import sys # argv
import math
# "constants"
# e.g., R_E_KM = 6378.137
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments


# parse script arguments
if len(sys.argv)==7:
 year = int(sys.argv[1])
 month = int(sys.argv[2])
 day = int(sys.argv[3])
 hour = int(sys.argv[4])
 minute = int(sys.argv[5])
 second = float(sys.argv[6])

else:
   print(\
      'Usage: '\
      'python3 ymdhms_to_jd.py year month day hour minute second'
     )
   exit()

# write script below this line
jd = day - 32075 + 1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
JDmidnight = jd-0.5
Dfrac = (second+60*(minute+60*hour))/86400
jd_frac = JDmidnight+Dfrac
print(jd_frac)
