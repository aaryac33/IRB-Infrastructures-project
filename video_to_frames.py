import os
import subprocess

def extract_frames(input_folder, output_folder, frame_interval):
    # Get a list of all video files in the input folder
    video_files = [file for file in os.listdir(input_folder) if file.lower().endswith((".mp4", ".avi", ".mkv", ".mov"))]

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each video file and extract frames using ffmpeg
    for video_file in video_files:
        input_file_path = os.path.join(input_folder, video_file)
        output_file_pattern = os.path.join(output_folder, f"{os.path.splitext(video_file)[0]}_%d.png")

        command = f"ffmpeg -i \"{input_file_path}\" -vf fps={1/frame_interval} \"{output_file_pattern}\""
        subprocess.run(command, shell=True)

def get_frame_interval():
    while True:
        try:
            frame_interval = int(input("Enter the frame interval (e.g., 1 for every frame, 2 for every 2nd frame): "))
            if frame_interval > 0:
                return frame_interval
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    input_folder = r"path o the folder having videos"  # Replace with the path to your input folder
    output_folder = r"path of the folder where you want to save the images"  # Replace with the path to your output folder

    # Get the frame interval from the user
    frame_interval = get_frame_interval()

    extract_frames(input_folder, output_folder, frame_interval)
