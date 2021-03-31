# Statistical Analysis of 2019 Housing Prices in King County, Washington

![readme_pic](/readme_pic.jpg)

There are many factors which influence housing prices, and understanding how they affect property value can be extremely useful to people- from homeowners hoping to improve the market potential of their current homes, to policymakers making decisions about investment in public projects. 

In this project we're going to analyze various housing related factors and see how they affect house prices.

## Introduction:
So, how does one go about buying a house?
A house is a large investment that can become a bad investment if done incorrectly.
We took data from King County in Washington and looked at three specific attributes,
Sqaure footage of livable space, does a home have a porch, and if it is located on one of King
counties many waterfronts.
We wanted to know, if any of these attributes increased the sales price of a home.


## Purpose of Analysis:
This project tries to validate the following questions regarding housing prices in King County for the year 2019:
Does having higher square footage increase home sale price?
Does having a porch increase home sale price?
Does having a beach or lake front increase home sale price?

## Data:
For our analysis, we used the King County House Sales dataset, narrowed down to all homes sold in 2019.
The dataset itself was a combination of the following datatables, all of which we individually retrieved from King County's website:
-Real Property Sales
-Residential Building
-Parcel

Once we had all our data tables, we combined them into one big dataframe along the 'major' and 'minor' columns within each data table.
We named this combined table, rps2019_parcel_dfmerge
Once we had our combined dataframe, we defined what a 'house sale' was:
Single family homes: Properties containing 1 living unit per property. (no duplexes, apartments, condominiums, etc.)
Residential. (No commercial properties)
Sales price between $50,000 and $2,000,000. As we discussed this would remove outliers and bad data, while covering
the bulk of sales in King County during 2019.
Properties containing greater than 500 sq ft.

## Regression modeling:
We deicded on our features using "gut feeling" and combing through the data:
We chose the features which interested us in relation to the Sale Price, the "gut feeling"
We looked at the correlation matrix and picked features which had a high correlation with Sale Price, which we hadn't picked earlier, the data combing.
A heatmap of the corraltion between features was also used.

We were left with the following pool of features:
'SalePrice','DocumentDate','SaleInstrument','HBUAsIfVacant','BldgGrade','SqFtLot','SqFtTotLiving','SqFt1stFloor','SqFt2ndFloor','SqFtTotBasement','SqFtFinBasement','FinBasementGrade','SqFtGarageAttached',                         'Bedrooms','BathHalfCount','Bath3qtrCount','BathFullCount','SqFtOpenPorch','SqFtEnclosedPorch','SqFtDeck','WfntLocation','WfntFootage','SaleReason'
Some of the above features are categorical which needed to be split up. We wanted to split each category from each variable into a new column for each category. 
For example: Builidng Grad (bldgr), became 12 seprate columns, with each representing a different grade from 1 to 12.

For the final step we looked at the Variance inflation factor (VIF), to show us the corraltion between our features. We then excluded features which had a high p-value, and many that had high multicollinearity. This made our model more "True" and accurate to real life.

## Conclusion:
With our final model we were able to answer, that:
Sqaure Footage of your Total Living does increase Sales Price.
Having a porch does increase Sales Price.
We also found some interesting data around Waterfront Locations, that seemed to conflcit with our common sense. We have since concluded that this was due to the way we sliced our data from earlier.
We would like to do more tests and anlysis around Wa