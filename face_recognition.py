import cv2
import face_recognition
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Load the student details from a CSV file
def load_student_data("C:\Users\jatin\OneDrive\Desktop\face_recognition\StudentDetails.csv")):
    try:
        student_data = pd.read_csv(r"C:\Users\jatin\OneDrive\Desktop\face_recognition\StudentDetails.csv")
        return student_data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load student data: {e}")
        return None

def process_face_encodings(encodings_column):
    return [eval(encoding) for encoding in encodings_column]  # Convert string back to list of floats

def mark_attendance(name):
    if name not in attendance_log:
        now = datetime.now()
        time = now.strftime('%H:%M:%S')
        attendance_log[name] = time

def start_attendance_system():
    global known_face_encodings, known_face_names, attendance_log

    # Initialize attendance log
    attendance_log = {}

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    print("Starting the attendance system. Press 'q' to quit.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to RGB (OpenCV uses BGR)
        rgb_frame = frame[:, :, ::-1]

        # Detect face locations and encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare the detected face with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Find the best match for the detected face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = face_distances.argmin()
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Mark attendance
            mark_attendance(name)

            # Draw a rectangle around the face
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Label the face
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Attendance System', frame)

        # Break on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Save attendance log to CSV
    attendance_df = pd.DataFrame(list(attendance_log.items()), columns=['Name', 'Time'])
    attendance_df.to_csv('attendance_log.csv', index=False)

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

    messagebox.showinfo("Info", "Attendance logged successfully.")

# GUI Components
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        global known_face_encodings, known_face_names
        student_data = load_student_data(r"C:\Users\jatin\OneDrive\Desktop\face_recognition\StudentDetails.csv")
        if student_data is not None:
            known_face_encodings = process_face_encodings(student_data['FaceEncoding'])
            known_face_names = student_data['Name']
            messagebox.showinfo("Success", "Student data loaded successfully.")

# Main Window
root = tk.Tk()
root.title("Attendance Management System")

# GUI Elements
tk.Label(root, text="Attendance Management System", font=("Arial", 16)).pack(pady=10)

load_button = tk.Button(root, text="Load Student Data", command=select_file, font=("Arial", 12))
load_button.pack(pady=10)

start_button = tk.Button(root, text="Start Attendance System", command=start_attendance_system, font=("Arial", 12))
start_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
quit_button.pack(pady=10)

root.mainloop()