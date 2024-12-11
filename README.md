# Attendance Management System Using Face Recognition

This project implements an Attendance Management System using real-time face recognition. The system uses a webcam to detect and identify students, mark their attendance, and save the logs in a CSV file.

---

## Features
- **Real-time Face Recognition**: Detects faces from a webcam and identifies them using pre-stored face encodings.
- **Attendance Logging**: Marks attendance with a timestamp and saves it to a CSV file.
- **Graphical User Interface (GUI)**: User-friendly GUI for loading student data and starting the attendance system.
- **CSV Integration**: Supports loading student details from a CSV file and exporting attendance logs.

---

## Prerequisites

### Hardware Requirements
- **Webcam**: For real-time face detection and recognition.
- **Processor**: Dual-core or higher (Quad-core recommended for better performance).
- **Memory**: Minimum 4GB RAM (8GB recommended).
- **Storage**: At least 1GB free space.

### Software Requirements
- **Operating System**: Windows, macOS, or Linux.
- **Python Version**: Python 3.7 or later.
- **Python Libraries**:
  - `opencv-python`
  - `face-recognition`
  - `pandas`
  - `tkinter` (pre-installed with Python)

To install the necessary libraries, run:
```bash
pip install opencv-python face-recognition pandas
```

---

## File Requirements

### Student Data CSV File
The CSV file should contain the following columns:
- `Name`: Name of the student.
- `FaceEncoding`: String representation of the face encoding generated using the `face_recognition` library.

Example:
```csv
Name,FaceEncoding
John Doe,"[0.123, 0.456, 0.789, ...]"
Jane Doe,"[0.321, 0.654, 0.987, ...]"
```

---

## How to Use

1. **Prepare the Environment**:
   - Ensure all dependencies are installed.
   - Create a CSV file (`students.csv`) with student names and face encodings.

2. **Run the Code**:
   - Save the script as `attendance_system.py`.
   - Execute the script:
     ```bash
     python attendance_system.py
     ```

3. **Using the GUI**:
   - Load the student data using the "Load Student Data" button.
   - Start the attendance system by clicking "Start Attendance System".
   - Press 'q' to quit the webcam feed.

4. **View Attendance Logs**:
   - Attendance is saved in `attendance_log.csv`.

---

## Code Workflow

1. **Load Student Data**:
   - Reads the CSV file containing student details and face encodings.

2. **Initialize Webcam**:
   - Captures video frames in real time.

3. **Face Detection and Recognition**:
   - Detects faces in each frame and compares them with stored encodings.

4. **Attendance Marking**:
   - Marks attendance for recognized faces with a timestamp.

5. **Save Attendance Logs**:
   - Writes attendance logs to a CSV file for record-keeping.

---

## Output
- **Real-time Webcam Feed**: Displays detected faces with labels.
- **Attendance Log CSV File**: Contains columns `Name` and `Time`, saved as `attendance_log.csv`.

---

## Troubleshooting

- **Webcam Not Detected**:
  - Ensure the webcam is properly connected and functional.
  - Test the webcam using another application.

- **Face Not Recognized**:
  - Verify that the face encoding in the CSV matches the individual.
  - Improve lighting and camera positioning.

- **Error in CSV File**:
  - Ensure the CSV format matches the requirements (columns `Name` and `FaceEncoding`).

---

## Future Enhancements
- **Database Integration**: Replace CSV files with a database for scalability.
- **Cloud Deployment**: Deploy the system on the cloud for remote access.
- **Mobile App**: Develop a mobile version for enhanced portability.
- **Multi-camera Support**: Enable attendance logging from multiple locations.

---

## License
This project is open-source and free to use under the MIT License.

---

For any queries or assistance, feel free to contact the developer.

