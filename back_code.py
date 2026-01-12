from PIL import Image
import os

def compress_image(input_path, output_path, target_size_mb):
    """
    Compress an image to approximately the target file size in MB.
    Saves as JPEG with adjusted quality.
    """
    img = Image.open(input_path)
    
    # Convert to RGB if necessary (for JPEG)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    
    target_size_bytes = target_size_mb * 1024 * 1024
    
    # Start with high quality
    quality = 95
    min_quality = 10  # Minimum quality to avoid too low
    
    while quality >= min_quality:
        img.save(output_path, 'JPEG', quality=quality)
        file_size = os.path.getsize(output_path)
        
        if file_size <= target_size_bytes:
            print(f"Compressed to {file_size / (1024*1024):.2f} MB with quality {quality}")
            break
        quality -= 5  # Decrease quality
    else:
        print(f"Could not compress below {target_size_mb} MB even at quality {min_quality}")
        # Save at minimum quality anyway
        img.save(output_path, 'JPEG', quality=min_quality)