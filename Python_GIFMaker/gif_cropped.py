import imageio.v2 as imageio
from PIL import Image
import glob

# Set the desired resolution (width, height)
desired_size = (500, 500)  # Change this to your preferred resolution

# Automatically get all PNG images in a folder (sorted)
image_files = sorted(glob.glob("images/*.jpg"))  # Change 'your_folder' to your directory

# Create GIF
with imageio.get_writer("animated_images.gif", mode="I", duration=0.5) as writer:
    for filename in image_files:
        image = Image.open(filename)

        # Resize image to the desired resolution using LANCZOS (Best quality)
        image = image.resize(desired_size, Image.LANCZOS)

        # Convert image to RGB mode to avoid transparency issues
        image = image.convert("RGB")

        # Save temporarily and read again
        temp_filename = "temp_resized.png"
        image.save(temp_filename)

        # Add to GIF
        writer.append_data(imageio.imread(temp_filename))

print("GIF created successfully with resized images!")
