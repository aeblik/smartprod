# Cloud Storage and Databse Integration Demo
This technical demonstration showcases the integration of cloud object storage (MinIO) with a relational database (PostgreSQL) using a Flask application. It shows how unstructured file data (e.g. images, documents) can be stored in cloud object storage while structured metadata is stored in a relational database. 

## Features
Flask API: Handles file uploads and metadata management

MinIO: S3-compatible object storage for storing files

PostgreSQL: Stores file metadata

Presigned URLs: Provides secure access to stored files

## Prerequisites
Docker
Docker Compose
Git

## Getting Started
1. Clone the Repository
`git clone https://github.com/aeblik/smartprod.git`
2. Build and run containers
`docker-compose up --build`
3. Access Services
Flask App: http://localhost:5000
MinIO Console: http://localhost:9001
  Username: minio
  Password: minio123
PostgreSQL: runs on port 5432 (accessible with "postgres" user and "password")

## Usage
Upload a File: Use the web interface to upload files

List Files: Uploaded Files are listed and can also be axxessed through the MinIO console

Donwload Files: Click on a File in the MinIO console

## Notes
Adjust credentials and ports in `.env` if needed
