from tracker_engine import ObjectTracker

tracker = ObjectTracker()

for frame in tracker.process_video(
    source=0,
    output_path="output.mp4"
):
    pass

print("Saved output.mp4")