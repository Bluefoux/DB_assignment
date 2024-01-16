# Use an official Node.js runtime as a base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

RUN apk update && apk add bash

# Install wait-for-it
ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire application to the working directory
COPY . .

# Build the React app
RUN npm run build

# Copy the entry point script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose the port that the app will run on
EXPOSE 8500

# Specify the command to run your application
CMD ["/wait-for-it.sh", "database_engine:8501", "--", "/entrypoint.sh"]
