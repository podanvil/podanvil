use actix_web::{get, web, App, HttpResponse, HttpServer, middleware};
use actix_files as fs;
use std::io;
use std::sync::Mutex;

// Shared application state
struct AppState {
    // This can be anything you need to share across handlers
    // (database connections, configuration, etc)
    server_name: Mutex<String>,
}

#[get("/{filename:.*}")]
async fn index(filename: web::Path<String>, data: web::Data<AppState>) -> HttpResponse {
    let contents = std::fs::read_to_string(&filename.into_inner())
        .unwrap_or_else(|_| String::from("File not found"));

    let server_name = data.server_name.lock().unwrap().clone();

    HttpResponse::Ok()
        .header("Content-Type", "text/html")
        .header("X-Server-Name", &*server_name)
        .body(contents)
}

#[actix_web::main]
async fn main() -> io::Result<()> {
    let server_name = String::from("My Server");

    HttpServer::new(move || {
        App::new()
            .data(AppState {
                server_name: Mutex::new(server_name.clone()),
            })
            // enable logger
            .wrap(middleware::Logger::default())
            // gzip or deflate
            .wrap(middleware::Compress::default())
            .service(index)
            .service(
                // serve static files
                fs::Files::new("/static", "./static")
                    .show_files_listing()
                    .use_last_modified(true),
            )
    })
    .bind("0.0.0.0:80")?
    .workers(4)  // <-- number of worker threads
    .run()
    .await
}

