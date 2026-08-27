"""Saitama Training"""

def exercise():
    pushup = int(input())
    situp = int(input())
    squat = int(input())
    run = int(input())

    pushup_per_day = int(input())
    situp_per_day = int(input())
    run_per_day = int(input())
    squat_per_day = int(input())

    days_pushup = (pushup + pushup_per_day - 1) // pushup_per_day
    days_situp = (situp + situp_per_day - 1) // situp_per_day
    days_squat = (squat + squat_per_day - 1) // squat_per_day
    days_run = (run + run_per_day - 1) // run_per_day

    days = max(days_pushup, days_situp, days_squat, days_run)

    print(days)

exercise()
