import pymysql
import pandas as pd

if __name__ == '__main__':
    # Connect to the MySQL database
    connection = pymysql.connect(
        host="127.0.0.1", 
        user="UserName", 
        password="password", 
        db="DBName", 
        charset="utf8"
    )

    try:
        # Query to select data from MySQL
        query = """
            SELECT * FROM SchemeName.TableName;
        """

        # Fetch data into a pandas DataFrame
        df = pd.read_sql(query, connection)

        # Close the connection
        connection.close()

        # Export data to an Excel file
        excel_file = 'output.xlsx'
        df.to_excel(excel_file, index=False)

        print("Data exported to", excel_file)

    except Exception as e:
        print("Error:", e)
        connection.close()
