# Task 2: System Boundary, Actors and I/O

## Actors

| Actor | Role | Interaction |
|-------|------|-------------|
| Security Operator | Watches live feed and alerts | Views dashboard, acknowledges alerts |
| Admin | Manages the system | Enrols people, sets thresholds, exports reports |
| Automated Trigger System | Scheduler or motion sensor | Starts and stops processing for a session |
| Camera (external) | Source of video | Pushes RTSP stream |

## Inputs

| Input | Format | Details |
|-------|--------|---------|
| Video stream | RTSP / H.264 | 1280x720, 25 FPS |
| Sensor parameters | JSON | Motion sensitivity, schedule |
| Enrolment data | JPEG + metadata | 3-5 photos per person |
| Config file | YAML | Thresholds, camera URLs |

## Outputs

| Output | Format | Details |
|--------|--------|---------|
| Bounding boxes | `(x1, y1, x2, y2, conf)` | Per face, per frame |
| Alert notifications | Email / dashboard popup | Unknown person or camera offline |
| Log entries | DB rows + `.log` file | Timestamp, ID, confidence |
| Attendance report | CSV | Per course, per day |

## Operational constraints

| Constraint | Limit |
|------------|-------|
| Memory footprint | Max 2 GB RAM on edge device |
| Bandwidth | Max 4 Mbps per camera stream |
| Latency (frame to log) | Under 500 ms |
| Storage | 32 GB local, logs rotated weekly |
| Connectivity | Must keep working offline and sync later |
