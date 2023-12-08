import argparse
from datetime import datetime

import psycopg2

from settings import DATABASE_NAME, DEFAULT_STUDY_DATETIME_MAX


def to_datetime(value):
    return datetime.strptime(value, "%Y-%m-%d")


def display_study_totals_report(employee_id, pgy_n):
    con = psycopg2.connect(dbname=DATABASE_NAME, host="localhost", user="postgres")
    cur = con.cursor()
    cur.execute(
        """
        SELECT sq1.Body_part, sq1.Imaging_modality, sq1.Requirement_source, sq1.required_quantity, COALESCE(sq2.actual_count, 0)
        FROM 
        (
            -- Get requirements for the desired Employee and PGY-n
            SELECT tr.Body_part, tr.Imaging_modality, tr.Requirement_source, tr.Quantity as required_quantity
            FROM
            IS_ASSIGNED isa JOIN TRAINEE_REQUIREMENT tr ON isa.Requirement_id = tr.Id
            WHERE
            isa.Employee_id = %s and tr.PGY_n = %s
        ) AS sq1
        LEFT JOIN
        (
            -- Get actual studies authored by desired Employee in correct date range
            SELECT Body_part, Imaging_modality, COUNT(*) as actual_count
            FROM
            STUDY s
            WHERE EXISTS
            (
                SELECT rr.Accession_number
                FROM 
                REPORT_REVISION rr
                JOIN
                EMPLOYMENT e
                ON
                rr.Author = e.Employee_id
                WHERE 
                s.Accession_number = rr.Accession_number
                AND
                rr.Author = %s
                AND
                e.PGY_n = %s
                AND
                rr.Date_time_saved BETWEEN e.Start_date AND COALESCE(e.End_date, %s)
            )
            GROUP BY Body_part, Imaging_modality
        ) AS sq2
        ON
        sq1.Body_part = sq2.Body_part AND sq1.Imaging_modality = sq2.Imaging_modality;
        """,
        (employee_id, pgy_n, employee_id, pgy_n, to_datetime(DEFAULT_STUDY_DATETIME_MAX))
    )
    results = cur.fetchall()
    print("{:=^50}".format(" BEGIN 'DISPLAY STUDY TOTALS' REPORT "))
    print()
    print("Search parameters:")
    print(f"Employee ID = {employee_id!r}")
    print(f"PGY-n = {pgy_n}")
    print()
    print(f"Found {len(results)} requirements")
    if results:
        print(f"{'Requirement':>15}{'Body part':>15}{'Imaging modality':>20}{'Source':>15}{'Required amount':>17}{'Actual amount':>15}")
        for i, result in enumerate(results, start=1):
            print("{:>15}".format(f"({i})"), end="")
            print("{:>15}".format(result[0]), end="")
            print("{:>20}".format(result[1]), end="")
            print("{:>15}".format(result[2]), end="")
            print("{:>17}".format(result[3]), end="")
            print("{:>15}".format(result[4]), end="")
            print()
    print()
    print("{:=^50}".format(" END 'DISPLAY STUDY TOTALS' REPORT "))
    cur.close()
    con.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--employee-id", "-E", required=True)
    parser.add_argument("--pgy-n", "-p", required=True)
    args = parser.parse_args()
    display_study_totals_report(args.employee_id, args.pgy_n)
