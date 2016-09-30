
#  HOW TO READ THE Z TABLE

### Z tables are (unlike most other statistical tables) 1 dimensional 
#### (I was confusing on this issue in class, my confusion and my bad!) 

When you read a z-statistics table the **rows indicate the z** value to some precision, the different **columns indicate further precision**. So the way to get your value is: 

ROW: look for the row wich has the largest number that is just smaller than the result of your z-test

e.g. your z statistics is 1.373, choose row 1.3,

COLUMN: then look for the column with the closest second and third, if available, decimal digit (but still smaller than the one in your result for a conservative result) for more refined precision (that's  0.07 in this example) 

THE NUMBER AT THE INTERSECTION IS  0.9147.

![]('http://intersci.ss.uci.edu/wiki/images/3/3a/Normal01.jpg')

the p-value is  1- the number you read off the table. In our example: 1-0.9147 = 0.0853

 

HOW TO READ THE CHI SQ TABLE

chi sq tables are 2 dimensional, because the chi-square distribution is different for different degrees of freedom.

The degrees of freedom (generally) equal the number of observations minus the number of dependent variables. For a test of proportions between 2 samples that is 2 observations (the percentage in each sample) and 1 independent variable (e.g. participating in a program or not)

ROW: look for the row with the right number of degrees of freedom (sometimes the column, depending on who wrote the table, but generally row).

COLUMN: look for the column that stated the statistical significance you require (e.g. 0.05 for alpha=0.05!)

the number at the interception of the row and column is the MINIMUM CHI SQ significant value. Meaning if you got a value larger than that you have rejection of null at the p value corresponding to the alpha you have set.

