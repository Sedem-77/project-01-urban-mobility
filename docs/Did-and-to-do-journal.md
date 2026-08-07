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