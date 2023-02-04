# fetch-take-home
Take home homework from Fetch for internship.

A django application is developed which runs the deep learing model for time-series regression.
Steps to run the application:
1. Clone the repository.
2. Create a virtual environment for this project.
3. In the command prompt, inside the mysite directory where the requirements.txt file is present, run the command: pip install -r requirements.txt
4. After all the dependencies are installed, run the command (in the same directory as before) - python manage.py migrate
5. The above command intitates all the necessary django table required, if already present it would show no changes.
6. Finally run te command - python manage.py runserver. It would provide you with a localhost url - http://127.0.0.1:8000/home/
7. It would open a page that looks like:

![The page](https://github.com/Siddp278/fetch-take-home/blob/main/img/Screenshot%202023-02-03%20202910.png)
