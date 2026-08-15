// Day 1: Secret Entrance, Part 1

use std::error::Error;
use std::fs;

const FILE_PATH: &str = "../.input";

fn main() -> Result<(), Box<dyn Error>> {
    let mut position: i32 = 50;
    let mut count: i32 = 0;

    let contents: String = fs::read_to_string(FILE_PATH).expect("Unable to read file");

    for line in contents.lines() {
        // println!("DEBUG: line: {}", line);
        let direction: char = line[..1].parse()?;
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

        position %= 100;  // a bit slower due to reassignment, helps prevent over/underflow though
        if position == 0 {
            count += 1;
        }
        // println!("DEBUG: {}", position);
    }

    println!("Final count (password): {}", count);
    Ok(())
}
