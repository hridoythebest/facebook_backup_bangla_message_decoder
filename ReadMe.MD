# Extract Customer Details from JSON Files

This Python script extracts customer chat history from multiple JSON files stored in different folders. It converts unsupported characters into readable Bengali characters and saves the extracted data into a CSV file.

## Features

- Recursively processes folders containing JSON files.
- Converts unsupported characters into readable Bengali characters using the `ftfy` library.
- Extracts sender name, message content, and timestamp from the chat history.
- Saves the extracted data into a CSV file.

## Prerequisites

- Python 3.x
- `ftfy` library

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
