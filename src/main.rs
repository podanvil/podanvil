use std::env;
fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} [directory]", args[0]);
        std::process::exit(1);
    }
    let directory = &args[1];
    let route = warp::fs::dir(directory);
    warp::serve(route).run(([127, 0, 0, 1], 80));
}

