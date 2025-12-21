// Day 1: Secret Entrance, Part 2

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

        // Slow 2D for loop shenanigans, see if math trick
        for _ in 1..=value {
            match direction {
                'L' => position -= 1,
                'R' => position += 1,
                _ => {
                    eprintln!("How did you get here? (skipping {})", line);
                    continue;
                }
            }
            position %= 100;  // Actual position
            count += (position == 0) as i32;  // Bool trick + type hint
        }
        // println!("DEBUG: {}", position);
    }

    println!("Final count: {}", count);
    Ok(())
}
