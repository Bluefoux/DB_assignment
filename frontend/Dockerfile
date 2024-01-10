# Node.js is the base image
FROM node:latest

# working directory in the container
WORKDIR /app

# copy the json files to the working directory
COPY package.json .
COPY package-lock.json .

# install dependencies
RUN npm install

# copy the rest to working directory
COPY . .

# building the app
RUN npm run build

ENV DEVELOPMENT=prod

ENV LISTEN_PORT 8500
EXPOSE 8500

# Set the command to run the app when the container starts
CMD ["npm", "start"]