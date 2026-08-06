# 1. Project Title
Urban Mobility: a look into the NYC TLC data

## 2. Project Overview and Value
* **Problem:** NYC has been oen of the busiest state in the US. One of the most thriving businesses in this state is the taxi business. (edit)

* **Objectives:**
    * **Main:**  We seek to understand customer behaviour, trip patterns, traffic congestions, airport demand, weather effects , and revenue trend.
    * **Specific:**
        * **A. Spatial inequality in Mobility:** Here, we seek to answer the question: Do neighborhoods exhibit persistent mobility inequalities that cannot be explained by population density alone?. We aim to answer this by using spatial statistics and clustering analysis, and then, also look at the policy implication.
        * **B. Detecting emerging transportation:** Can we detect unusual mobility patterns before they become obvious?. We would use methods such as change-point detection, anomaly detection and bayesian approaches.
        * **C. Fairness in tipping behaviour:** How do tipping patterns vary after adjusting for: 
            * trip distance,
            * fare,
            * time,
            * neighborhood,
            * weather?
            We do a causal/statistical modeling.? 
        * **D. Mobility Resilience:** How quicklu do different neighborhoods recover after disruptions? for eg after snowstorms, holidays, COVID, subway outages(external data) etc
        * **E. Driver Revenue Variability:** Which factors increase the variability of driver earnings.
        * **Network Analysis:** Treating taxi trips as a directed graph, we will study the centrality, bottlenecks and evolving transportation netwroks. 

* **Value:** (Edit)

## 3. Data Source and Methodology

* **Source:** NYC TLC Trip Record Data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page  
* **Data:** yellow_tripdata_2026-01.parquet
* **Features:** To be filled 
* **Pipeline:** 

## 4. Repository Structure
```tree
│   README.md
│   
├───.vscode
│       settings.json
│       
├───data
│   ├───external_supp
│   ├───interim
│   ├───processed
│   └───raw
│           yellow_tripdata_2026-01.parquet
│           
├───docs
│       Did-and-to-do-journal.md
│       
├───figures
├───notebooks
│       urban-mobility-nyc-tlc-trip.ipynb
│       
├───reports
├───scripts
├───src
└───tests
```
## 5. Getting Started and installation

To be filled 

## 6. Usage

To be filled 

## 7. Results & Model Evaluation
* **Performance:** [State key metrics. eg accuracy, F1-score etc]
* **Visual:** to be filled
* **Key Findings:** [Takeaways]

## 8. License & Contact
* **License:** To be filled 
* **Author:** Denis Folitse - Email: denisfolitse@gmail.com | LinkedIn: Denis Folitse