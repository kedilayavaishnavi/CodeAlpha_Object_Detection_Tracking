from ultralytics import YOLO
import cv2

class ObjectTracker:
    def __init__(self, model_path="yolov8n.pt"):
        # yolov8n = nano, fastest, good for CPU/Apple Silicon live demo
        self.model = YOLO(model_path)

    def process_video(self, source=0, output_path="output.mp4", conf=0.4):
        results_gen = self.model.track(
            source=source,
            conf=conf,
            persist=True,
            tracker="bytetrack.yaml",
            stream=True
        )

        writer = None

        for result in results_gen:
            frame = result.plot()

            if writer is None:
                h, w = frame.shape[:2]
                writer = cv2.VideoWriter(
                    output_path,
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    20,
                    (w, h)
                )

            writer.write(frame)

            yield frame

        if writer:
            writer.release()