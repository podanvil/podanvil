# Our base image
FROM rust as builder

WORKDIR /app

# Copy over our Cargo.toml and build the dependencies
COPY Cargo.toml Cargo.lock ./

# Copy the source and build the application.
COPY ./src ./src
RUN cargo build --release

# Start a new stage
FROM debian

# Install procps
RUN apt-get update && apt-get install -y procps

# Copy the compiled Rust binary into the Docker image
COPY --from=builder /app/target/release/podanvil .
COPY ./thaodean.com ./thaodean.com

# Set the startup command
ENTRYPOINT ["./podanvil"]
CMD ["./thaodean.com"]

