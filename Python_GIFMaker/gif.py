import imageio.v2 as imageio
import glob

# Automatically get all PNG images in a folder (sorted)
image_files = sorted(glob.glob("images/*.jpg"))  # Change 'your_folder' to your directory

# Create GIF
with imageio.get_writer("animated_images.gif", mode="I", duration=0.5) as writer:
    for filename in image_files:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF created successfully!")
