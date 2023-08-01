
        FROM rust:latest as builder
        WORKDIR /usr/src

        COPY ./ ./
        RUN cargo build --release

        FROM debian:buster-slim
        COPY --from=builder /usr/src/target/release/main.rs /usr/local/bin
        CMD ["main.rs"]
        