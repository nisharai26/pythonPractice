# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

#     If the book is returned on or before the expected return date, no fine will be charged (i.e.: 


# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,

# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the

# If the book is returned after the calendar year in which it was expected, there is a fixed fine of

# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be

def libraryFine(d1, m1, y1, d2, m2, y2):
        if y1>y2:
                return 10000

        if y1==y2:
            if m1>m2:
                return (m1-m2)*500
            if m1==m2 and d1>d2:
                return (d1-d2)*15

        return 0

libraryFine(9,6,2015,6,6,2015)

