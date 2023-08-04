use std::env;
fn main() {
    let args: Vec<String> = env::args().collect();
    let directory = args[1].clone();
    let route = warp::fs::dir(directory);
    warp::serve(route).run(([127, 0, 0, 1], 80));
}

