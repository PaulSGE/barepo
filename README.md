# Electric Vehicle Next Charge Location Prediction

### Abstract—
By 2050, global sales of electric vehicles (EVs) are predicted to account for approximately 70% of all vehicle sales. However, whilst transitioning from combustion engine vehicles to EVs would result in reduced carbon dioxide emissions, it would place significant strain on energy generation, and grid infrastructure. Many EV studies investigated routing or charge station management, while research on predicting energy demand at a specific location was lacking. To address this, our study focused on predicting EV’s next charge location. We developed a localised onboard Convolutional Neural Network (CNN) model that achieved accuracies up to 95%. Our proposal used community area Distributed Energy Resource Management Systems (DERMS) to train EV models during charge transactions, while predictions were made onboard each EV. To address the lack of EV mobility charge data, we created a hybrid dataset using empirical Chicago city taxi mobility data adding synthetic EV charging event states. We conducted multiple experiments over various battery charge levels to understand how far ahead in time next charge location could be predicted, achieving reliable predictions up to 3 days before requiring next charge. Finally, this study laid a foundation for future EV mobility research by providing a novel EV mobility charge dataset.

Index Terms—EV Mobility prediction, EV next charge location prediction, Convolutional Neural Network CNN

## This repository contains the following folders: 

## Code
	
a) BATCH_PADDING.ipynb
This file contains functions to prepare data for modelling, all code is fully commented. Functions include creating batches, padding batches, and analysis of data.  

b) MODELLING.ipynb 
This file contains all scripts required to prepare and model data using both BiLSTM and CNN fastai models, all code is fully commented.

c) BATTERY_MASK.ipynb 
This file is used to mask charge cycles to represent different battery charge levels to model data representing a variety of battery charge ranges.


## Docs

a) Chicago City Map.afphoto
This file is a map for Chicago city which has 77 community areas, these community areas are taxi passenger pickup and drop off locations as well as possible EV next charge location prediction areas.

b) Chicago-Charge-Stations.xlsx
This file is a list of service stations and their addresses including the community area ID, we assume these service stations will be charge stations in the future.


## Data

This folder contains all datasets including: 

a) 12 months of EV taxi spatio-temporal datasets every month divided into 3 CSV files, each CSV file has a header including all feature titles.

b) A CSV file which is a data_dictionary.csv explaining features in our EV monthly CSV files.

c) EV_Sales.xlsx this file contains logistics for the 9 EVs including battery capacity kWh, range in kilometres (km), energy consumption Wh/km (watt hours per km), sales 2019, and total sales within the USA.

d) A file called period.xlsx this file contains 7 periods of a 24 hour day including start and end time for these periods.

e) ChargeStations.xlsx this file contains 77 community areas and the number of petrol/service stations that these communities have, we assume these service stations will be charge stations in the future.

f) location_boundary.xlsx this file contains community areas ranging from 1 to 77 in the first column, followed by community areas that share a common border with the community area in the first column.
 
