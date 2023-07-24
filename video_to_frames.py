import cv2
import os

def extract_frames_from_folder(input_folder, output_folder, frame_interval=1):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        extract_frames(video_path, output_folder, frame_interval)

def extract_frames(video_path, output_folder, frame_interval=1):
    cap = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()

        # Break the loop when the video ends
        if not ret:
            break

        # Save the frame as an image file
        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_folder, f"frame_{os.path.splitext(video_path)[0]}_{frame_count}.png")
            cv2.imwrite(output_path, frame)
            print(f"Frame {frame_count} from {video_path} saved as {output_path}")

        frame_count += 1

    cap.release()

if __name__ == "__main__":
    # Replace 'videos_folder' with the path to the folder containing the videos
    input_folder = "videos_folder"

    # Replace 'frames_folder' with the path to the folder where you want to save the extracted frames
    output_folder = "frames_folder"

    # Set the frame_interval to specify how many frames you want to skip before saving the next frame
    # For example, frame_interval=1 will save every frame, frame_interval=2 will save every other frame, and so on.
    frame_interval = 1

    extract_frames_from_folder(input_folder, output_folder, frame_interval)