import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageEnhance

# Load the single image
image_path = "images/1.jpg"  # Change to your image path
image = Image.open(image_path)

# Create a list to store frames
frames = []

# Generate animated frames (e.g., zoom effect)
for i in range(10):  # Creates 10 frames
    scale = 1 + (i * 0.05)  # Zoom-in effect
    new_size = (int(image.width * scale), int(image.height * scale))
    
    # Resize with zoom effect
    frame = image.resize(new_size, Image.LANCZOS)
    
    # Crop to original size (to maintain a stable size)
    left = (frame.width - image.width) // 2
    top = (frame.height - image.height) // 2
    frame = frame.crop((left, top, left + image.width, top + image.height))
    
    # Optional: Add brightness variation (flashing effect)
    enhancer = ImageEnhance.Brightness(frame)
    frame = enhancer.enhance(1 + (i * 0.1))  # Increase brightness gradually
    
    frames.append(frame)

# Save as animated GIF
frames[0].save("single_image.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)

print("GIF created successfully!")
