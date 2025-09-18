from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic models
class Task(BaseModel):
    id: int
    name: str
    description: str
    tech: str = ""
    x: float
    y: float
    created_at: str

class Connection(BaseModel):
    id: int
    parent_id: int
    child_id: int

# AI Assistant DAG Structure
DEMO_TASKS = [
    # Root/Main Categories
    {"id": 1, "name": "Wake Word Detection", "description": "Detect wake word using CNN model", "tech": "• TensorFlow / PyTorch (CNN model training)\n• pyaudio (microphone input)\n• Vosk (offline speech recognition)", "x": 400, "y": 50, "created_at": "2025-09-18T10:00:00"},
    {"id": 2, "name": "Voice Interaction", "description": "Capture voice input, process commands with Whisper, convert text to speech", "tech": "• pyaudio/sounddevice (local audio capture)\n• Wave format (local audio storage)\n• Whisper (offline speech-to-text model)\n• PyTorch/TensorFlow (offline local models)\n• pyttsx3 (offline text-to-speech)\n• espeak-ng (offline Linux TTS)", "x": 100, "y": 150, "created_at": "2025-09-18T10:01:00"},
    {"id": 3, "name": "Face Recognition", "description": "Detect faces, authenticate users, optional voice verification", "tech": "• OpenCV (Haar cascades / DNN module)\n• Dlib (high-accuracy face detection)\n• Face Recognition (local facial recognition)\n• PyAudio (voice samples)\n• SpeakerRecognition (local speaker ID)", "x": 700, "y": 150, "created_at": "2025-09-18T10:02:00"},
    {"id": 4, "name": "General AI (Llama 3)", "description": "Process commands, generate responses, provide recommendations", "tech": "• Llama 3 (offline local text generation)\n• Hugging Face Transformers (offline models)\n• Rasa (offline conversational AI)\n• Scikit-learn (local recommendation engines)\n• TensorFlow/PyTorch (offline ML models)\n• ONNX Runtime (optimized inference)", "x": 400, "y": 250, "created_at": "2025-09-18T10:03:00"},
    {"id": 5, "name": "Social Media Integration", "description": "Scrape public data, automate posting, local scripts", "tech": "• BeautifulSoup / Scrapy (web scraping)\n• Selenium (dynamic content scraping)\n• Python Requests (HTTP requests)\n• Selenium (browser automation)", "x": 50, "y": 350, "created_at": "2025-09-18T10:04:00"},
    {"id": 6, "name": "Smart Home Automation", "description": "Control lighting, temperature, voice-based appliances, security cameras", "tech": "• MQTT (local-only device messaging)\n• Home Assistant/openHAB (offline platforms)\n• PySerial (direct device communication)\n• OpenCV (local camera processing)\n• RTSP (local-only video streaming)\n• Raspberry Pi GPIO (direct control)\n• Zigbee/Z-Wave (local mesh networks)", "x": 750, "y": 350, "created_at": "2025-09-18T10:05:00"},
    {"id": 7, "name": "Task Automation", "description": "Automate daily tasks, schedule tasks with cron jobs", "tech": "• Cron Jobs (Linux scheduling)\n• Celery (task queue management)\n• APScheduler (local scheduling)", "x": 200, "y": 450, "created_at": "2025-09-18T10:06:00"},
    {"id": 8, "name": "Web Scraping", "description": "Scrape news updates, weather data from local sources", "tech": "• BeautifulSoup (local website scraping)\n• Scrapy (offline scraping framework)\n• Requests (local HTTP requests)\n• Local RSS feed parsing\n• Custom scrapers (no external APIs)\n• Local data caching", "x": 600, "y": 450, "created_at": "2025-09-18T10:07:00"},
    {"id": 9, "name": "Security", "description": "Encryption of communications, local data protection", "tech": "• PyCryptodome (AES encryption, local data)\n• ssl (secure local connections)\n• SQLite (local database encryption)", "x": 400, "y": 550, "created_at": "2025-09-18T10:08:00"},
    {"id": 10, "name": "User Personalization", "description": "Maintain user preferences, provide personalized responses", "tech": "• SQLite (local preference database)\n• JSON (lightweight local data storage)\n• Rasa (offline chatbot framework)\n• Llama 3 (offline conversational agent)", "x": 100, "y": 650, "created_at": "2025-09-18T10:09:00"},
    {"id": 11, "name": "Device Communication", "description": "Sync data across devices", "tech": "• MQTT (local message passing)\n• WebSocket (real-time communication)", "x": 700, "y": 650, "created_at": "2025-09-18T10:10:00"},
    {"id": 12, "name": "Data Storage", "description": "Backup important files and data locally", "tech": "• Rsync (local backup synchronization)\n• Tar (local backup creation)", "x": 50, "y": 750, "created_at": "2025-09-18T10:11:00"},
    {"id": 13, "name": "Health Monitoring", "description": "Track user activity locally, analyze health data offline", "tech": "• Local health data parsing (no cloud APIs)\n• CSV/JSON local data storage\n• Scikit-learn (offline activity prediction)\n• TensorFlow (local health predictions)\n• Custom health tracking algorithms", "x": 300, "y": 750, "created_at": "2025-09-18T10:12:00"},
    {"id": 14, "name": "System Monitoring", "description": "Monitor system performance and diagnostics", "tech": "• Custom monitoring scripts\n• System resource tracking\n• Performance metrics collection", "x": 550, "y": 750, "created_at": "2025-09-18T10:13:00"},
    {"id": 15, "name": "Data Analytics", "description": "Generate usage insights and reporting", "tech": "• Scikit-learn (data analysis)\n• TensorFlow (predictive modeling)\n• Data visualization libraries", "x": 800, "y": 750, "created_at": "2025-09-18T10:14:00"},
    {"id": 16, "name": "Offline Capabilities", "description": "Local processing without internet connectivity", "tech": "• Local model inference\n• Offline speech recognition\n• Local data processing", "x": 200, "y": 850, "created_at": "2025-09-18T10:15:00"},
    {"id": 17, "name": "Emotional Intelligence", "description": "Detect user emotions, respond empathetically", "tech": "• DeepMoji (offline emotion detection)\n• OpenSmile (local audio emotion analysis)\n• Hugging Face Transformers (offline sentiment)\n• Llama 3 (offline emotional responses)\n• Custom emotion recognition models", "x": 600, "y": 850, "created_at": "2025-09-18T10:16:00"},
    {"id": 18, "name": "Creativity", "description": "Generate stories, poems, creative content, suggest hobbies", "tech": "• GPT-2/Llama 3 (offline content generation)\n• Rasa (offline creative conversations)\n• Scikit-learn (local hobby recommendations)\n• TensorFlow/PyTorch (offline ML models)\n• Custom creativity algorithms", "x": 100, "y": 950, "created_at": "2025-09-18T10:17:00"},
    {"id": 19, "name": "Social Interaction", "description": "Natural conversation with humor and personality", "tech": "• Llama 3 (natural conversation)\n• Humor generation algorithms\n• Personality modeling", "x": 400, "y": 950, "created_at": "2025-09-18T10:18:00"},
    {"id": 20, "name": "Life Management", "description": "Personal assistant for daily life management", "tech": "• Task scheduling algorithms\n• Calendar integration\n• Reminder systems\n• Productivity tracking", "x": 700, "y": 950, "created_at": "2025-09-18T10:19:00"},
    {"id": 21, "name": "Personal Memory", "description": "Keep journal of activities, track milestones and achievements", "tech": "• SQLite (local database for entries)\n• JSON (lightweight entry storage)", "x": 250, "y": 1050, "created_at": "2025-09-18T10:20:00"},
    {"id": 22, "name": "Entertainment", "description": "Generate jokes, memes, and entertainment content", "tech": "• Llama 3/GPT-2 (offline humor generation)\n• Pillow (local meme creation)\n• Custom joke databases (local storage)\n• Local entertainment content algorithms", "x": 550, "y": 1050, "created_at": "2025-09-18T10:21:00"},

    # Sub-components for Voice Interaction
    {"id": 23, "name": "Capture Voice", "description": "Real-time audio capture and preprocessing", "tech": "• PyAudio/sounddevice (microphone input)\n• Wave format (local audio storage)\n• NumPy (audio processing)\n• Noise reduction algorithms\n• Audio normalization", "x": 50, "y": 200, "created_at": "2025-09-18T10:22:00"},
    {"id": 24, "name": "Process Command", "description": "Offline speech-to-text processing with Whisper", "tech": "• OpenAI Whisper (offline model)\n• PyTorch (local inference)\n• Hugging Face Transformers (offline)\n• Custom audio preprocessing\n• Local model optimization", "x": 100, "y": 200, "created_at": "2025-09-18T10:23:00"},
    {"id": 25, "name": "Text to Speech", "description": "Offline voice synthesis and speech generation", "tech": "• pyttsx3 (offline TTS engine)\n• espeak-ng (Linux offline TTS)\n• Voice customization\n• Emotion-aware speech\n• SSML support (local)", "x": 150, "y": 200, "created_at": "2025-09-18T10:24:00"},

    # Sub-components for Face Recognition
    {"id": 26, "name": "Detect Face", "description": "Advanced facial detection system. Tech: OpenCV with Haar cascades for basic detection, Dlib for enhanced accuracy, MTCNN for multi-face detection. Real-time face tracking and recognition.", "x": 650, "y": 200, "created_at": "2025-09-18T10:25:00"},
    {"id": 27, "name": "Authenticate User", "description": "Secure facial authentication system. Tech: Face Recognition library, DeepFace for advanced recognition, facial embedding comparison, anti-spoofing measures. Verifies user identity through facial biometrics.", "x": 700, "y": 200, "created_at": "2025-09-18T10:26:00"},
    {"id": 28, "name": "Voice Verification", "description": "Optional voice auth", "x": 750, "y": 200, "created_at": "2025-09-18T10:27:00"},
    {"id": 29, "name": "Video Stream", "description": "Facial analysis capture", "x": 800, "y": 200, "created_at": "2025-09-18T10:28:00"},

    # Sub-components for General AI
    {"id": 30, "name": "Text Generation", "description": "Problem solving responses", "x": 300, "y": 300, "created_at": "2025-09-18T10:29:00"},
    {"id": 31, "name": "Human-like Response", "description": "Natural conversation", "x": 400, "y": 300, "created_at": "2025-09-18T10:30:00"},
    {"id": 32, "name": "Recommendations", "description": "Content suggestions", "x": 500, "y": 300, "created_at": "2025-09-18T10:31:00"},
    {"id": 33, "name": "Context Awareness", "description": "Decision making", "x": 350, "y": 320, "created_at": "2025-09-18T10:32:00"},
    {"id": 34, "name": "Humor Generation", "description": "Joke creation", "x": 450, "y": 320, "created_at": "2025-09-18T10:33:00"},

    # Social Media sub-components
    {"id": 35, "name": "Twitter Scraping", "description": "Twitter data extraction and interaction. Tech: Tweepy for Twitter API v2, tweet analysis, hashtag tracking, trend monitoring. Automates posting, replies, and social media engagement.", "x": 0, "y": 400, "created_at": "2025-09-18T10:34:00"},
    {"id": 36, "name": "Instagram API", "description": "Instagram automation and content management. Tech: Instagram-Private-API for advanced access, Instabot for automation, image processing for posts. Handles story posting, DMs, and engagement.", "x": 50, "y": 400, "created_at": "2025-09-18T10:35:00"},
    {"id": 37, "name": "Facebook Graph", "description": "FB API integration", "x": 100, "y": 400, "created_at": "2025-09-18T10:36:00"},
    {"id": 38, "name": "Auto Posting", "description": "Content automation", "x": 25, "y": 420, "created_at": "2025-09-18T10:37:00"},
    {"id": 39, "name": "Trend Analysis", "description": "Topic & hashtag extraction", "x": 75, "y": 420, "created_at": "2025-09-18T10:38:00"},

    # Smart Home sub-components
    {"id": 40, "name": "Lighting Control", "description": "Advanced smart lighting system. Tech: Philips Hue API, MQTT protocols, color temperature control, circadian rhythm optimization. Voice-controlled ambient lighting with mood presets.", "x": 700, "y": 400, "created_at": "2025-09-18T10:39:00"},
    {"id": 41, "name": "Temperature Control", "description": "Intelligent climate management system. Tech: Nest API, smart thermostat integration, weather data correlation, energy optimization algorithms. Maintains optimal comfort while minimizing energy usage.", "x": 750, "y": 400, "created_at": "2025-09-18T10:40:00"},
    {"id": 42, "name": "Security Cameras", "description": "Advanced security camera management. Tech: OpenCV for video processing, RTSP/ONVIF protocols, motion detection, facial recognition integration. Real-time monitoring with intelligent alerts.", "x": 800, "y": 400, "created_at": "2025-09-18T10:41:00"},
    {"id": 43, "name": "Door Locks", "description": "Access control", "x": 725, "y": 420, "created_at": "2025-09-18T10:42:00"},
    {"id": 44, "name": "IoT Integration", "description": "Smart device connectivity", "x": 775, "y": 420, "created_at": "2025-09-18T10:43:00"}
]

