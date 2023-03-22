import datetime as dt
import time as tt

from pytz import timezone

# ETL libs
import extract as ext
import transform as xform
import load as ld


def main():
    """
    The ETL program
    """

    tz = timezone('America/Los_Angeles')
    start_time = dt.datetime.now(tz).timestamp()
    while True:
        dfe = ext.extract()
        dft = xform.transform(dfe)
        print(dft)
        ld.load(dft)
        print("ETL ran and uploaded the data")
        # go to sleep for 1 day - runtime (run the next day)
        end_time = dt.datetime.now(tz).timestamp()
        run_time = (end_time - start_time)
        now = dt.datetime.now(tz).timestamp()
        now_plus_24hrs = \
            (dt.datetime.now(tz) + dt.timedelta(days=1)).timestamp()
        now_RT = now + run_time
        secss = (now_plus_24hrs - now_RT)
        print(f'Sleeping for {secss} seconds')
        tt.sleep(secss)


if __name__ == "__main__":
    main()
