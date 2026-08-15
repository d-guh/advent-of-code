// Day 1: Secret Entrance, Part 2

use std::error::Error;
use std::fs;

const FILE_PATH: &str = "../.input";
const DIAL_SIZE: i32 = 100;

fn main() -> Result<(), Box<dyn Error>> {
    let mut position: i32 = 50;
    let mut password: i32 = 0;

    let contents: String = fs::read_to_string(FILE_PATH).expect("Unable to read file");

    for line in contents.lines() {
        //println!("DEBUG: line: {}", line);
        //let direction: char = line[..1].parse()?;  // Slightly more robust?
        let direction: char = line.as_bytes()[0] as char;  // Technically faster! (assumes correct encoding)
        let magnitude: i32 = line[1..].parse()?;
        //println!("DEBUG: dir: {} mag: {}", direction, magnitude);

        //print!("DEBUG: {}", position);  // DEBUG GROUP1 PT1
        let dist_to_zero: i32 = match direction {
            'L' => if position == 0 { DIAL_SIZE } else { position },
            'R' => if position == 0 { DIAL_SIZE } else { DIAL_SIZE - position },
            _ => {
                eprintln!("Invalid direction: (skipping {})", line);
                continue;
            }
        };

        match direction {
            'L' => position -= magnitude,
            'R' => position += magnitude,
            _ => {
                eprintln!("Invalid direction: (skipping {})", line);
                continue;
            }
        }

        // Euclidean remainder & assignment required in this part
        // We need the accurate "real" position to calculate dist_to_zero
        position = position.rem_euclid(DIAL_SIZE);
        
        // NOTE: rem_euclid is equivalent to replacing the above match with:
        // 'L' => position = ((position - magnitude) % 100 + 100) % 100,
        // 'R' => position = (position + magnitude) % 100,

        // Calculate number of times passing zero (includes landing)
        if magnitude >= dist_to_zero {
            password += 1 + (magnitude - dist_to_zero) / 100;  // 0-rounded division
        }

        //println!(" -> {} -> {}", line, position);  // DEBUG GROUP1 PT2
    }

    println!("Password: {}", password);  // ANSWER: 5815
    Ok(())
}
