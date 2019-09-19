## This project creates a pipeline between Git and Code Collaborator.

#### Below are the key points
    * The main file is generateCodeReview.py
    * You can query git and generate code collaborator reviews based on below review mode
        1. Date wise
        2. Commit wise
        3. Story wise
    * How does this work?
        1. Fetch git commit based on review mode
        2. Based on this, grouping of commits is done
        3. Then code reviews are generated in code collaborator
