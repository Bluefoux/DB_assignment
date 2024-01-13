# Node.js is the base image
FROM node:latest

# Working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json files
COPY package.json .
COPY package-lock.json .

# Install dependencies
RUN npm install

# Copy the rest to working directory
COPY . .

# Build the app
RUN npm run build

ENV NODE_ENV=production

# Set the command to run the app when the container starts
CMD ["npm", "run", "dev"]
