
# Movie Recommender System

This repository contains a **Movie Recommender System** built using Python and Streamlit. It recommends movies to users based on collaborative filtering, making it easy for users to discover movies that match their tastes.

![image](https://github.com/user-attachments/assets/478b304a-4ccf-4820-a2f5-dbe369cda688)


## Features

- **Movie Recommendation**: Get personalized movie recommendations based on selected movies.
- **Streamlit Interface**: A user-friendly web interface built using Streamlit for easy navigation and interaction.
- **Movie Details**: View information such as genres, cast, and other attributes for the recommended movies.

## Project Structure

```
MovieRecommenderSystem/
│
├── app.py                                     # Main Streamlit application script
├── movie-recommender-system.ipynb              # Jupyter notebook for model building and analysis
├── movie-recommender-system-checkpoint.ipynb   # Checkpoint notebook (backup)
├── movies.pkl                                  # Pickle file containing movie data
├── movies_dict.pkl                             # Pickle file with dictionary structure for movies
├── requirements.txt                            # Required dependencies
├── README.md                                   # Project documentation
├── tmdb_5000_credits.csv                       # Dataset containing movie credits information
├── tmdb_5000_movies.csv                        # Dataset containing movie details
├── vercel.json                                 # Configuration for Vercel deployment
└── .gitignore                                  # Files and directories to be ignored in version control
```

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- **pip** (Python package manager)

### Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/MovieRecommenderSystem.git
    cd MovieRecommenderSystem
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    streamlit run app.py
    ```

5. **Open the application in your browser**:

   By default, the app will run on `http://localhost:8501/`. Open this URL in your browser to start using the Movie Recommender System.

## Datasets

The application uses the following datasets:

- `tmdb_5000_movies.csv`: Contains movie details like title, genre, budget, and revenue.
- `tmdb_5000_credits.csv`: Contains information about the cast and crew of the movies.

## Deployment

The application is configured to be deployed on Vercel using the `vercel.json` configuration file. Make sure to install the [Vercel CLI](https://vercel.com/docs/cli) and run:

```bash
vercel deploy
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
