import connector as etlfns


def load(df):
    """
    Load data
    """

    load_qs = """
    INSERT INTO db."gendercounts" (
        "gender", "count"
        )
    VALUES (
        %s, %s
        )
    """

    pgconn = etlfns.pg_conn()
    print(df.tail())
    etlfns.pg_load(pgconn, load_qs, df, page_size=100)