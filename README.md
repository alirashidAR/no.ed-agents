# No.ed AI Agentic Layer Backend

## Overview
The *No.ed* AI Agentic Layer is the core intelligence behind the *No.ed* platform, helping users find career paths, generate personalized roadmaps, and receive tailored job recommendations. This backend processes user resumes, extracts relevant skills, and dynamically curates career guidance content.

## Features
- **Career Pathway Identification**: Suggests potential career paths based on user input and resume analysis.
- **Roadmap Generation**: Provides structured learning paths with relevant courses, resources, and milestones.
- **Job Recommendations**: Matches users with suitable job opportunities based on their skills and career goals.
- **AI-Driven Content Curation**: Extracts and recommends high-quality learning materials from various sources.

## Tech Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: CockroachDB
- **Authentication**: Firebase Google Authentication
- **AI Components**: 
  - Large Language Models (LLMs) for content extraction and recommendation
  - Embedding-based similarity search for matching job listings
  - Resume parsing using NLP models
- **Data Storage**: Vector database for efficient similarity searches

## API Endpoints
### 1. **Root Endpoint**
- **Endpoint**: `GET /`
- **Description**: Root endpoint for health check.
- **Response**:
  ```json
  "string"
  ```

### 2. **Generate Roadmap**
- **Endpoint**: `POST /roadmap`
- **Description**: Generates a step-by-step roadmap based on user resume and desired role.
- **Request Body**:
  ```json
  {
    "resume": "string",
    "role": "string"
  }
  ```
- **Response**:
  ```json
  "string"
  ```
- **Error Response (422 Validation Error)**:
  ```json
  {
    "detail": [
      {
        "loc": ["string", 0],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

### 3. **Generate Roles**
- **Endpoint**: `POST /recommend_roles`
- **Description**: Generates potential roles based on provided tags (skills, interests, etc.).
- **Request Body**:
  ```json
  {
    "tags": "string"
  }
  ```
- **Response**:
  ```json
  "string"
  ```
- **Error Response (422 Validation Error)**:
  ```json
  {
    "detail": [
      {
        "loc": ["string", 0],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

### 4. **Generate Job Recommendations**
- **Endpoint**: `POST /recommend_jobs`
- **Description**: Provides personalized job listings based on user roles and experience level.
- **Request Body**:
  ```json
  {
    "roles": "string",
    "experience_level": "string"
  }
  ```
- **Response**:
  ```json
  "string"
  ```
- **Error Response (422 Validation Error)**:
  ```json
  {
    "detail": [
      {
        "loc": ["string", 0],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/noed-agent-backend.git
   cd noed-agent-backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```sh
   cp .env.example .env
   ```
   - Add Firebase credentials
   - Configure database connection
   - Add API keys for AI services
   - Example `.env` file:
     ```sh
     HUGGINGFACE_TOKEN=HUGGINGFACE_TOKEN
     GOOGLE_GEN_AI=GOOGLE_GEN_AI
     CLIENT_ID=COURSERA_CLIENT_ID
     CLIENT_SECRET=COURSERA_CLIENT_SECRET
     OPENROUTER_API_KEY=OPENROUTER_API_KEY
     ```
4. Start the server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Future Enhancements
- **Integration with real-time job market trends**
- **Advanced AI-driven skill gap analysis**
- **More personalized roadmap variations**

## Contributing
Feel free to submit pull requests or open issues for improvements!

