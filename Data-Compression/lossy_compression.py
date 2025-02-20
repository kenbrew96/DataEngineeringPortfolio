from PIL import Image

def compress_image(input_image, output_image):
    img = Image.open(input_image)
    img.save(output_image, "JPEG", quality=50)

if __name__ == '__main__':
    compress_image('images/input.jpg', 'images/output.jpg')


