import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('nitikasasan', 'admin', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # @app.route("/categories", methods=["GET"])
    def test_get_all_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['categories'])

    # @app.route("/questions", methods=["GET"])
    def test_get_all_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))

    # @app.route("/questions/<int:qid>", methods=["DELETE"])
    def test_delete_question(self):
        response = self.client().delete('/questions/2')
        self.assertEqual(response.status_code, 200)

    # @app.route("/questions", methods=["POST"])
    def test_add_new_or_search_questions_1(self):
        response = self.client().post('/questions', json={"question": "Which company's stock soared 695% in 2020?",
                                                          "answer": "Tesla",
                                                          "difficulty": 2,
                                                          "category": 4})
        self.assertEqual(response.status_code, 200)

    # # @app.route("/questions/search", methods=["POST"])
    def test_add_new_or_search_questions_2(self):
        response = self.client().post('/questions', json={"searchTerm": "name"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data['questions']) == 2)
        self.assertEqual(data['total_questions'], 2)

    # @app.route("/categories/<int:cid>/questions", methods=["GET"])
    def test_get_questions_per_category(self):
        response = self.client().get('/categories/5/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'] > 0)

    # # @app.route("/quizzes", methods=["POST"])
    def test_quiz_random_question_generator(self):
        response = self.client().post('/quizzes', json={"previous_questions": [], "quiz_category": {"type": "Geography", "id": 3}})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['question'])

    # @app.errorhandler(404)
    def test_404_get_all_questions(self):
        response = self.client().get('/questions?page=500')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False )

    # @app.errorhandler(422)
    def test_422_quiz_random_question_generator(self):
        response = self.client().post('/quizzes', json={'previous_questions': [], 'id': 5})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()