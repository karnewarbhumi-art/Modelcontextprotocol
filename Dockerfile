# Dockerfile

# Use the official Golang image as a base image
FROM golang:1.20-alpine AS builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy the Go Modules manifests
COPY go.mod .
COPY go.sum .

# Download all dependencies. Dependency management is enforced when using the Go modules
RUN go mod download

# Copy the source code into the container
COPY . .

# Build the Go app
RUN go build -o weather-agent ./...

# Start a new stage from scratch
FROM alpine:latest

# Set the Current Working Directory inside the container
WORKDIR /root/

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /app/weather-agent .

# Command to run the executable
CMD ["./weather-agent"]
