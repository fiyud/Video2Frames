import cv2
import os

def video_to_images(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    frame_count = 0
    sec_count = 0
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        
        if frame_count % fps == 0:
            sec_count += 1
            image_path = os.path.join(output_folder, f"frame_{sec_count}.png")
            cv2.imwrite(image_path, frame)
        
        frame_count += 1
    
    video.release()
    print(f"Frames saved to {output_folder}")

video_to_images("video_path", "./Output_frames")