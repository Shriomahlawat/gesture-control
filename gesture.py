
import cv2
import time
import pyautogui
from mediapipe import Image, ImageFormat
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load model
base_options = python.BaseOptions(
    model_asset_path=r"C:\Users\satya\Desktop\hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
print("Camera started. Press Q to quit.")

last_action_time = 0
ACTION_DELAY = 0.3  # seconds
last_gesture = "CENTER"


while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame not read")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = Image(
        image_format=ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:

            h, w, _ = frame.shape

            # 🟢 GREEN DOTS 
            for lm in hand_landmarks:
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)

            # 🔴 INDEX FINGER TIP (landmark 8)
            index_tip = hand_landmarks[8]
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            cv2.circle(frame, (ix, iy), 10, (0, 0, 255), -1)

            # 🧠 LEFT / RIGHT / JUMP / ROLL LOGIC
            center_x = w // 2
            center_y = h // 2

            gesture = "CENTER"

            # LEFT / RIGHT (X-axis)
            if ix < center_x - 50:
                gesture = "LEFT"
            elif ix > center_x + 50:
                gesture = "RIGHT"

            # JUMP / ROLL (Y-axis)
            if iy < center_y - 50:
                gesture = "JUMP"
            elif iy > center_y + 90:
                gesture = "ROLL"

            cv2.putText(
                frame,
                gesture,
                (50, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 255, 255),
                3
            )

            # 🎮 KEYBOARD CONTROL (ADDED ONLY THIS PART)
            current_time = time.time()
            # key sirf tab fire ho jab gesture CHANGE ho
            if gesture != last_gesture and current_time - last_action_time > ACTION_DELAY:

                print("KEY:", gesture)  # debug

                if gesture == "LEFT":
                    pyautogui.press("left")

                elif gesture == "RIGHT":
                    pyautogui.press("right")

                elif gesture == "JUMP":
                    pyautogui.press("up")

                elif gesture == "ROLL":
                    pyautogui.press("down")

                last_action_time = current_time
                last_gesture = gesture


    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break

cap.release()
cv2.destroyAllWindows()
