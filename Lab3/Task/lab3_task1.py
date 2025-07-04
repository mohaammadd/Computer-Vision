import numpy as np
import cv2

# Create a VideoCapture object for the original video
cap = cv2.VideoCapture('eggs.avi')

# Get the frame dimensions
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height
fps = int(cap.get(cv2.CAP_PROP_FPS))        # frames per second

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('eggs-reverse.avi', fourcc, fps, (w, h))

# Buffer to store frames
frame_buffer = []

# Read all frames and store them in the buffer
while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video
    
    frame_buffer.append(frame)  # Store frame

cap.release()  # Release the video file

# Write frames in reverse order
for frame in reversed(frame_buffer):
    out.write(frame)

out.release()  # Save the new reversed video

# Open both videos for display
cap_original = cv2.VideoCapture('eggs.avi')
cap_reversed = cv2.VideoCapture('eggs-reverse.avi')

while True:
    # Read frames from both videos
    ret1, frame1 = cap_original.read()
    ret2, frame2 = cap_reversed.read()

    # If one video ends, break the loop
    if not ret1 or not ret2:
        break

    # Show both videos side by side
    cv2.imshow('Original Video', frame1)
    cv2.imshow('Reversed Video', frame2)

    # Exit when 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release video captures and close windows