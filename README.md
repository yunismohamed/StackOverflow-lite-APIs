# StackOverflow-lite Application
# StackOverflow-lite Application Endpoints
## The following are API Endpoints that enable one to:
* Create an account and login
* Post questions
* Delete questions one posts
* Post answers
* View answers to questions
* Accept an answer out of all the answers to his or her question as the preferred answer

## Here is a list of the functioning endpoints

EndPoint | Functionality | Actual routes
---------|---------------|--------------
POST /auth/signup | Register a user | /api/v1/users/register
POST /auth/login | Login a user | /api/v1/users/login
GET /questions | Fetch all questions | /api/v1/questions
