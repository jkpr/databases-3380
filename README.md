# Requirements

Have docker installed. We will start up the database using Docker.

# Set up

Create a virtual environment and install the requirements file:

```
python -m venv env/ --prompt .
source env/bin/activate
python -m pip install -r requirements.txt
```

# Running the code

1. Start up the database:

    ```
    docker compose up -d
    ```

1. Initialize the database

    ```
    python create_db.py
    ```

1. Run the queries and get the reports

    ```
    python -m queries.calculate_time_to_finalize -s 2023-12-01 -p 7
    python -m queries.calculate_wrvus -E '000-879-234' -s 2023-12-01
    python -m queries.display_study_totals_report -E '000-776-393' -p 5
    ```