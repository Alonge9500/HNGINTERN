# Stage 2 Documentation

This documentation provides information about the RESTful API endpoints provided by the Flask application. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on `Person` records in a SQLite database.

### Base URL

The base URL for this API is `http://localhost:5000` if you are running it locally. If hosted elsewhere, replace it with the appropriate base URL.

### Endpoints

#### 1. Create a New Person (POST)

- **Endpoint**: `/person`
- **HTTP Method**: POST
- **Description**: Create a new `Person` record with the provided data.
- **Request Body**: JSON object with the following fields:
  - `name` (string): Name of the person (required).
  - `age` (integer): Age of the person (optional).
  - `gender` (string): Gender of the person (optional).
- **Response**:
  - HTTP Status Code: 200 if successful.
  - JSON response with a "report" field indicating success or failure.

**Example Request:**

```http
POST /person
Content-Type: application/json

{
    "name": "John",
    "age": 30,
    "gender": "Male"
}
```

**Example Response:**

```json
{
    "report": "Successful"
}
```

#### 2. Update a Person (PUT)

- **Endpoint**: `/person/<name>`
- **HTTP Method**: PUT
- **Description**: Update an existing `Person` record with the provided data. The person is identified by their `name`.
- **Request URL Parameters**:
  - `<name>` (string): Name of the person to update.
- **Request Body**: JSON object with the following fields (any combination of fields can be updated):
  - `name` (string): New name of the person (optional).
  - `age` (integer): New age of the person (optional).
  - `gender` (string): New gender of the person (optional).
- **Response**:
  - HTTP Status Code: 200 if successful.
  - JSON response with a "report" field indicating success or failure, and the updated person's information.

**Example Request:**

```http
PUT /person/John
Content-Type: application/json

{
    "age": 35,
    "gender": "Male"
}
```

**Example Response:**

```json
{
    "report": "Update successful",
    "updated_person": {
        "name": "John",
        "age": 35,
        "gender": "Male"
    }
}
```

#### 3. Get a Person (GET)

- **Endpoint**: `/person/<name>`
- **HTTP Method**: GET
- **Description**: Retrieve information about a specific `Person` record by their `name`.
- **Request URL Parameters**:
  - `<name>` (string): Name of the person to retrieve.
- **Response**:
  - HTTP Status Code: 200 if the person is found.
  - JSON response with the person's information including name, age, and gender.
  - If the person is not found, a JSON response with a "report" field indicating "User Not Found" and a 404 status code is returned.

**Example Request:**

```http
GET /person/John
```

**Example Response (if found):**

```json
{
    "name": "John",
    "age": 35,
    "gender": "Male"
}
```

**Example Response (if not found):**

```json
{
    "report": "User Not Found"
}
```

#### 4. Delete a Person (DELETE)

- **Endpoint**: `/person/<name>`
- **HTTP Method**: DELETE
- **Description**: Delete a `Person` record by their `name`.
- **Request URL Parameters**:
  - `<name>` (string): Name of the person to delete.
- **Response**:
  - HTTP Status Code: 200 if the person is successfully deleted.
  - JSON response with a "report" field indicating "Delete successful."
  - If the person is not found, a JSON response with a "report" field indicating "User Not Found" and a 404 status code is returned.

**Example Request:**

```http
DELETE /person/John
```

**Example Response (if successful):**

```json
{
    "report": "Delete successful"
}
```

**Example Response (if not found):**

```json
{
    "report": "User Not Found"
}
```

### Running the API

To run the Flask API locally, execute the script with the following command:

```bash
python your_api_script.py
```

Replace `your_api_script.py` with the filename of your Flask application script. The API will be accessible at `http://localhost:5000`.

### Testing the API

You can use the provided Python script to test all the API endpoints. Modify the data and endpoints in the script as needed to perform tests.

Please ensure that you have the required Python packages (Flask, SQLAlchemy, Flask-Migrate, requests) installed and that the SQLite database (`details.db`) is accessible.
