use warp::Filter;

#[tokio::main]
async fn main() {
    // Serve files from the /thaodean.com directory
    let route = warp::fs::dir("/thaodean.com");

    warp::serve(route).run(([0, 0, 0, 0], 80)).await;
}

