import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="HPXrni34563",
                                  #host="10.101.1.34",
                                  host="node7512-pladaw.app.ruk-com.cloud",
                                  port="11061",
                                  database="CloudDB")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")