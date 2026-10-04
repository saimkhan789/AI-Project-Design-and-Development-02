# Task 1: Requirements for the Smart Attendance System

The idea: a camera at the classroom door recognises students and marks them present automatically.

## Functional requirements

| ID | Requirement | Acceptance criteria |
|----|-------------|---------------------|
| FR-1 | Detect faces in live video | Detection takes under 100 ms per frame |
| FR-2 | Match each face against enrolled students | Match is accepted only at confidence >= 0.85 |
| FR-3 | Log attendance (student ID, timestamp, course) | One entry per student per class session, no duplicates |
| FR-4 | Sync local records to the central database | Sync runs every 5 minutes, retries if the network is down |
| FR-5 | Let an admin enrol, edit or remove students | Changes take effect without restarting the system |

## Non-functional requirements

| ID | Category | Requirement |
|----|----------|-------------|
| NFR-1 | Performance | Process at least 15 FPS on the edge device |
| NFR-2 | Accuracy | Recognition accuracy >= 95%, false accept rate <= 1% |
| NFR-3 | Power | Edge device (Jetson-class) stays under 15 W |
| NFR-4 | Privacy | Face embeddings are stored encrypted, raw frames are never saved |
| NFR-5 | Reliability | 99% uptime during class hours, auto-restart after a crash |
