Currently Under Construction: Weviate/ Open API Vector Search

Notes:
- remember to activate the virtual environment!
`source .venv/bin/activate`

To run this project:
1. connect to the Weviate db first: `python open_db_connection.py`. This should return TRUE in the console
2. TODO: need to import the data to the collection. Current status:
weaviate.exceptions.WeaviateInsertManyAllFailedError: Every object failed during insertion. Here is the set of all errors: connection to: OpenAI API failed with status: 429 error: You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.
- This appears to be an OpenAPI error, currently troubleshooting
3. The db connection can be stopped by running `python close_db_connection.py`
4. We can run queries on the provided data by running `python queries.py`
