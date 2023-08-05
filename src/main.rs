use std::env;
use warp::Filter;
use log::{info, debug, error};

#[tokio::main]
async fn main() {
    env_logger::init();

    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        error!("Usage: {} [directory]", args[0]);
        std::process::exit(1);
    }

    let directory = args[1].clone();
    info!("Serving files from directory: {}", directory);

    let route = warp::fs::dir(directory.clone());
    debug!("Created route for directory: {}", directory);

    let ip = [127, 0, 0, 1];
    let port = 80;
    info!("Starting server at {}:{}", ip[0], port);
    
    let (_, server) = warp::serve(route).bind_with_graceful_shutdown((ip, port), async {
        tokio::signal::ctrl_c().await.unwrap();
        println!("Ctrl-C received, shutting down");
    });
    server.await;
}
