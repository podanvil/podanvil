# Use the latest version of Rust
FROM rust as builder

# Set the working directory in the Docker image
WORKDIR /app

# Copy only the Cargo.toml and Cargo.lock to make use of Docker cache,
# build dependencies first
COPY Cargo.toml Cargo.lock ./

# Dummy build to cache dependencies
RUN mkdir -p src/ && echo "fn main() {}" > src/main.rs
RUN cargo build --release
RUN rm -rf src/

# Copy the rest of the source code.
COPY ./src ./src

# Build the Rust application
RUN cargo build --release

# Start a new build stage
FROM debian

# Set the working directory in the Docker image
WORKDIR /

# Copy the compiled Rust binary into the Docker image
COPY --from=builder /app/target/release/podanvil /podanvil
RUN mkdir thaodean.com
COPY ./thaodean.com ./thaodean.com #will need to be parameter here, not hardcoded, please modify

# Run the Rust application
CMD ["/podanvil /thaodean.com"]

# Expose port 80
EXPOSE 80

