// Day 2: Gift Shop, Part 2

use std::fs::File;
use std::io::{BufRead, BufReader};

const FILE_PATH: &str = "../.input";

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut invalid_total: u64 = 0;

    let file: File = File::open(FILE_PATH)?;
    let reader: BufReader<File> = BufReader::new(file);

    for line in reader.lines() {
        let id_ranges_full: String = line?;
        // println!("DEBUG: all ranges full: {}", &id_ranges_full);
        
        let id_ranges: Vec<&str> = id_ranges_full.split(',').collect();
        // println!("DEBUG: all ranges list: {:?}", &id_ranges)

        for id_range in id_ranges {
            let id_range_split: Vec<&str> = id_range.split('-').collect();
            // println!("DEBUG: each range: {:?}", &id_range_split);
            let start_id: &str = id_range_split[0];
            let end_id: &str = id_range_split[1];

            let start_id_num: u64 = start_id.parse::<u64>().unwrap_or(0);
            let end_id_num: u64 = end_id.parse::<u64>().unwrap_or(0);
            // println!("DEBUG: num range: {}-{}", &start_id_num, &end_id_num);

            for cur_id in start_id_num..=end_id_num {
                let id_str: &str = &cur_id.to_string();
                let length: &usize = &id_str.len();
                // println!("DEBUG: len: {}", &length);
                let half_length: usize = length / 2;

                for i in 1..=half_length {
                    if length % 1 == 0 {
                        let pattern: &str = &id_str[0..i];
                        if pattern.repeat(length / i) == id_str {
                            invalid_total += cur_id;
                            break;
                        }
                    }
                }
            }
        }
    }
    println!("{}", invalid_total);

    Ok(())
}
