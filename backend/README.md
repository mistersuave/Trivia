# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## REST API Reference

### Getting Started
- Base URL: currently the backend flask server runs locally on http://127.0.0.1:5000/
- Authentication: Not yet implemented.

### Error Handling

Flask's @app.errorhandler decorators are implemented for:

- 404: Resource not found
- 422: Unprocessable entity

Errors are returned as JSON objects in the following format:
```bash
{
    "success": False, 
    "error": 404,
    "message": "Resource not found"
}
```
### EndPoints
### Categories

#### GET /categories
- Fetches a dictionary of categories in which the keys are the ids, and the value is the corresponding string of the category
- Request Arguments: None
- @Return Value: The JSON response includes success status, and a dictionary of categories { id: type } stored in the database.
- Example: ``` curl http://127.0.0.1:5000/categories```
```bash
{
    "categories": {
        "1":"Science",
        "2":"Art",
        "3":"Geography",
        "4":"History",
        "5":"Entertainment",
        "6":"Sports"
    },
    "success":true
}
```

#### GET /categories/{category_id}/questions
- Fetches a list of questions that fall inside the request category.
- Request Arguments: <category_id> and Page number (starting from 1)
- @Return Value: The return JSON response includes success , questions, total number of questions, and the current category.The list of questions is paginated in groups of 10 by default.
- Example: ``` curl http://127.0.0.1:5000/categories/6/questions```
```bash
{
  "current_category": 6, 
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
  "success": true, 
  "total_questions": 2
}
```

### Questions

#### GET /questions
- Fetches the list of all the questions in the database.
- Request Arguments: Page Number (starting from 1)
- @Return Value: The JSON response includes a list of questions, the total number of questions, the current category, a list of categories, and a success value. Results are paginated in groups of 10 by default.
- Example: ``` curl http://127.0.0.1:5000/questions```
```bash
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    ..
    ..
     {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 19
}   
```

#### DELETE  /questions/{question_id}
- Deletes the question of the given ID if it exists in the database.
- Request Arguments: <question_id> of the question to be deleted
- @Return Value: The JSON response includes a success value, and the question id of the deleted question.
- Example: ``` curl -X DELETE http://127.0.0.1:5000/questions/25```

```bash
{
  "id": 25, 
  "success": true
}
```

#### POST /questions
- Allows user to post a new question resource using the submitted question, answer, difficulty, and category. Additionally, allows user to get questions based on a search term by sending searchTerm as an argument in POST body expression.
- Request Arguments: POST body expression containing question, answer, difficulty, and category. Additionally, for search searchTerm key is passed in the POST body expression.
- @Return Value: The JSON response includes a success value.
- Example 1: ``` curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "Are tests working?", "answer": "Yes", "difficulty": 1, "category": 3}' ```

```bash
{
  "success": true
}
```
- Example 2: ``` curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "name"}' ```

```bash
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```

#### POST /quizzes
- Fetch questions from the database to play the quiz. It takes a category and list of previous questions' id's as parameters in the POST body expression and returns a random question within the given category, if provided, and that is not one of the previous questions.
- Request Arguments: POST body expression containing a category and list of previous questions.
- @Return Value: The JSON response includes a success value and a random question.
- Example 1: ``` curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "Geography", "id": 3}}'```

```bash
{
  "question": {
    "answer": "Agra", 
    "category": 3, 
    "difficulty": 2, 
    "id": 15, 
    "question": "The Taj Mahal is located in which Indian city?"
  }, 
  "success": true
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python3 test_flaskr.py
```
