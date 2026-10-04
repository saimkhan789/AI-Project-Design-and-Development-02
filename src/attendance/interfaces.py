"""Interface skeletons for the attendance pipeline (Lab 02, Task 4)."""
from dataclasses import dataclass
from typing import Iterator, List, Optional, Tuple
import numpy as np


@dataclass
class Detection:
    box: Tuple[int, int, int, int]  # x1, y1, x2, y2
    confidence: float
    label: str = "face"
    identity: Optional[str] = None


class DataIngestion:
    """Reads frames from an RTSP stream or video file."""

    def __init__(self, source: str, fps_limit: int = 15) -> None:
        self.source = source
        self.fps_limit = fps_limit

    def connect(self) -> bool:
        """Open the source. Returns True on success."""
        raise NotImplementedError

    def frames(self) -> Iterator[np.ndarray]:
        """Yield BGR frames (H, W, 3) uint8."""
        raise NotImplementedError

    def release(self) -> None:
        raise NotImplementedError


class ImagePreprocessor:
    """Resizes and normalises frames for the model."""

    def __init__(self, size: Tuple[int, int] = (640, 640)) -> None:
        self.size = size

    def process(self, frame: np.ndarray) -> np.ndarray:
        """Return float32 array (H, W, 3) scaled to 0-1."""
        raise NotImplementedError


class ModelInferenceEngine:
    """Loads the detector and runs it on frames."""

    def __init__(self, weights_path: str, conf_threshold: float = 0.5) -> None:
        self.weights_path = weights_path
        self.conf_threshold = conf_threshold

    def load_model(self) -> None:
        raise NotImplementedError

    def predict(self, frame: np.ndarray) -> List[Detection]:
        """Run inference, return detections above the threshold."""
        raise NotImplementedError


class AlertLogger:
    """Writes attendance logs and raises alerts."""

    def __init__(self, db_path: str, log_file: str = "logs/attendance.log") -> None:
        self.db_path = db_path
        self.log_file = log_file

    def log_attendance(self, student_id: str, confidence: float) -> bool:
        """Store a record. Returns False if already logged this session."""
        raise NotImplementedError

    def send_alert(self, message: str, level: str = "WARNING") -> None:
        raise NotImplementedError
