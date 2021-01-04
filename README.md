## Basic Test

Interviewing clients will clone the repo and then go through a set of small programming tasks while sitting with the person giving the interview.  The interviewer will ask for the the client/interviewie to do tasks as they progress through the system.  The ideal situation is that this does not last longer than an hour.

The whole test will be done through an api endpoint that can be hit by using Postman.


## Run Local in a virtual environment

1. Set up application locally

    ```
    # Install the virutalenv
    virtualenv venv

    # Active your virtualenv
    source venv/bin/activate

    # Install the requiremnts
    pip install -r requirements.txt

    # Python migrations
    python manage.py migrate

    ```

2. Run the server

    ```
    # Active your virtualenv (run this command if venv is not activated)
    source venv/bin/activate

    # Python runserver
    python manage.py runserver

    > Python development server started: http://127.0.0.1:8000
    ```

3. Tests
    ```
    # Active your virtualenv (run this command if venv is not activated)
    source venv/bin/activate

    # Python tests
    python manage.py test interview.tests
    ```

