# importing required libraries
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cvzone
import cv2
import os
from cvzone.PoseModule import PoseDetector

# some required ratios
fixedRatio = 262 / 190  
RatioHeightWidth = 581 / 440
detector = PoseDetector()

# Define the overlay function to apply the selected item to the image
def overlay_item(filename, item):
    if item == 'Shirt':

        cap = cv2.VideoCapture(0)
        #resizing the video
        cap.set(3, 1280)
        cap.set(4, 720)
        while True:
            success, img = cap.read()
            img = detector.findPose(img)
            # img = cv2.flip(img,1)
            lmList, bboxInfo = detector.findPosition(img ,bboxWithHands=False, draw=False)
            if lmList:
                # center = bboxInfo["center"]
                lm11 = lmList[11][1:3]
                lm12 = lmList[12][1:3]
                imgShirt = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
 
                widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
                #print(widthOfShirt)
                imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * RatioHeightWidth)))
                currentScale = (lm11[0] - lm12[0]) / 190
                offset = int(44 * currentScale), int(48 * currentScale)
 
                try:
                    img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
                except:
                    pass

 
            cv2.imshow("Image", img)
            cv2.waitKey(1)


    elif item == 'Lower':
        cap = cv2.VideoCapture(0)
        #resizing the video
        cap.set(3, 1280)
        cap.set(4, 720)
        while True:
            success, img = cap.read()
            img = detector.findPose(img)
            # img = cv2.flip(img,1)
            lmList, bboxInfo = detector.findPosition(img ,bboxWithHands=False, draw=False)
            if lmList:
                # center = bboxInfo["center"]
                lm23 = lmList[23][1:3]
                lm24 = lmList[24][1:3]
                imglower = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                imglower = cv2.resize(imglower, (460, 335))
                widthOflower = int((lm23[0] - lm24[0]) * fixedRatio)
                #print(widthOfShirt)
                #imglower = cv2.resize(imglower, (widthOflower, int(widthOflower * RatioHeightWidth)))
                currentScale = (lm23[0] - lm24[0]) / 18
                offset = int(42 * currentScale), int(5 * currentScale)
 
                try:
                    img = cvzone.overlayPNG(img, imglower, (lm24[0] - offset[0], lm23[1] - offset[1]))
                except:
                    pass

 
            cv2.imshow("Image", img)
            cv2.waitKey(1)

        
    elif item == 'Sunglasses':
  
        cap = cv2.VideoCapture(0)
        #resizing the video
        cap.set(3, 1280)
        cap.set(4, 720)
        while True:
            success, img = cap.read()
            img = detector.findPose(img)
            # img = cv2.flip(img,1)
            lmList, bboxInfo = detector.findPosition(img ,bboxWithHands=False, draw=False)
            if lmList:
                # center = bboxInfo["center"]
                lm3 = lmList[3][1:3]
                lm6 = lmList[6][1:3]
                imgglass = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
 
                widthOfglass = int((lm3[0] - lm6[0]) * fixedRatio)
                #print(widthOfShirt)
                imgglass = cv2.resize(imgglass, (widthOfglass+20, int(widthOfglass * RatioHeightWidth)))
                currentScale = (lm3[0] - lm6[0]) / 185
                offset = int(30 * currentScale), int(180 * currentScale)
 
                try:
                    img = cvzone.overlayPNG(img, imgglass, (lm6[0] - offset[0], lm3[1] - offset[1]))
                except:
                    pass

 
            cv2.imshow("Image", img)
            cv2.waitKey(1)

    else:
        pass

# Define the function to browse for the image file
def browse_image():
    item = item_choice.get()
    filename = filedialog.askopenfilename(initialdir='/', title='Select Image', filetypes=(('Image Files', '*.png'),))
    overlay_item(filename, item)


# Create the main GUI window
root = tk.Tk()
root.title('Virtual Try-On')
root.geometry("500x600")
root.resizable(False, False)

# Add a background color and image
bg_color = '#2c2d2f'
bg_image = Image.open("F:/VS Code/minor 2/background.png")
bg_image = bg_image.resize((500, 600), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the image display label
image_label = tk.Label(root)
image_label.pack(pady=20)

# Add a title label
title_label = tk.Label(root, text="Virtual Try-On", font=("Arial", 24), bg=bg_color, fg="#fff")
title_label.pack(pady=10)

# Create the item choice dropdown menu
item_choice = tk.StringVar(root)
item_choice.set('Select Item') 
item_menu = tk.OptionMenu(root, item_choice, 'Shirt', 'Lower', 'Sunglasses')
item_menu.config(bg=bg_color, fg="#fff", activebackground=bg_color, activeforeground="#fff", font=("Arial", 16))
item_menu.pack(pady=10)

# Create the image browse button
browse_button = tk.Button(root, text='Browse & Overlay', command=browse_image, bg="#fff", fg=bg_color, font=("Arial", 16))
browse_button.pack(pady=10)

# Run the GUI
root.mainloop()
