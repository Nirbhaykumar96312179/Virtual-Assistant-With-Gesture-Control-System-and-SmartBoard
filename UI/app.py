import tkinter as tk
from tkinter import ttk
import subprocess
from threading import Thread

# Paths to the scripts
PROTON_PATH = r"C:\\Users\\SikarwarNirbhay\\Desktop\\SSB\\Virtual Mouse  & V Bot\\src\\Proton.py"
MAIN_PATH = r"C:\\Users\\SikarwarNirbhay\\Desktop\\SSB\\Board\\main.py"
PPT_PATH = r"C:\\Users\\SikarwarNirbhay\\Desktop\\SSB\\PPT\\pptmain.py"

# Store the running processes
processes = []

def run_script(script_path):
    def run():
        process = subprocess.Popen(["python", script_path])
        processes.append(process)
    thread = Thread(target=run)
    thread.start()

def stop_scripts():
    for process in processes:
        process.terminate()
    processes.clear()

def show_learn_text():
    learn_text = (
    
        "Gesture Controlled Virtual Mouse\n"
        "Enhancing Human-Computer Interaction with Hand Gestures and Voice Commands\n\n"
        "Introduction\n"
        "The concept of a Gesture Controlled Virtual Mouse revolutionizes human-computer interaction by leveraging hand gestures and voice commands to perform various input and output operations. This approach eliminates the need for physical contact with a computer, providing a seamless and intuitive user experience.\n\n"
        "The project integrates advanced Machine Learning (ML) and Computer Vision algorithms to accurately recognize and interpret hand gestures and voice commands, offering a fluid and responsive interaction without the necessity for additional hardware. The project is compatible with Windows platforms and harnesses the power of modern ML models such as Convolutional Neural Networks (CNN) implemented by MediaPipe, operating on top of pybind11.\n\n"
        "Technological Foundations\n"
        "Machine Learning and Computer Vision\n"
        "At the core of the Gesture Controlled Virtual Mouse are cutting-edge ML and Computer Vision techniques. These technologies enable the system to recognize and interpret human gestures and voice commands accurately.\n\n"
        "MediaPipe and pybind11\n"
        "The project leverages MediaPipe, a framework developed by Google for building perception pipelines. MediaPipe offers pre-trained models for hand detection and tracking, which are crucial for recognizing and interpreting gestures. Additionally, pybind11, a lightweight header-only library, is used to create Python bindings of C++ code, ensuring smooth integration and performance.\n\n"
        "System Modules\n"
        "Direct Hand Module: This module employs MediaPipe Hand detection to recognize gestures made directly with the user's hands. It uses the webcam to capture real-time video, from which hand gestures are detected and interpreted.\n"
        "Glove Module: This module works with gloves of any uniform color, enhancing gesture recognition accuracy by providing a clear distinction between the hand and the background.\n\n"
        "Platform Compatibility\n"
        "The project is designed to operate on Windows platforms, leveraging the system's computational capabilities to run ML models and process real-time video streams.\n\n"
        "Key Features\n"
        "Gesture Recognition:\n"
        "Neutral Gesture\n"
        "Move Cursor\n"
        "Left Click\n"
        "Right Click\n"
        "Double Click\n"
        "Scrolling\n"
        "Drag and Drop\n"
        "Multiple Item Selection\n"
        "Volume Control\n"
        "Brightness Control\n"
        "Voice Assistant (Proton):\n"
        "Launch / Stop Gesture Recognition\n"
        "Google Search\n"
        "Find a Location on Google Maps\n"
        "File Navigation\n"
        "Current Date and Time\n"
        "Copy and Paste\n"
        "Sleep / Wake up Proton\n"
        "Exit\n\n"
        "Implementation Details\n"
        "Hand detection is achieved using MediaPipe's pre-trained models, which accurately identify hand landmarks from the video feed. These landmarks are then used to recognize various gestures through a combination of ML algorithms and heuristic rules.\n\n"
        "The voice assistant, Proton, utilizes speech recognition technology to process and execute voice commands.\n\n"
        "User Experience and Applications\n"
        "The Gesture Controlled Virtual Mouse offers an enhanced user experience by providing an intuitive and contactless method of interaction. Its applications span various domains, including accessibility, presentations, gaming, and general productivity.\n\n"
        "Conclusion\n"
        "The Gesture Controlled Virtual Mouse represents a significant advancement in human-computer interaction. By combining state-of-the-art ML and Computer Vision technologies with practical applications, it provides a seamless, intuitive, and efficient way to interact with computers."
    )

    learn_window = tk.Toplevel(root)
    learn_window.title("Learn")
    learn_window.geometry("600x400")
    learn_window.configure(bg="#2c3e50")

    text_frame = tk.Frame(learn_window, bg="#2c3e50")
    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    text_widget = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 10), bg="#2c3e50", fg="#ecf0f1")
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget.config(yscrollcommand=scrollbar.set)
    text_widget.insert(tk.END, learn_text)
    text_widget.config(state=tk.DISABLED)

