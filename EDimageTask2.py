from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        # Load image
        img = Image.open(input_path)
        img = img.convert("RGB")
        pixels = img.load()

        width, height = img.size

        # Encrypt/Decrypt using XOR with key
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        # Save result
        img.save(output_path)
        print(f"Image saved to {output_path}")

    except Exception as e:
        print("Error:", e)

def main():
    print("=== Image Encrypt/Decrypt Tool ===")
    mode = input("Choose mode - (E)ncrypt or (D)ecrypt: ").strip().upper()

    if mode not in ['E', 'D']:
        print("Invalid choice. Please enter E or D.")
        return

    input_path = input("Enter path to the image file: ").strip()
    if not os.path.exists(input_path):
        print("File does not exist.")
        return

    try:
        key = int(input("Enter numeric key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Must be an integer between 0 and 255.")
        return

    output_path = input("Enter output file name (e.g., output.png): ").strip()
    encrypt_decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
