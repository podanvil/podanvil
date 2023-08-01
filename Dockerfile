
        FROM rust:latest as builder
        WORKDIR /usr/src

        COPY ./ ./
        RUN cargo build --release

        FROM debian:buster-slim
	COPY --from=builder /usr/src/target/release/podanvil /usr/local/bin

        CMD ["/usr/local/bin/podanvil"]
        
