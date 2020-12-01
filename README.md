# locust_test
trying perfomance framework locust


# Simple test server to play with
Server - https://jsonplaceholder.typicode.com/
To run test server NodeJS required. NodeJS 12 used in provided samples
To run server use command:
```
json-server --watch sample_server/db.json

```
Data file provided in sample_server folder

To use clean data each time execute run_test_server.bat file

```
run_test_server.bat
```
# Install Python 3.6 or later.

# Install Locust using pip.

```
$ pip3 install locust
```

# Run tests

```
locust -f locust_stress.py --host=http://localhost:3333
```
