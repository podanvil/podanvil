use std::env;
use warp::Filter;
use log::{info, debug, error, warn};

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
    info!("Preparing to start server at {}:{}", ip[0], port);
    
    let server = warp::serve(route)
        .bind_with_graceful_shutdown((ip, port), async {
            info!("Shutdown signal received, starting to shut down...");
            tokio::signal::ctrl_c().await.unwrap();
            info!("Shutdown process completed.");
        });

    match server {
        Ok(_) => {
            info!("Server started successfully at {}:{}", ip[0], port);
            server.await;
            info!("Server has been shut down.");
        },
        Err(e) => {
            error!("Failed to start server at {}:{} due to {:?}", ip[0], port, e);
        }
    }
}
