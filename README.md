Rest-api for collecting different type of sorting and measure time of their working.

App is written with help of framework Flask.

There are integratinal and unit tests. Sortings with result and time of working stored in a NoSQL database - MongoDB.

App is ready for building by docker-compose. To do this, in root directory you should write in console/terminal docker-compose --build up. From docker-compose, the application is run on gunicorn with 4 processes, each with 4 threads.

