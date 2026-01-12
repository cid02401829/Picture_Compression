from back_code import compress_image
# filepath: /Users/rayschan/Downloads/Picture_Compression/compress_image.py
# Example usage
if __name__ == "__main__":
    input_image = ""  # Replace with your image path
    output_image = "compressed_" + input_image
    target_mb = 1  # Desired size in MB
    ########  REMEMBER TO SAVE AFTER CHANGING BEFORE RUNNING FILE  ########
    compress_image(input_image, output_image, target_mb)