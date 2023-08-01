use actix_web::{get, App, HttpResponse, HttpServer, Responder};
use std::fs;
use std::io;

#[get("/{filename:.*}")]
async fn index(filename: actix_web::web::Path<String>) -> impl Responder {
    let contents = fs::read_to_string(filename.into_inner()).unwrap_or_else(|_| String::from("File not found"));

    HttpResponse::Ok()
        .header("Content-Type", "text/html")
        .body(contents)
}

#[actix_web::main]
async fn main() -> io::Result<()> {
    let addr = "0.0.0.0:80";
    println!("Server listening on http://{}", addr);

    HttpServer::new(|| App::new().service(index))
        .bind(addr)?
        .run()
        .await
}

