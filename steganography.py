from PIL import Image

DELIMITER = "#####"

def text_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def hide_message(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = text_to_binary(message + DELIMITER)

    pixels = list(img.getdata())
    new_pixels = []

    index = 0
    for pixel in pixels:
        # Handle RGB and RGBA
        if len(pixel) == 3:
            r, g, b = pixel
            a = None
        elif len(pixel) == 4:
            r, g, b, a = pixel

        # Embed data in LSB of Red channel
        if index < len(binary_message):
            r = (r & ~1) | int(binary_message[index])
            index += 1

        # Reconstruct pixel
        if a is None:
            new_pixels.append((r, g, b))
        else:
            new_pixels.append((r, g, b, a))

    img.putdata(new_pixels)
    img.save(output_path)

    print("Message hidden successfully.")

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ""

    for pixel in pixels:
        # Handle RGB and RGBA
        if len(pixel) == 3:
            r, g, b = pixel
        elif len(pixel) == 4:
            r, g, b, a = pixel

        binary_data += str(r & 1)

    decoded = binary_to_text(binary_data)

    if DELIMITER in decoded:
        return decoded.split(DELIMITER)[0]

    return "No hidden message found"