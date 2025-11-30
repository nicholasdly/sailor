# sailor 🏴‍☠️

> A profanity detecting and censoring API built with Python using FastAPI.

> [!CAUTION]
> Due to the nature of this project, this codebase contains profanity and vulgar language strictly for functionality and testing. This project does not condone the use of profanity anywhere else—the goal of this project is to _censor_ profanity, after all. Please proceed with this understanding when reviewing the repository.

## Architecture

This project uses a monorepo structure with two main components:

```
sailor/
├── api/              # Python (FastAPI) backend
│   ├── app/
│   │   ├── data/
│   │   │   └── profanity.txt    # Profanity word list
│   │   ├── main.py              # FastAPI app & endpoints
│   │   └── sailor.py            # Core filtering logic
│   └── tests/                   # Pytest test suite
└── www/              # TypeScript (React) frontend
    └── src/
        ├── components/          # UI components
        ├── lib/                 # Utilities & API fetchers
        └── app.tsx              # Main application
```

### Backend ([`/api`](api))

- **Framework:** FastAPI
- **Language:** Python 3.12+
- **Testing:** pytest
- **Linting:** ruff
- **Package Manager:** uv

### Frontend ([`/www`](www))

- **Framework:** React 19 (Vite)
- **Language:** TypeScript
- **Data Fetching:** SWR
- **UI Components:** shadcn/ui
- **Styling:** tailwindcss

## Getting Started

### Prerequisites

- **Backend:** Python 3.12+, uv
- **Frontend:** Node.js 18+, npm
- **Docker**

### Using Docker

The easiest way to run the entire project is with Docker. This way you won't have to run the backend and frontend individually, and both will automatically reload on changes.

```bash
docker compose up
```

- The API will be available at http://localhost:8000.
- The website will be available at http://localhost:5173.

## Deployment

Both the backend and frontend are deployed on [Fly.io](https://fly.io) using their respective Dockerfiles. This is done automatically via GitHub Actions.

## License

Licensed under the [MIT License](LICENSE), Copyright © 2025
