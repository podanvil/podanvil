# Use the latest version of Rust #Updated! TY!
FROM rust

# Set the working directory in the Docker image
WORKDIR /

# Copy the Rust application into the Docker image
COPY . . #is this ok?

# Build the Rust application
RUN cargo build --release

# Create a directory for the website files
#RUN mkdir /app/content

# Copy the website files into the Docker image
COPY ./thaodean.com /thaodean.com #or whatver url was defined to identify this based on nmaing convetntion, like now i have this so i can also use it as a command line parameter if needed, but only then, what do you think?
So how to serve this now?

# Configure the Rust server to serve files from /app/content
# This depends on your specific Rust server setup

# Run the Rust application
CMD ["cargo", "run", "--release"]

# Expose port 80
EXPOSE 80
#good?
