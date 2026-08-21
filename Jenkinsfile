pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Automatically clones your GitHub repository into the workspace
                git branch: 'main', url: 'https://github.com/Dineshmech0397/Employee-Management-Website.git'
            }
        }
        stage('Deploy Containers') {
            steps {
                sh '''
                    # 1. Ensure network and Persistent Volume exist
                    docker network create 3tier-network || true
                    docker volume create db_volume || true

                    # 2. Build Fresh Docker Images from workspace files
                    docker build -t frontend:emp-app ./frontend
                    docker build -t backend:emp-app ./backend
                    docker build -t database:emp-app ./database

                    # 3. Stop and remove old containers (Data is safe in the volume!)
                    docker stop emp-frontend emp-backend emp-database || true
                    docker rm emp-frontend emp-backend emp-database || true

                    # 4. Run Database Container WITH VOLUME MOUNT
                    docker run -d --name emp-database \
                        --network 3tier-network \
                        -v db_volume:/var/lib/mysql \
                        -e MYSQL_DATABASE=employee_db \
                        -e MYSQL_ROOT_PASSWORD=password \
                        -p 3306:3306 \
                        database:emp-app

                    # 5. Run Backend Container
                    docker run -d --name emp-backend \
                        --network 3tier-network \
                        -e DB_HOST=emp-database \
                        -e DB_PORT=3306 \
                        -e DB_NAME=employee_db \
                        -e DB_USER=root \
                        -e DB_PASSWORD=password \
                        -p 5000:5000 \
                        backend:emp-app

                    # 6. Run Frontend Container
                    docker run -d --name emp-frontend \
                        --network 3tier-network \
                        -p 80:80 \
                        frontend:emp-app
                '''
            }
        }
    }
}
