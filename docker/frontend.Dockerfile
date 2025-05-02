FROM nginx:alpine

# Copy frontend files into nginx HTML directory
COPY ./frontend/ /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]