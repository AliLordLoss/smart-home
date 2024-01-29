# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package.json .

# Install dependencies
RUN yarn

# Copy the current directory contents into the container at /app
COPY . .

# Build the Nuxt.js application
RUN yarn build

# Expose port 3000 for the Nuxt.js app
EXPOSE 3000

# Command to run the Nuxt.js app
CMD ["yarn", "start"]
