import os
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", default="badapple.mp4",
   help="Input Video Path")
ap.add_argument("-o", "--output", default="server/frames/",
   help="Output Folder path for serving")
ap.add_argument("-y", "--height", default=42,
   help="Resize frames with aspect ratio maintained")
ap.add_argument("-b", "--br", default=False,
   help="For HTML rendering, adding <br> tags")
args = vars(ap.parse_args())

def resize_frame(image, newHeight = 42):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aspectRatio = img.shape[1] / img.shape[0]
    newWidth = int(aspectRatio * newHeight)
    img = cv2.resize(img, (newWidth, newHeight))
    return img

def mapToAscii(image):
    newLine = '\n' if args['br'] == False else '<br>'
    ascii_array = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    newAsciiImageString = ''
    for x, row in enumerate(image):
        for i, element in enumerate(row):
            char_idx = 0 if element < 127 else 10
            newAsciiImageString = newAsciiImageString + ascii_array[char_idx] + ' '
        newAsciiImageString += newLine
    return newAsciiImageString

def writeToFile(data, folder, filename):
    txtFile = open(os.path.join(folder, filename), "w")
    txtFile.write(data)
    txtFile.close()

def process_video(videoPath):
    asciiStrings = []
    cap = cv2.VideoCapture(videoPath)
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if (ret == False):
            break
        if (i % 100 == 0):
            print("Processing frame "+ str(i))
        if (i % 2 == 0):
            resized_image = resize_frame(frame, int(args['height']))
            asciiImage = mapToAscii(resized_image)
            asciiStrings.append(asciiImage)
        i = i + 1
    cap.release()
    return asciiStrings

# I have separated video processing and file write, not efficient? but in case, I might reuse these functions separately
outputArrayOfStrings = process_video(args['input'])
print("Writing frames to files...")
for i, data in enumerate(outputArrayOfStrings):
    writeToFile(data, args['output'], "frame{0}.txt".format(i))
print("Success")
