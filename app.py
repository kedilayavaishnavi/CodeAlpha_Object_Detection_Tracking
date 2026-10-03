import streamlit as st
import cv2
import tempfile
from tracker_engine import ObjectTracker

st.set_page_config(
    page_title="Object Detection & Tracking",
    page_icon="🎥"
)

st.title("🎥 Real-Time Object Detection & Tracking")

source_type = st.radio(
    "Input source",
    ["Webcam", "Upload video"]
)

conf = st.slider(
    "Confidence threshold",
    0.1,
    0.9,
    0.4
)

tracker = ObjectTracker()

if source_type == "Upload video":

    uploaded = st.file_uploader(
        "Upload a video",
        type=["mp4", "mov", "avi"]
    )

    if uploaded and st.button("Run detection"):

        tfile = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )

        tfile.write(uploaded.read())

        frame_placeholder = st.empty()

        for frame in tracker.process_video(
            source=tfile.name,
            conf=conf
        ):
            frame_rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            frame_placeholder.image(
                frame_rgb,
                channels="RGB"
            )

        st.success("Done — saved to output.mp4")

else:

    run = st.checkbox("Start webcam")

    frame_placeholder = st.empty()

    if run:

        for frame in tracker.process_video(
            source=0,
            conf=conf
        ):
            frame_rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            frame_placeholder.image(
                frame_rgb,
                channels="RGB"
            )

            if not run:
                break