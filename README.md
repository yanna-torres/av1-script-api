# Number Access API

This is a simple Flask API that tracks the number of times a specific number has been accessed. The data is stored in a JSON file.

You can access the application at [https://av1-script-api.onrender.com/](https://av1-script-api.onrender.com/) (there is a possibility that the Render server used may be down, taking a while to restart, usually 1 minute).

**Table of Contents**
- [Setup](#setup)
- [Running the API](#running-the-api)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
  - [GET /number/<number>](#1-get-number)
  - [GET /](#2-get-)
- [How the Data is Handled](#how-the-data-is-handled)
  - [Data Storage](#data-storage)
  - [Data Structure](#data-structure)


## Setup

1. Clone the repository.
2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the API

1. On th `main.py` file include at the end the following code:
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```
3. Start the Flask server:
    ```sh
    python main.py
    ```
4. The API will be available at `http://127.0.0.1:5000`.

## Project Structure

```bash
av1-script-api/
├── data/
│   └── numbers.json
├── .gitignore
├── README.md
├── index.html
├── main.py
└── requirements.txt
```

## API Endpoints

### 1. **GET /number/<number>**

**Description**:  
This endpoint checks if a specific number exists in the `numbers.json` file. If the number exists, it returns the number of times it has been accessed. If the number does not exist, it initializes the number with an "accessed" count of 1.

**URL**:  
`/number/<number>`

**Method**:  
GET

**URL Parameters**:
- `number` (required): The number to check in the JSON file. This is a string or numeric value.

**Response**:
- **200 OK**: Returns a JSON object with the `number` and its `accessed` count.
  ```json
  {
    "number": "12345",
    "accessed": 2
  }
  ```

**Example Request**: `GET /number/12345`
**Example Response**:
```json
{
  "number": "12345",
  "accessed": 2
}
```

### 2. **GET /**

**Description:**
This endpoint serves the `index.html` file located in the static directory. It is the main entry point to the application.

**URL:**
`/`

**Method:**
GET

**Response**:
- **200 OK**: Returns the HTML content of `index.html`.

## How the Data is Handled

### Data Storage

The application stores data in a local JSON file located in the `./data/numbers.json` path. This file contains a dictionary where each key is a number, and the associated value is an object with the `accessed` count. The data is stored in JSON format to maintain simplicity and ease of access.

### Data Structure

The data in `numbers.json` follows this structure:
```json
{
  "12345": {
    "accessed": 2
  },
  "67890": {
    "accessed": 1
  }
}
```

- **Key:** The number (as a string) that has been accessed.
- **Value:** An object containing:
    - `accessed`: The number of times this specific number has been accessed.
