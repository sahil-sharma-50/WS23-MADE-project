# Project Plan

## Title
<!-- Give your project a short title. -->
An Analytical Study on the Influence of Weather Conditions on Road Safety in Berlin.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
This project digs into how the weather—rain, snow, and extreme temperatures—affects road safety. It's looking at accident data from Berlin in 2019 to see how these weather conditions impact the number of accidents that happen.

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to figure out how weather influences road safety, which is super important for creating better safety rules. It's checking out how different weather conditions link to the number of accidents. Plus, the goal is to make people more aware of the risks when driving in certain weather, to cut down on accidents, and to make the roads safer for everyone.
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->
### Datasource1: Road traffic accidents by accident location in Berlin 2019 
* Metadata URL: [https://data.europa.eu/en](https://data.europa.eu/data/datasets/418d5d6f-04c6-4a45-84da-b85d21c9d47c/quality?locale=en)
* Data URL: https://www.statistik-berlin-brandenburg.de/opendata/AfSBBB_BE_LOR_Strasse_Strassenverkehrsunfaelle_2019_Datensatz.csv
* Data Type: CSV
<br>
Road traffic accidents by accident location with street name, GPS coordinates, and LOR planning room in Berlin 2019; Accident month, weekday, hour; Type and category of accident

### Datasource2: Weather Dataset
* Metadata URL: https://mobilithek.info/offers/-6901989592576801458](https://www.dwd.de/EN/ourservices/cdc/cdc_ueberblick-klimadaten_en.html
* Data URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/
* Data Type: CSV
<br>
Daily, 10-minute intervals of precipitation at weather stations throughout Germany.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->
1. Collect and refine the two datasets. [#1][i1]
2. Establish automated data pipelines for effective data processing. [#2][i2]
3. Implement automated testing mechanisms for the pipeline. [#3][i3]
4. Conduct exploratory data analysis. [#4][i4]
5. Leverage GitHub Actions for continuous integration. [#5][i5]
6. Visualize the data, derive conclusions, and compile a final report. [#6][i6]

[i1]: https://github.com/sahil-sharma-50/WS23-MADE-project/issues/1
[i2]: https://github.com/sahil-sharma-50/WS23-MADE-project/issues/2
[i3]: https://github.com/sahil-sharma-50/WS23-MADE-project/issues/3
[i4]: https://github.com/sahil-sharma-50/WS23-MADE-project/issues/4
[i5]: https://github.com/sahil-sharma-50/WS23-MADE-project/issues/5
[i6]: https://github.com/sahil-sharma-50/WS23-MADE-project/issues/6
