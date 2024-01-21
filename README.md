# Shor URL Generator

This project is a URL shortener that generates short links for given long URLs.

## Docker Compose Setup

To run the project using Docker Compose, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/raqp/url_shortener.git
    cd url_shortener
    ```



2. Create a `.env` file with the necessary environment variables. You can use the provided example file:

    ```bash
    cp .env.example .env
    ```

    Edit the `.env` file and fill in the required values.



3. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

   This command will build the Docker images and start the containers based on the configuration in `docker-compose.yml`.



4. Access your application:

    By default, the application should be accessible at http://127.0.0.1:8000/.

### Running Documentation

You can access the full documentation for your API by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). This will provide detailed information on all available endpoints, request/response examples, and more.

## Contact

For any questions, issues, or feedback, feel free to reach out at [rafik.parsyan.1998@gmail.com].
