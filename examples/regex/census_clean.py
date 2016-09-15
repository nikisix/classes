"""
American Census Survey Null Values
Convert all census null values to NULL (that will be specified in the copy command as the NULL paramter)
An '**' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.
An '-' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.
An '-' following a median estimate means the median falls in the lowest interval of an open-ended distribution.
An '+' following a median estimate means the median falls in the upper interval of an open-ended distribution.
An '***' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.
An '*****' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate. 
An 'N' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.
An '(X)' means that the estimate is not applicable or not available.
"""
import re, sys
f = file(sys.argv[1])
text = f.read()
f.close()

text = re.sub('"[\d,]+[\+-]"', 'N', text) # "2,500-"  "200,000+"
text = re.sub('[\d\.]+[\+-]', 'N', text) # 100-  9.0+
text = re.sub(',-,', ',N,', text)
text = re.sub('\(X\)', 'N', text)
text = re.sub('\*\*\*\*\*', 'N', text)
text = re.sub('\*\*\*', 'N', text)
text = re.sub('\*\*', 'N', text)
sys.stdout.write(text)
