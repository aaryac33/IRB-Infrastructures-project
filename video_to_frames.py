import cv2

def extract_frames(video_path, output_folder, frame_interval=1):
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file.")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        
        # Break the loop when the video ends
        if not ret:
            break
        
        # Save the frame as an image file
        if frame_count % frame_interval == 0:
            output_path = f"{output_folder}/frame_{frame_count}.png"
            cv2.imwrite(output_path, frame)
            print(f"Frame {frame_count} saved as {output_path}")
        
        frame_count += 1

    cap.release()

if __name__ == "__main__":
    # Replace 'video.mp4' with the path to your video file
    video_path = "video.mp4"

    # Replace 'frames_folder' with the path to the folder where you want to save the frames
    output_folder = "frames_folder"

    # Set the frame_interval to specify how many frames you want to skip before saving the next frame
    # For example, frame_interval=1 will save every frame, frame_interval=2 will save every other frame, and so on.
    frame_interval = 1

    extract_frames(video_path, output_folder, frame_interval)
