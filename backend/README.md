# _project_name_ Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Environment

Its recommended to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual environment for a platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running `pip install -r requirements.txt`. This will install all of the required packages we selected within the `requirements.txt` file.

## Setting up the Database

Find steps to install and [get started with PostgreSQL](https://www.postgresqltutorial.com/install-postgresql/) here.

## Running the server

From within the `./backend` directory, first ensure you are working using your created virtual environment. Then, export the required environment variables in your terminal. Run the following commands after updating the values accordingly:

```
export DATABASE_URL='postgresql://postgres:postgres@localhost:5432/database_name'
export FLASK_APP=app.py
export FLASK_ENV=development
```

After setting the above environment variables, run `flask run` to start the server. The server will run on `http://localhost:5000`.

The endpoints have been gathered in a [postman](https://www.postman.com/) collection to aid ease of use. To run the endpoints using [Postman](https://www.postman.com/) import the postman collection `./project_name.postman_collection.json`.

## Testing the application

To test the application, a [python test script](./test_app.py) has been provided.

Before running,

-   Ensure your working in a virtual environment and that you're in the `./backend` folder.
-   Run the following commands
    ```
    export DATABASE_URL='postgresql://postgres:postgres@localhost:5432/project_name_test'
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

Run the tests with:

```
    dropdb project_name_test
    createdb project_name_test
    python test_app.py
```

## API Reference

Provide the [API documentation URL](some-url) if it exists.
If the endpoints are not a lot, they can be documented here. Use the format below:

This API is currently not deployed to a remote server and has to be run locally to be used. <br/>

**BASE URL**: `http://localhost:5000`

### Error Handling

#### Response Object

Errors are returned as JSON in the following format:

```
{
    "error": 404,
    "message": "The requested resource was not found."
}
```

#### Response Keys

`error` - Status code of the error that occurred. <br>
`message` - Accompanying error message.

#### Status Codes

`400 (Bad request)` - Your request was not properly formatted. <br>
`404 (Not found)` - The requested resource was not found. <br>
`405 (Method not allowed)` - The request method is not allowed. <br>
`422 (Unprocessable)` - The server understood your request but it could not be processed. <br>
`500 (Internal server error)` - Something went wrong on the server. <br>

### Endpoint Library

#### Resource category

#### `GET /categories`

This fetches all the categories and takes in A and returns B.

##### Query Parameters

This endpoint takes in no query parameter.

OR

page: int (optional) - Page number starting from 1.

##### Request Body

This endpoint doesn't require a request body.

##### Sample Request

`curl http://localhost:5000/categories`

##### Sample Response

```
{
    "1": "Science",
    "2", "Art",
    "3": "History"
}
```

#### `POST /categories`

This adds A to the system. It takes in A, B and C.

##### Query Parameters

This endpoint takes in no query parameters

##### Request Body

`type`: string <small> (required) </small> - Category type <br>

```
{"type": "Entertainment"}
```

##### Sample Request

`curl http://localhost:5000/categories -X POST -H "{Content-Type: 'application/json'}" -d '{"type": "Entertainment"}'`

##### Sample Response

`added`: int - Id of the added category. <br>
`success`: boolean - Request success status. <br>

```
{
    "added": 1,
    "success": True
}
```

#### `GET /categories/{item_id}/questions`

This returns all the questions within a particular category.

##### Query Parameters

This endpoint does not take in query parameters.

##### Request Body

This endpoint does not require a request body.

##### Sample Request

`curl http://localhost:5000/categories/`

##### Sample Response

`questions`: array - All questions within the specified category. <br>
`totalQuestions`: int - Total number of questions within specified category. <br>

```
{
  "questions": [
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ],
  "totalQuestions": 2
}
```

#### `DELETE /categories/{question_id}`

This deletes the category with the specified id. It returns the id of the deleted category and a success status.

##### Query Parameters

This endpoint takes in no query parameters.

##### Request Body

This endpoint requires no request body.

##### Sample Request

`curl http://localhost:5000/questions/1 -X DELETE`

##### Sample Response

`deleted`: int - Id of the deleted question. <br>
`success`: boolean - Request success status. <br>

```
{
    "deleted": 1,
    "success": True
}
```
