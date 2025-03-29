# MyHomeAssistant

A web-based home assistant application with task tracking and automation features.

## Features

- Task management and tracking
- Google Sheets integration for data storage
- User authentication and authorization
- Automated task scheduling
- Score tracking system
- Admin panel for user management
- Game-like features for task completion

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Alparslan006/myhomeassistant.git
cd myhomeassistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```
SECRET_KEY=your-secret-key
SHEET_ID=your-google-sheet-id
```

5. Set up Google Sheets API:
- Create a project in Google Cloud Console
- Enable Google Sheets API
- Create credentials (Service Account)
- Download the credentials as `credentials.json` and place it in the project root

6. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5500`

## Project Structure

- `app.py`: Main application file
- `config.py`: Configuration settings
- `routes/`: Blueprint route handlers
- `services/`: Business logic and external service integrations
- `models/`: Data models
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Security Notes

- Never commit sensitive information like API keys or credentials
- Use environment variables for configuration
- Keep `credentials.json` and `.env` files secure and never commit them
- In production, enable secure session cookies and use HTTPS