import subprocess

readme_content = """
# 2D Perlin Noise Metal Surface

A mesmerizing installation that showcases the beauty of Perlin noise, a pioneering algorithm that generates natural-looking patterns and textures.

## Description
This project presents a dynamic, ever-changing tapestry of pixels that evoke the infinite variability of the natural world. Developed by Ken Perlin in the 1980s, this technique has been used to create realistic environments and special effects in film and video games. Here, we present it as a work of art in its own right.

## Features
* Infinite pattern generation with each iteration producing a unique, intricate pattern
* Downloadable CSS file containing the seed of the installation, allowing users to unleash the variance on their own device
* Hypnotic rhythms that blur the boundaries between art and science
* Optimized for desktop devices, with a mobile-friendly notification for best experience

## How it Works
The installation uses a combination of JavaScript and CSS to generate the Perlin noise pattern. The gmNoise function creates a canvas element and generates the noise pattern using a random number generator. The scrmPrms function scrambles the prime numbers used in the noise generation, creating a unique pattern each time.

## Download and Unleash the Variance
Click the "[DOWNLOAD CSS INC. MIME IMG DATA]" link to download the CSS file containing the seed of the installation. Witness the infinite possibilities unfold before your eyes as the algorithm generates new patterns and textures in real-time.

## Experience the Emergence
Step into the world of Perlin noise and discover the beauty that lies at the intersection of chaos and order. Let the hypnotic rhythms of this installation wash over you and explore the infinite variability of the natural world.
"""

with open("README.md", "w") as f:
    f.write(readme_content)

# Alternatively, using subprocess
subprocess.run(["echo", readme_content], stdout=open("README.md", "w"))
