# Use the latest version of Rust
FROM rust as builder

# Set the working directory in the Docker image
WORKDIR /app

# Copy the Rust application into the Docker image
COPY . .

# Build the Rust application
RUN cargo build --release

# Start a new build stage
FROM debian:buster-slim

# Set the working directory in the Docker image
WORKDIR /

# Copy the compiled Rust binary into the Docker image
COPY --from=builder /app/target/release/podanvil /podanvil

# Use a build argument to specify the URL
ARG URL

# Copy the website content into the Docker image
COPY ./${URL} /${URL}

# Run the Rust application, specifying the directory to serve files from
CMD ["/podanvil"]

# Expose port 80
EXPOSE 80

