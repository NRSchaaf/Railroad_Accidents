# Weathering the Rails: The Impact of Extreme Temperatures and Temperature Changes on Railroad Safety

### Authors: Nathan Schaaf, Sheryl Kamesetty, Bikramjit Sinha Roy, Andrea Arrivillaga Corado, Yash Pradhan   
### Date: December 10, 2024  
### Course: Advanced Business Analytics, The University of North Carolina at Charlotte  
### Professional Context: Prepared for the U.S. Railroad Industry (with a focus on safety improvements)


<!-- Table of Contents -->
1. [Introduction](##introduction)
2. [Tools](##tools)
3. [Project Structure](##project-structure)  
4. [Recreating the Analysis](##recreating-the-analysis)  
5. [Key Findings](##key-findings)  
6. [Conclusion](##conclusion)  
7. [References](##references)


<!-- Introduction -->
## Introduction
This project analyzes the impact of extreme temperatures and temperature fluctuations on track-related failures in the U.S. railroad industry. By combining weather data with historical rail incident reports, the goal is to identify high-risk areas for proactive track maintenance and safety improvements. Key insights are drawn to support strategic interventions aimed at reducing derailments and operational costs.

Key statistics:  
- Over the last decade, 4,595 incidents were attributed to track failures, with 4,301 resulting in derailments.  
- The average cost of a track failure incident is \$208,356, with some exceeding \$22 million.  

As climate change accelerates extreme weather patterns, this analysis provides actionable recommendations to mitigate risks and enhance railroad safety.


<!-- TOOLS -->
### Tools

* Jupyter Notebook
* Python
* FRA Accident/Incident Data API
* visualcrossings.com free membership and API key (weather data)
* ESRI Arc GIS free membership


<!-- Project Structure -->
## Project Structure

The project consists of the following directories:  

- **`data/`**: Contains raw and processed datasets used in the analysis.  
- **`images/`**: Stores visualizations and maps generated during the analysis.  
- **`notebooks/`**: Jupyter notebooks used for data extraction, cleaning, and analysis.


<!-- Recreating the Analysis -->
## Recreating the Analysis

To replicate the analysis, execute the notebooks in the following order:

1. **`notebooks/fra_data_pull.ipynb`**  
   - Pulls historical safety incident data from the FRA API.  
   - Filters data to include only incidents from 2014 to 2024.  

2. **`notebooks/weather_data_pull.ipynb`**  
   - Extracts local weather data for each incident using the Visual Crossing Weather API.  
   - Note: Due to API call limitations (free-tier subscription), data extraction requires multiple sessions.

3. **`notebooks/weathering_the_rails_analysis.ipynb`**

### Mapping Tools
Maps were created using the **free tier of ESRI ArcGIS Online** for geographic visualization.


<!-- Key Findings -->
## Key Findings

1. **Temperature Changes**  
   - Extreme temperatures (<32°F or >85°F) show no significant impact on track-related incidents.  
   - Significant temperature changes (≥12°F) are associated with increased risk.  

2. **High-Risk Locations**  
   - Cities: Houston, St. Louis, Chicago, New York City, Philadelphia, and Washington, D.C.  
   - Rail Routes: Corridor from Cleveland to New York City to Washington, D.C.  

3. **Critical Threshold**  
   - A temperature change of ±12°F (6.6°C) is identified as the critical threshold for incident likelihood.

4. **FRA Reporting Accuracy**  
   - 24% of incident reports have a temperature deviation of ±10°F, highlighting the importance of accurate external weather data.


<!-- Conclusion -->
## Conclusion

Railroads should:  
- Maintain current track maintenance best practices to mitigate risks.  
- Prioritize enhanced inspections in high-risk areas, particularly during extreme weather events.  
- Focus on critical regions identified through this analysis for targeted interventions.  

These strategies will enhance safety, minimize derailments, and address vulnerabilities associated with climate-induced weather patterns.


<!-- References -->
## References

1. Transportation, U. D. (n.d.). Transportation data : National Highway Traffice Safety Administration [Data set]. Retrieved October 19, 2024, from https://data.transportation.gov/resource/85tf-2kj.json  
2. U.S. Department of Transportation, F.R. (2011). FRA Guide for Preparing Accident/Incident Reports. Retrieved October 18, 2024, from https://railroads.dot.gov/sites/fra.dot.gov/files/fra_net/18233/FRAGuideforPreparingAccIncReportspubMay2011.pdf
3. Weather, V. C. (n.d.). Visual crossing web services timeline [Data set]. Retrieved October 20, 2024, from https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}
4. Esri. (n.d.). ArcGIS Online. Environmental Systems Research Institute. https://www.arcgis.com
5. Railroad Track Maintenance Best Practices for Lasting Results. (2023, July 19). RS Track, Inc.. Retrieved November 25, 2024, from https://rstrackinc.com/railroad-maintenance-best-practice 


For further details, refer to the full analysis and visualizations in the `notebooks` and `images` directories.
