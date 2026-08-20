pipeline {
    agent any

    stages {
        stage('Deploy to AWS EC2') {
            steps {
                sh '''
                    # 1. Pull latest code
                    cd ~/Employee-Management-Website
                    git pull origin main

                    # 2. Ensure network and Persistent Volume exist
                    docker network create 3tier-network || true
                    docker volume create db_volume || true

                    # 3. Build Fresh Docker Images
                    docker build -t frontend:emp-app ./frontend
                    docker build -t backend:emp-app ./backend
                    docker build -t database:emp-app ./database

                    # 4. Stop and remove old containers (Data is safe in the volume!)
                    docker stop emp-frontend emp-backend emp-database || true
                    docker rm emp-frontend emp-backend emp-database || true

                    # 5. Run Database Container WITH VOLUME MOUNT
                    docker run -d --name emp-database \
                        --network 3tier-network \
                        -v db_volume:/var/lib/mysql \
                        -e MYSQL_DATABASE=employee_db \
                        -e MYSQL_ROOT_PASSWORD=password \
                        -p 3306:3306 \
                        database:emp-app

                    # 6. Run Backend Container
                    docker run -d --name emp-backend \
                        --network 3tier-network \
                        -e DB_HOST=emp-database \
                        -e DB_PORT=3306 \
                        -e DB_NAME=employee_db \
                        -e DB_USER=root \
                        -e DB_PASSWORD=password \
                        -p 5000:5000 \
                        backend:emp-app

                    # 7. Run Frontend Container
                    docker run -d --name emp-frontend \
                        --network 3tier-network \
                        -p 80:80 \
                        frontend:emp-app
                '''
            }
        }
    }
}