def show_contact_info():
    contact_info = (
        "Contributor1: Ritik Patel\n"
        "Phone: 9113425958\n"
        "Email: ritik3286@gmail.com\n\n"
        "Contributor2: Divyanshu Sharma\n"
        "Phone: 8808244430\n"
        "Email: divya@gmail.com\n\n"
        "Contributor3: Nirbhay Kumar\n"
        "Phone: 9631217965\n"
        "Email: nirbhaykumar4021@gmail.com\n"
    )

    contact_window = tk.Toplevel(root)
    contact_window.title("Contact")
    contact_window.geometry("400x300")
    contact_window.configure(bg="#2c3e50")

    text_frame = tk.Frame(contact_window, bg="#2c3e50")
    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    text_widget = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 10), bg="#2c3e50", fg="#ecf0f1")
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget.config(yscrollcommand=scrollbar.set)
    text_widget.insert(tk.END, contact_info)
    text_widget.config(state=tk.DISABLED)


def main():
    global root
    root = tk.Tk()
    root.title("Rangers WelComes you on Revolutionary Platform")
    root.geometry("600x400")
    root.configure(bg="#2c3e50")

    main_frame = ttk.Frame(root, padding=(20, 20), style="Main.TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)

    label = ttk.Label(main_frame,text="Revolutionizing interaction:--", font=("Arial", 16, "bold"), background="#2c3e50", foreground="#ecf0f1")
    label.grid(row=0, column=1, columnspan=3, pady=(0, 20), sticky="ew")

    # Create and place the main buttons in the center
    create_round_button(main_frame, "SmartBoard", lambda: run_script(MAIN_PATH)).grid(row=1, column=1, padx=20, pady=10, sticky="ew")
    create_round_button(main_frame, "PPT", lambda: run_script(PPT_PATH)).grid(row=1, column=2, padx=20, pady=10, sticky="ew")
    create_round_button(main_frame, "Virtual Assist", lambda: run_script(PROTON_PATH)).grid(row=1, column=3, padx=20, pady=10, sticky="ew")

    # Descriptive label
    description_label = ttk.Label(main_frame, text="Control your digital world with gestures, voice, and seamless technology :---", 
                                  font=("Arial", 12), background="#2c3e50", foreground="#ecf0f1", justify=tk.CENTER)
    description_label.grid(row=2, column=1, columnspan=3, pady=(20, 0), sticky="ew")

    # Create and place the stop button
    create_rectangular_button(root, "Stop All", stop_scripts).place(relx=0.5, rely=1, anchor='s', y=-20)
    
    # Create and place the learn button in the corner
    create_rectangular_button(root, "Learn", show_learn_text).place(relx=0, rely=1, anchor='sw', x=20, y=-20)

    # Create and place the contact button in the corner
    create_rectangular_button(root, "Contact Us", show_contact_info).place(relx=1, rely=1, anchor='se', x=-20, y=-20)

    # Center align all columns
    for col in range(5):
        main_frame.grid_columnconfigure(col, weight=1)

    style = ttk.Style()
    style.configure("Main.TFrame", background="#2c3e50")

    root.mainloop()

def create_round_button(master, text, command):
    button_frame = tk.Frame(master, background="#2c3e50")
    canvas = tk.Canvas(button_frame, width=120, height=120, background="#2c3e50", highlightthickness=0)
    canvas.pack(pady=10)

    canvas.create_oval(10, 10, 110, 110, fill="#e74c3c", outline="#e74c3c")
    canvas.create_text(60, 60, text=text, font=("Arial", 12, "bold"), fill="white")

    canvas.bind("<Button-1>", lambda event: command())
    return button_frame

def create_rectangular_button(master, text, command):
    button = tk.Button(master, text=text, command=command, font=("Arial", 12, "bold"), bg="#3498db", fg="white", padx=10, pady=5)
    return button

if __name__ == "__main__":
    main()

