A simple exploration of using Weaviate for vector search

To run this project locally:
- you will need a Weaviate db instance with API key and database URL saved as .env variables
1. Create and activate your virtual environment
2. Install requirements.txt file: `pip install -r requirements.txt`
3. Connect to the Weviate db: `python open_db_connection.py`. This should return TRUE in the console
4. Create a collection in your db using provided data: `python build_collection.py`
5. Insert data into your new collection: `python insert_data.py`
5. Query data by running: `python queries.py`

- The db connection can be stopped by running `python close_db_connection.py`
