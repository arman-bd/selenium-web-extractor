# Weaby the Extractor

<img src="res/weaby-header.png" width="100%" />

**Weaby** is a program that can collect data from multiple websites. It is written in **Python** and extracts data from websites using **Selenium**. The project is containerized using **Docker Compose**. (**Undetected Chrome Driver**)[https://github.com/ultrafunkamsterdam/undetected-chromedriver] within the project downloads the most recent version of Chrome Driver to support the current Chrome version, which is installed by **Docker**.

## Installation

### Docker
To install the project, you need to have **Docker** and **Docker Compose** installed on your machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop) and Docker Compose from [here](https://docs.docker.com/compose/install/).

### Project
After installing Docker and Docker Compose, you can clone the project by running the following command:

```bash
git clone https://github.com/arman-bd/weaby-the-extractor.git
```

### Environment

After cloning the project, you need to create a **.env** file in the project directory. You can copy the **.env.example** file and rename it to **.env**. 

```bash
cp .env.example .env
```

You may change the **.env** file according to your needs. To change the **.env** file, open it with a text editor and change the values of the variables.

## Usage

Run the following command to start the project:

```bash
docker-compose --build up -d
```

After running the command, you can access the project by visiting **http://localhost:8081** in your browser.

## Disclaimer

The project is still in development and is not ready for production. The project is not tested thoroughly and may contain bugs. It is designed to be used for educational purposes only. The very purpose of this project is to demonstrate how to use Selenium to interact with a websites. Use at your own risk. I am not responsible for any misuse of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* [Undetected Chrome Driver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
* [Docker](https://www.docker.com/)
* [MongoDB](https://www.mongodb.com/)
* [Selenium](https://www.selenium.dev/)
* [FastAPI](https://fastapi.tiangolo.com/)


