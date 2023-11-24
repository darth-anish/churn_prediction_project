# Use an official Nginx image as a parent image
FROM nginx:1.21-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the Nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Make port 80 available to the world outside this container
EXPOSE 80

# Command to run Nginx
CMD ["nginx", "-g", "daemon off;"]