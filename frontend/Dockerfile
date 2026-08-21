# 1. Build React App
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 2. Serve with Nginx
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# REMOVE default Nginx configuration file so it doesn't conflict
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom Nginx proxy config into container
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
