FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=employee_db

# Copy the initialization script so it runs automatically when the container starts
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
