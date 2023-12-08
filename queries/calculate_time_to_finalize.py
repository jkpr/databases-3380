import argparse
from datetime import datetime, timedelta

import psycopg2

from settings import (
    DATABASE_NAME,
    DEFAULT_PRIORITY_MIN,
    DEFAULT_PRIORITY_MAX,
    DEFAULT_STUDY_DATETIME_MIN,
    DEFAULT_STUDY_DATETIME_MAX,
)


def to_datetime(value):
    return datetime.strptime(value, "%Y-%m-%d")


def format_timedelta(value):
    if value.days:
        return f"{value.days}d"
    elif value.seconds >= 4 * 60 * 60:
        return f"{value.seconds // (60 * 60)}h"
    elif value.seconds >= 180:
        return f"{value.seconds // 60}m"
    else:
        return f"{value.seconds}s"
    

def get_mean(time_deltas):
    return sum(time_deltas, timedelta()) / len(time_deltas)


def get_median(time_deltas):
    if len(time_deltas) % 2 == 0:
        return get_mean(
            [
                time_deltas[len(time_deltas) // 2],
                time_deltas[len(time_deltas) // 2 + 1],
            ]
        )
    else:
        return time_deltas[(len(time_deltas) + 1) // 2]



def calculate_time_to_finalize(priority_min, priority_max, start_date, end_date):
    con = psycopg2.connect(dbname=DATABASE_NAME, host="localhost", user="postgres")
    cur = con.cursor()
    cur.execute(
        """
        SELECT (r.Date_time_saved - s.Exam_date) as finalize_time
        FROM STUDY s LEFT JOIN REPORT_REVISION r
        ON s.Accession_number = r.Accession_number
        WHERE r.Prelim_or_final = 'final' AND
        s.Priority BETWEEN %s AND %s AND
        s.Exam_date BETWEEN %s AND %s
        ORDER BY finalize_time;
        """,
        (priority_min, priority_max, to_datetime(start_date), to_datetime(end_date))
    )
    results = cur.fetchall()
    time_deltas = [result[0] for result in results]
    print("{:=^50}".format(" BEGIN 'TIME TO FINALIZE' REPORT "))
    print()
    print("Search parameters:")
    print(f"{priority_min:<12} <= Priority  <= {priority_max:>12}")
    print(f"{start_date:<12} <= Exam date <= {end_date:>12}")
    print()
    print(f"Found {len(results)} studies")
    if results:
        print()
        print(f"Min:   {format_timedelta(time_deltas[0]):>6}{' ':18}Median: {format_timedelta(get_median(time_deltas)):>6}")
        print(f"Max:   {format_timedelta(time_deltas[-1]):>6}{' ':18}Mean:   {format_timedelta(get_mean(time_deltas)):>6}")
    print()
    print("{:=^50}".format(" END 'TIME TO FINALIZE' REPORT "))
    cur.close()
    con.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--priority-min", "-p", type=int, default=DEFAULT_PRIORITY_MIN)
    parser.add_argument("--priority-max", "-P", type=int, default=DEFAULT_PRIORITY_MAX)
    parser.add_argument("--start-date", "-s", default=DEFAULT_STUDY_DATETIME_MIN)
    parser.add_argument("--end-date", "-e", default=DEFAULT_STUDY_DATETIME_MAX)
    args = parser.parse_args()
    calculate_time_to_finalize(args.priority_min, args.priority_max, args.start_date, args.end_date)
