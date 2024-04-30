<div align="center">
<a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100"></a>
</div>

<h1 align="center">Python Clean Architecture</h1>

Clean architecture, as defined by [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin) in his book **Clean Architecture: A Craftsman's Guide to Software Structure and Design** emphasizes the separation of concerns into distinct layers to promote modularity, testing, and code maintenance.

## Installation
1. Clone the repository to your local environment:
```bash
git clone https://github.com/wesleey/python-clean-architecture.git
```
2. Navigate to the project directory:
```bash
cd python-clean-architecture
```
3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate     # For Windows
```
4. Install dependencies using pip3:
```
pip3 install -r requirements.txt
```
5. Install pre-commit hooks:
```bash
pre-commit install
```

## Database Migrations
After installing and configuring the database, you can apply the necessary migrations using the following command:
```bash
alembic upgrade head
```

## Usage
### Run the In-Memory CLI
```bash
python cli_memory_process_handler.py
```
### Run the In-Memory Flask API
```bash
python flask_memory_process_handler.py
```
### Run the PostgreSQL Flask API
```bash
python flask_process_handler.py
```

## Testing Flask APIs
```bash
curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john@example.com"}' http://localhost:5000/v1/user/
```
Make sure the Flask server is running before making requests using cURL.

## Commands
### Docker
#### Starts containers in the background
```bash
docker compose up -d
```
#### Stops containers
```bash
docker compose down
```
#### Show all running containers
```bash
docker ps
```
#### Open shell in running container
```bash
docker exec -it <container_id> bash
```
#### Exit the shell
```bash
exit
```
### PostgreSQL
#### Show all users
```bash
psql -U db_user -d db_name -c "SELECT * FROM users"
```
#### Delete all users
```bash
psql -U db_user -d db_name -c "DELETE FROM users"
```
#### Delete user by email
```bash
psql -U db_user -d db_name -c "DELETE FROM users WHERE email = '<user_email>'"
```

## References
- [Python Clean Architecture In-memory CLI implementation](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-1-cli-watanabe/)
- [Error Handling, Logging and Validation implementation in Python Clean Architecture](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-2-error-watanabe/)
- [Python Clean Architecture Flask Web API In-memory implementation](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-3-adding-watanabe/)
- [Python Clean Architecture Flask Web API Postgresql implementation](https://github.com/claudiosw/python-clean-architecture-example/pulse/implementation-clean-architecture-python-part-4-adding-watanabe)

## License
This project is licensed under the [MIT License](./LICENSE).
