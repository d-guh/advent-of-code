// Day 1: Secret Entrance, Part 1

use std::io::{self, BufRead};
use std::fs::File;

const FILE_PATH: &str = "../.input";

// Result handling is much better than a bunch of expect calls
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut position: i32 = 50;
    let mut count: i32 = 0;

    let file: File = File::open(FILE_PATH)?;
    let reader: io::BufReader<File> = io::BufReader::new(file);

    for line in reader.lines() {
        let line: String = line?;
        let direction: char = line.chars().next().unwrap_or(' ');
        let value: i32 = line[1..].parse()?;

        match direction {
            'L' => {
                position -= value;
                // println!("DEBUG: {}: {}", line, position);
            },
            'R' => {
                position += value;
                // println!("DEBUG: {}: {}", line, position);
            },
            _ => {
                eprintln!("How did you get here? (skipping {})", line);
                continue;
            }
        }

        position %= 100;  // Actual position
        count += (position == 0) as i32;  // Bool trick + type hint
        // println!("DEBUG: {}", position);
    }

    println!("Final count: {}", count);
    Ok(())
}
