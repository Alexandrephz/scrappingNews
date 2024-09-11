# Scraping News

## Objective

The **Scraping News** project is designed to extract content from articles given a URL. This tool scrapes the article content, tags, and link, and then stores this information in a MongoDB database.



## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/scrapingNews.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd scrapingNews
    ```

3. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **MongoDB Configuration:**

    Edit `app/config/config.py` to configure your MongoDB connection settings. Make sure to set the appropriate values for your database connection.

    ```python
    MONGO_URI = 'mongodb://localhost:27017'
    DATABASE_NAME = 'news_scraper'
    ```

2. **Other Settings:**

    Update any additional settings or configurations as needed in `app/config/config.py`.

## Usage

1. **Run the main script:**

    ```bash
    python main.py
    ```

2. **Example Usage:**

    - The script is designed to scrape articles given a URL.
    - Modify `main.py` to include the URLs you want to scrape.

## Code Structure

- **`app/config/config.py`:** Configuration file for MongoDB and other settings.
- **`app/mongo_utils/mongo.py`:** MongoDB utility functions for connecting and interacting with the database.
- **`app/scrapper/scrapper.py`:** Core scraping logic for extracting content from articles.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any questions or issues, please contact [your-email@example.com](mailto:your-email@example.com).

