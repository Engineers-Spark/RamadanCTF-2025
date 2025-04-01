# Base image (using Ubuntu)
FROM ubuntu:latest

# Install necessary tools (optional, for analysis inside the container)
RUN apt update && apt install -y file tar

# Copy the shared library into the container
COPY lib.so /usr/lib/lib.so

# Set working directory
WORKDIR /usr/lib

# Provide a hint for players
CMD echo "it's easier than you think"
