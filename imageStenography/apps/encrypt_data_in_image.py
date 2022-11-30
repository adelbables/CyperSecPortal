import math

import cv2

from CyperSecPortal.settings import MEDIA_ROOT

image_display_size = 300, 300


def encrypt_data_into_image(path_image, data):
    img = cv2.imread(path_image)

    # data encrypt message
    # break the image into its character level. Represent the characters in ASCII.
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    # algorithm to encode the image
    pix_req = len(data) * 3

    row_req = pix_req / width
    row_req = math.ceil(row_req)

    count = 0
    char_count = 0
    # Step 3
    for i in range(row_req + 1):
        # Step 4
        while count < width and char_count < len(data):
            char = data[char_count]
            char_count += 1
            # Step 5
            for index_k, k in enumerate(char):
                if ((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (
                        k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if index_k % 3 == 2:
                    count += 1
                if index_k == 7:
                    if char_count * 3 < pix_req and img[i][count][2] % 2 == 1:
                        img[i][count][2] -= 1
                    if char_count * 3 >= pix_req and img[i][count][2] % 2 == 0:
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    # Step 6
    # Write the encrypted image into a new file
    cv2.imwrite("%s/images/encrypted/encrypted_image.png" % MEDIA_ROOT, img)
