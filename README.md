# Task Graph - DAG Visualization Tool

A modern, single-page web application built with FastAPI that displays tasks as nodes in an infinite canvas with draggable connections, creating a visual DAG (Directed Acyclic Graph) similar to Creately.com's flow chart tools.

## Features

- 🌐 **Infinite Canvas**: Unlimited space for organizing tasks with pan and zoom
- 🎨 **Modern Dark Theme**: Sleek interface with gradient backgrounds and glass morphism
- 🔗 **Visual Connections**: Draggable task nodes with curved connection lines
- 📱 **Mobile Friendly**: Touch-responsive design that works on all devices
- ⚡ **Real-time Updates**: Dynamic task management without page reloads
- 💾 **SQLite Storage**: Lightweight database for persistent task and connection storage
- 🔄 **CRUD Operations**: Create, read, update, and delete tasks and connections
- 🎯 **DAG Structure**: Tasks connected as parent-child relationships

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite
- **Styling**: Modern CSS with gradients, animations, and responsive design

## Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

## Usage

### Creating Tasks
1. Click the "➕ Add Task" button or press Ctrl+N
2. Fill in the task details:
   - **Task Name**: Required field for the task title
   - **Description**: Optional detailed description
3. Tasks appear as draggable nodes on the infinite canvas

### Connecting Tasks
1. Click the "🔗 Connect" button to enter connection mode
2. Click on a parent task (source node)
3. Click on a child task (target node) to create a connection
4. Press Escape to exit connection mode

### Managing Tasks
- **Drag**: Click and drag any task node to reposition it
- **Edit**: Click the edit (✏️) button on any task
- **Delete**: Click the delete (🗑️) button with confirmation
- **Connections**: Click on any connection line to delete it

### Canvas Navigation
- **Pan**: Click and drag on empty canvas space
- **Zoom**: Use mouse wheel or zoom controls (+ - ⌂)
- **Center**: Click "🎯 Center" to focus on all tasks
- **Auto Layout**: Click "🔄 Auto Layout" for automatic positioning

## API Endpoints

The application provides a REST API for task management:

- `GET /` - Serve the main HTML page
- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{task_id}` - Update an existing task
- `DELETE /tasks/{task_id}` - Delete a task
- `GET /connections` - Get all task connections
- `POST /connections` - Create a new connection
- `DELETE /connections/{connection_id}` - Delete a connection

## Data Structures

### Task Object
```json
{
  "id": 1,
  "name": "Complete Frontend Design",
  "description": "Design the UI for the task graph page",
  "x": 150.5,
  "y": 200.0,
  "created_at": "2025-09-18T10:30:00"
}
```

### Connection Object
```json
{
  "id": 1,
  "parent_id": 1,
  "child_id": 2
}
```

## Project Structure

```
task-graph/
│
├── main.py              # FastAPI backend with SQLite integration
├── index.html           # Single-page frontend application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── tasks.db            # SQLite database (created automatically)
```

## Customization

### Styling
The CSS in `index.html` can be easily customized:
- Colors: Modify the rgba color values and gradients
- Node appearance: Adjust task-node styles for different visual effects
- Connections: Customize connection-line stroke properties
- Animations: Modify transition durations and keyframe animations

### Graph Layout
- **Force-directed layout**: The auto-layout uses a simple physics simulation
- **Manual positioning**: All nodes can be dragged and positioned manually
- **Zoom levels**: Supports zoom from 0.1x to 3x with smooth transitions

### Database
The SQLite database is created automatically with two tables:
- `tasks`: Stores task information with x,y coordinates
- `connections`: Stores parent-child relationships between tasks

To reset: Stop the server, delete `tasks.db`, restart the server

## Development

For development with auto-reload:
```bash
uvicorn main:app --reload
```

The application will automatically restart when you make changes to the Python code.

## Browser Support

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## License

This project is open source and available under the MIT License.