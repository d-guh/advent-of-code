// Day 1: Secret Entrance, Part 1

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
        let direction: char = line[..1].parse()?;
        let magnitude: i32 = line[1..].parse()?;
        //println!("DEBUG: dir: {} mag: {}", direction, magnitude);

        //print!("DEBUG: {}", position);  // DEBUG GROUP1 PT1
        match direction {
            'L' => position -= magnitude,
            'R' => position += magnitude,
            _ => {
                eprintln!("Invalid direction: (skipping {})", line);
                continue;
            }
        }

        // Choice 1: % (remainder)
        // Most efficient, but you have to be careful about integer underflow/overflow
        if (position % DIAL_SIZE) == 0 {
            password += 1;
        }

        // Choice 2: %= (remainder & assignment)
        // Slightly less efficient, helps prevent integer flow issues
        //position %= DIAL_SIZE;
        //if position == 0 {
        //    password += 1
        //}

        // Choice 3: .rem_euclid (euclidean remainder)
        // Less efficient, but clamps to "real" positive values, has integer flow issues
        //if (position.rem_euclid(DIAL_SIZE)) == 0 {
        //    password += 1;
        //}

        // Choice 4: =.rem_euclid (euclidean remainder & assignment)
        // Least efficient, but "real" positional record, helps prevent integer flow issues
        // RECOMMENDED FOR DEBUG/VISUALS
        //position = position.rem_euclid(DIAL_SIZE);
        //if position == 0 {
        //    password += 1
        //}

        //println!(" -> {} -> {}", line, position);  // DEBUG GROUP1 PT2
    }

    println!("Password: {}", password);  // ANSWER: 1018
    Ok(())
}