DEMO_CONNECTIONS = [
    # Main flow connections
    {"id": 1, "parent_id": 1, "child_id": 2},   # Wake Word → Voice Interaction
    {"id": 2, "parent_id": 1, "child_id": 3},   # Wake Word → Face Recognition
    {"id": 3, "parent_id": 2, "child_id": 4},   # Voice → General AI
    {"id": 4, "parent_id": 3, "child_id": 4},   # Face → General AI
    {"id": 5, "parent_id": 4, "child_id": 5},   # AI → Social Media
    {"id": 6, "parent_id": 4, "child_id": 6},   # AI → Smart Home
    {"id": 7, "parent_id": 4, "child_id": 7},   # AI → Task Automation
    {"id": 8, "parent_id": 4, "child_id": 8},   # AI → Web Scraping
    {"id": 9, "parent_id": 4, "child_id": 10},  # AI → Personalization
    {"id": 10, "parent_id": 9, "child_id": 11}, # Security → Communication
    {"id": 11, "parent_id": 11, "child_id": 12}, # Communication → Storage
    {"id": 12, "parent_id": 10, "child_id": 13}, # Personalization → Health
    {"id": 13, "parent_id": 11, "child_id": 14}, # Communication → System Monitor
    {"id": 14, "parent_id": 12, "child_id": 15}, # Storage → Analytics
    {"id": 15, "parent_id": 4, "child_id": 16},  # AI → Offline
    {"id": 16, "parent_id": 4, "child_id": 17},  # AI → Emotional Intelligence
    {"id": 17, "parent_id": 17, "child_id": 18}, # Emotional → Creativity
    {"id": 18, "parent_id": 17, "child_id": 19}, # Emotional → Social Interaction
    {"id": 19, "parent_id": 10, "child_id": 20}, # Personalization → Life Management
    {"id": 20, "parent_id": 20, "child_id": 21}, # Life Management → Memory
    {"id": 21, "parent_id": 19, "child_id": 22}, # Social Interaction → Entertainment

    # Voice Interaction sub-components
    {"id": 22, "parent_id": 2, "child_id": 23},  # Voice → Capture Voice
    {"id": 23, "parent_id": 23, "child_id": 24}, # Capture → Process
    {"id": 24, "parent_id": 24, "child_id": 25}, # Process → TTS

    # Face Recognition sub-components
    {"id": 25, "parent_id": 3, "child_id": 26},  # Face Recognition → Detect Face
    {"id": 26, "parent_id": 26, "child_id": 27}, # Detect → Authenticate
    {"id": 27, "parent_id": 27, "child_id": 28}, # Authenticate → Voice Verify
    {"id": 28, "parent_id": 3, "child_id": 29},  # Face Recognition → Video Stream

    # General AI sub-components
    {"id": 29, "parent_id": 4, "child_id": 30},  # AI → Text Generation
    {"id": 30, "parent_id": 4, "child_id": 31},  # AI → Human Response
    {"id": 31, "parent_id": 4, "child_id": 32},  # AI → Recommendations
    {"id": 32, "parent_id": 4, "child_id": 33},  # AI → Context Awareness
    {"id": 33, "parent_id": 4, "child_id": 34},  # AI → Humor

    # Social Media sub-components
    {"id": 34, "parent_id": 5, "child_id": 35},  # Social → Twitter
    {"id": 35, "parent_id": 5, "child_id": 36},  # Social → Instagram
    {"id": 36, "parent_id": 5, "child_id": 37},  # Social → Facebook
    {"id": 37, "parent_id": 5, "child_id": 38},  # Social → Auto Posting
    {"id": 38, "parent_id": 5, "child_id": 39},  # Social → Trend Analysis

    # Smart Home sub-components
    {"id": 39, "parent_id": 6, "child_id": 40},  # Smart Home → Lighting
    {"id": 40, "parent_id": 6, "child_id": 41},  # Smart Home → Temperature
    {"id": 41, "parent_id": 6, "child_id": 42},  # Smart Home → Security
    {"id": 42, "parent_id": 6, "child_id": 43},  # Smart Home → Locks
    {"id": 43, "parent_id": 6, "child_id": 44},  # Smart Home → IoT

    # Cross-connections for system integration
    {"id": 44, "parent_id": 8, "child_id": 15},  # Web Scraping → Analytics
    {"id": 45, "parent_id": 7, "child_id": 14},  # Task Automation → System Monitor
    {"id": 46, "parent_id": 13, "child_id": 15}, # Health → Analytics
    {"id": 47, "parent_id": 16, "child_id": 4},  # Offline → AI (bidirectional support)
    {"id": 48, "parent_id": 9, "child_id": 12},  # Security → Storage
]

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return [Task(**task) for task in DEMO_TASKS]

@app.get("/connections", response_model=List[Connection])
async def get_connections():
    return [Connection(**connection) for connection in DEMO_CONNECTIONS]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)