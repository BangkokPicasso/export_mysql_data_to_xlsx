# Export MySQL Data to Excel

This project provides a simple Python script to connect to a MySQL database, execute a query, and export the result to an Excel file using `pandas` and `pymysql`. This script is useful for data analysts and developers who need to extract data from MySQL databases and save it in a user-friendly Excel format for further analysis or reporting.

## Features

- Connects to a MySQL database using `pymysql`.
- Executes a specified SQL query to fetch data.
- Loads the data into a `pandas` DataFrame for easy manipulation.
- Exports the DataFrame to an Excel file using `pandas`.

## How to Use

1. **Install Required Libraries**: Ensure you have `pymysql` and `pandas` installed.
   ```sh
     pip install pymysql pandas
    ```
2. **Configure Database Connection**: Update the connection parameters (host, user, password, db) in the script.
3. **Run the Script**: Execute the script to export data from your MySQL database to an Excel file.
   ```sh
    python export_mysql_data_to_xlsx.py
    ```

## Example
This script connects to a local MySQL database, fetches data from SchemeName.TableName, and exports it to output.xlsx.

## Related Repositories
* [Excel_to_MySQL_Importer](https://github.com/BangkokPicasso/Excel_to_MySQL_Importer): a Python script to import data from an Excel file into a MySQL database
* [df_to_mysql_table_statement_generator](https://github.com/BangkokPicasso/df_to_mysql_table_statement_generator): Converting a Pandas DataFrame into a MySQL CREATE TABLE statement
  
## Prerequisites
* Python 3.x
* MySQL server
* Necessary Python libraries: pymysql, pandas

## Notes
* Ensure your MySQL server is running and accessible.
* Update the SQL query to match your specific requirements
