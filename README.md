**A personal assistant that walks me through my day, so keeping track of deadlines and to-dos doesn't have to be my first priority.**

Donna is a Python app that loads, stores, and filters my upcoming events, pulls in useful context from third-party APIs (like the weather), and is growing into an LLM-powered assistant that can answer questions about my own schedule and data.

> 🚧 **Status:** Active development (started August 2026), following an 8-week build plan. See the [Roadmap](#roadmap) below.

---

## Why I built this

Between classes, work, a capstone project, and everything else, it's easy to get overwhelmed. I wanted something that does the remembering for me: a single place that knows what's coming up and tells me what matters today. Donna is also my hands-on way to learn how real assistant-style apps are built, from data storage all the way to retrieval-augmented generation.

## Features

**Current**
- Load upcoming events and store them in a local SQLite database (`donna.db`)
- Filter events (e.g. by date range) to see what's coming up
- Fetch weather data from the OpenWeatherMap API to add context to the day

**Planned**
- Retrieval-augmented generation (RAG) with embeddings over my events and notes
- Connect an LLM to my data so I can ask things like *"What's due this week?"*
- An interface, either a CLI or a simple web app

## Tech stack

| Area | Tools |
|------|-------|
| Language | Python |
| Storage | SQLite |
| External APIs | OpenWeatherMap |
| Planned | Embeddings / RAG, LLM integration, Claude Code |
| Version control | Git & GitHub |

## Getting started

### Prerequisites
- Python 3.10+
- An [OpenWeatherMap](https://openweathermap.org/api) API key

### Installation

```bash
git clone https://github.com/<your-username>/donna.git
cd donna
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
OPENWEATHER_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file or API keys. Make sure `.env` and `donna.db` are listed in `.gitignore`.

### Run

```bash
python main.py
```

## Project structure

```
donna/
├── main.py            # Entry point
├── donna.db           # Local SQLite database (not committed)
├── requirements.txt
├── .env               # API keys (not committed)
└── README.md
```

## Roadmap

- [x] Load and filter upcoming events
- [x] Store events in SQLite
- [x] Integrate a third-party API (OpenWeatherMap)
- [ ] Add embeddings and RAG over personal data
- [ ] Connect an LLM to answer questions about my schedule
- [ ] Build with Claude Code
- [ ] Choose and build an interface (CLI vs. simple web app)

## What I'm learning

- Designing and querying a relational database with SQLite
- Working with REST APIs and managing secrets safely
- How RAG and embeddings let an LLM reason over personal data
- Structuring a personal project with a plan and shipping it incrementally

## Author

**Maria Gabrielle Laquindanum**
Computer Science, minor in Creative Technological Design, University of Colorado Boulder (May 2027)
