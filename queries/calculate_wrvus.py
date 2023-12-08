import argparse
from datetime import datetime

import psycopg2

from settings import (
    DATABASE_NAME,
    DEFAULT_STUDY_DATETIME_MIN,
    DEFAULT_STUDY_DATETIME_MAX,
)

def to_datetime(value):
    return datetime.strptime(value, "%Y-%m-%d")


def calculate_wrvus(employee_id, start_date, end_date):
    con = psycopg2.connect(dbname=DATABASE_NAME, host="localhost", user="postgres")
    cur = con.cursor()
    cur.execute(
        """
        SELECT SUM(cpt.wRVU) as total_wrvus, COUNT(cpt.wRVU) as count_wrvus
        FROM 
        REPORT_REVISION r 
        JOIN STUDY s ON s.Accession_number = r.Accession_number
        JOIN CODED_WITH cw ON s.Accession_number = cw.Accession_number
        JOIN CPT_CODE cpt ON cw.CPT_code = cpt.code
        WHERE r.Prelim_or_final = 'final' AND
        r.Author = %s AND
        r.Date_time_saved BETWEEN %s AND %s;
        """,
        (employee_id, to_datetime(start_date), to_datetime(end_date))
    )
    total_wrvus, count = cur.fetchone()
    print("{:=^50}".format(" BEGIN 'CALCULATE wRVUs' REPORT "))
    print()
    print("Search parameters:")
    print(f"Employee ID = {employee_id!r}")
    print(f"{start_date:<12} <= Exam date <= {end_date:>12}")
    print()
    print(f"Found {count} studies")
    if count:
        print()
        print(f"Total wRVUs: {total_wrvus}")
    print()
    print("{:=^50}".format(" END 'CALCULATE wRVUs' REPORT "))
    cur.close()
    con.close()
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--employee-id", "-E", required=True)
    parser.add_argument("--start-date", "-s", default=DEFAULT_STUDY_DATETIME_MIN)
    parser.add_argument("--end-date", "-e", default=DEFAULT_STUDY_DATETIME_MAX)
    args = parser.parse_args()
    calculate_wrvus(args.employee_id, args.start_date, args.end_date)
