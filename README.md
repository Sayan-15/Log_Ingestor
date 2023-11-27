[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2sZOX9xt)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Log-Ingestor Progect Details</h3>

  <p align="center">
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="[https://github.com/othneildrew/Best-README-Template](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/blob/master/Log_Ingestor%20Demo.mp4)">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![image](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/assets/72929741/a727a102-f389-4634-9829-8b52b2116760)

Developed a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.
Both the systems (the log ingestor and the query interface) can be built using python.
The logs ingested (in the log ingestor) over HTTP, on port `3000`.

Log Ingestion code -> log_ingestor.py (runs on port:3000)
Query Interface code -> query_interface.py (runs on port:3001)
Data Population Script -> data_population_script.py
UI Template -> index.html

(Recommeded IDE -> pyCharm)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

Data population script generates the logging data and passes it to Log Ingestion code. Log ingestion code stores the log into MongoDB cluster with indexing on log_ingest database. Query Interface takes values for each logging paramater, on the basis of which you can extract the required field. It also supports regex and date range search, to extract the required logs. 

### Built With

* Python
* MongoDB
* HTML


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Choose an IDE for the project (preferably PyCharm). Click on 'File' tab and create a new project. Download the codes, from the repository and follow the directory design as shared below.
![image](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/assets/72929741/b2372aa0-633f-4635-8a5a-6d6d2edd56c6)


### Prerequisites

#### Packages
* Flask
  ```sh
  pip install Flask
  ```
* Flask PyMongo
  ```sh
  pip install Flask-PyMongo
  ```
* Flask socketio 
  ```sh
  pip install Flask-SocketIO
  ```
* Requests
  ```sh
  pip install requests
  ```
* Waitress (for windows) (gunicorn for linux)
  ```sh
  pip install waitress
  ```

#### Tools
* MongoDB
* MongoDB Shell
  
### Installation
To run this this project you need to first setup MongoDB and then setup the project directories.

#### MongoDB Setup
  1. Download MongoDB Community version from official site [MongoDB Community Server](https://www.mongodb.com/try/download/community) . In case you want to create cloud solution refeer MongoDB Atlas.
  2. Run downloaded MongoDB file.
  3. For MongoDB version 6.0+ you need to download MongoDB Shell package seperately. [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/install/)
  4. From extracted Mongosh package, copy the files from 'bin' folder and store it into 'bin' folder of MongoDB (C:\Program Files\MongoDB\Server\[version-no]\bin).
  5. Add 'C:\Program Files\MongoDB\Server\[version-no]\bin' to the 'Path' Environment variable in advanced System settings.
  6. Open Command prompt, run 'cmd' command.
  7. On command prompt, execute 'cd C:\Program Files\MongoDB\Server\[version-no]\bin'. You will see somthing like this (snapshot below). Then execute 'mongosh'.
     ![image](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/assets/72929741/bb26549e-c23a-46ee-b8ed-0ebd0614deac)
  8. This will start mongodb shell. Run the below commands to create database and user/password and provide roles to access database:-
     USE log_ingest
     db.createUser(
     {
      user: "username",
      pwd: "password",
      roles: [ { role: "readWrite", db: "log_ingest" } ]
     }
    )
  9. Start mongodb compass and connect database. Save the connection string that needs to be used in source code. You can edit this connection string at your end too.
    ![image](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/assets/72929741/7c3bfd04-6f7e-4be4-8b6c-b6694f11c0c5)
    ![image](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/assets/72929741/b875a786-361b-40a0-8f57-5eaea5e15268)
    ![image](https://github.com/dyte-submissions/november-2023-hiring-Sayan-15/assets/72929741/151e56e9-64e1-4447-85d5-0a06dcbea524)
      
#### Python Packages Setup
  1. Download repository zip file. Extract source files.
  2. Create new Project in PyCharm IDE. And setup project directory with all required files.
  3. Install all the required packages, using pip command.

#### Execution
  1. Execute log_ingestor.py in one terminal.
  2. Run query_interface.py in another terminal.
  3. To populate log data, run data_population_script.py in another terminal. Each execution will generate one new entry.
  4. Open local host URL. Or MongoDB compass to see the entry.
  5. You can fetch required logs using filters of UI interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - Sayandeep Ghosh 

Email - sayandeep2900@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


