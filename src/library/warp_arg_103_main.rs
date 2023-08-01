use std::env;
use warp::Filter;

#[tokio::main]
async fn main() {
    // Get the directory name from the first command-line argument
    let args: Vec<String> = env::args().collect();
    let directory = &args[1];

    // Serve files from the specified directory
    let route = warp::fs::dir(directory);

    warp::serve(route).run(([0, 0, 0, 0], 80)).await;
}

