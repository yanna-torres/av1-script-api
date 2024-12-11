# Number Access API

This is a simple Flask API that tracks the number of times a specific number has been accessed. The data is stored in a JSON file.

You can access the application at [https://av1-script-api.onrender.com/](https://av1-script-api.onrender.com/) (there is a possibility that the Render server used may be down, taking a while to restart).

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

## API Endpoints

### GET /number/<number>

This endpoint checks if a number exists in the JSON file and increments its access count.

- **URL:** `/number/<number>`
- **Method:** `GET`
- **URL Params:**
    - [number=[integer]](http://_vscodecontentref_/5) - The number to check.
- **Success Response:**
    - **Code:** 200
    - **Content:** `{"number": "<number>", "accessed": <access_count>}`
