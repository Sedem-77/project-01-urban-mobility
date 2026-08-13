# Learning Journal

In here, we track our progress and time spent on this work. We do so by answering the following questions each time we work on this project: 

* **Date:**
* **Time Spent:**
* **What did we accomplish today**
* **What new thing did we learn. Codewise and Methodwise (Document new models learnt or packages for futurre refs):**
* **What challenged us:**
* **To do next:**

## **Date:** Aug/07/2026
* **Time Spent:** 3hrs 50 min
* **What did we accomplish today** I reseolved my .gitignore issue. My gitignore contents were still being tracked. 
* **What new thing did we learn. Codewise and Methodwise (Document new models learnt or packages for futurre refs):** Codewise: to resolve this, I learnt about
1. git rm -r --cached . # clears all cache from the memory of git. It will deletes files already added to git repo before added to gitignore 
2.  Set-Content -Path .gitignore -Value "yellow_tripdata_2026-01.parquet`ndata/raw/*`n!data/raw/.gitkeep`ndata/interim/*`n!data/interim/.gitkeep`ndata/processed/*`n!data/processed/.gitkeep`ndata/external_supp/*`n!data/external_supp/.gitkeep`n__pycache__/`n*.pyc" -Encoding utf8 #( after you clear all cache, you re-add all files you dont want to track to the gitignore. If you want files in folder not to be tracked but the folder itself to be tracked, add a .gitkeep into that folder (code below) and a n!data/raw/.gitkeep to the gitigore file telling it to remember to keep this folder. The -Encoding utf8 is important so that it may not be saved as utf-16 or other form of encoding. gitignore may silenty fail because of that. 
3. `n!data/interim/.gitkeep
 #Create a .gitkeep file in the folders to keep 
4. git add .
5. git commit -m ""
6. git push


* **What challenged us:** Ensuring that the gitignore works well

*  **To do next:** Data quality report



## **Date:** From Aug/08/2026 - Aug/12/2026
* **Time Spent:** 3hrs 
* **What did we accomplish today** I explored the data briefly to check for it's validity and missingness. I noticed there were some missing values in some variables that needed cleaning (yet to do that) and some vairables contains rows that are not valid ( example: passenger_count having more than 6 passengers). I also creeated my tentative research questions that i want to look at. This takes my first objective in the readme file and created sub questions to look at. It is tentative because the questions will be modified based on what the exploratory analysis reveals. The Rest of the objectives will be tackeled later.. 
* **What new thing did we learn. Codewise and Methodwise (Document new models learnt or packages for future refs):** While at it, my  vscode keeps spliting my workspace into 2 and reopens my code in the second split opener and interrupting with my work flow. I checked on stackexchange and found this great suggestion that helped me resolved it: 

    Second action (Visual Studio Code opens multiple instances)
Open the Visual Studio Code editor, go to the setting and paste this in the search bar (e.g., Ctrl + ,):
"workbench.editor.enablePreview": false
If you have this option marked, you should unmark it or set it to false depending on the interface you are presented and interacting with. This should stop Visual Studio Code from running multiple instances and hopefully resolve your problem. (link: https://www.bing.com/search?q=why%20does%20my%20vscode%20keep%20spliting%20my%20workspace%20into%202%20and%20reopens%20my%20code%20in%20the%20second%20split%20opener&qs=n&form=QBRE&sp=-1&ghc=2&lq=0&pq=why%20does%20my%20vscode%20keep%20spliting%20my%20workspace%20into%202%20and%20reopens%20my%20code%20in%20the%20second%20split%20opener&sc=1-99&sk=&cvid=FE8754F4ED974B518CA9D7C8C525DA02&dayref=1&ajf=10).

Codewise: One code I think its good keeping in mind for expediency is this: df_filter_ratecodeid = df[~df["RatecodeID"].isin(range(1,7))] (Keep all columns except "RatecodeID)

* **What challenged us:**  Resolving the vscode splitting issue. I nearly gave up!

*  **To do next:** Explore more validity and quality of data and start cleaning (perhaps)