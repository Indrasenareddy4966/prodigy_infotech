from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key=42):
    # Load the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Apply a simple encryption operation
    # Example: Add a key to each pixel value
    encrypted_array = (image_array + key) % 256

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key=42):
    # Load the encrypted image
    encrypted_image = Image.open(image_path)
    encrypted_array = np.array(encrypted_image)

    # Apply the inverse of the encryption operation
    # Example: Subtract the key from each pixel value
    decrypted_array = (encrypted_array - key) % 256

    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
original_image_path = 'original_image.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
key = 42

encrypt_image(original_image_path, encrypted_image_path, key)
decrypt_image(encrypted_image_path, decrypted_image_path, key)
