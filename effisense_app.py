import customtkinter as ctk
import threading
import time
import math
from pynput import mouse, keyboard


class ActivityTracker:
    def __init__(self):
        self.is_tracking = False
        self.mouse_listener = None
        self.keyboard_listener = None
        

        self.prev_x = None
        self.prev_y = None
        self.prev_time = None
        self.prev_velocity = None


    def on_move(self, x, y):
        if not self.is_tracking:
            return

        current_time = time.time()
        
        
        if self.prev_time is not None:
            dt = current_time - self.prev_time
            
            
            if dt > 0:
                # 1. Distance
                dx = x - self.prev_x
                dy = y - self.prev_y
                distance = math.sqrt(dx**2 + dy**2)
                
                
                velocity = distance / dt
                
                
                acceleration = 0.0
                if self.prev_velocity is not None:
                    acceleration = (velocity - self.prev_velocity) / dt
                
                
                if distance > 1.0:
                    print(f"MOUSE  | Vel: {velocity:.2f} px/s | Accel: {acceleration:.2f} px/s²")
                
                self.prev_velocity = velocity

        
        self.prev_x = x
        self.prev_y = y
        self.prev_time = current_time

    
    def on_press(self, key):
        if not self.is_tracking:
            return
        
        current_time = time.time()
        print(f"KEYBOARD | Keystroke registered at {current_time:.4f}")

    
    def start_tracking(self):
        self.is_tracking = True
        
        
        self.prev_x, self.prev_y, self.prev_time, self.prev_velocity = None, None, None, None
        
        
        self.mouse_listener = mouse.Listener(on_move=self.on_move)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()
        print("--- Tracking Started ---")

    def stop_tracking(self):
        self.is_tracking = False
        
        
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            
        print("--- Tracking Stopped ---")


class EffiSenseApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("EffiSense - Productivity Monitor")
        self.geometry("400x250")
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("green") 

        # 
        self.tracker = ActivityTracker()

        # UI Elements
        self.label = ctk.CTkLabel(self, text="EffiSense is Inactive", font=("Arial", 18, "bold"))
        self.label.pack(pady=40)

        self.toggle_btn = ctk.CTkButton(self, text="Start Monitoring", command=self.toggle_monitoring)
        self.toggle_btn.pack(pady=10)

    def toggle_monitoring(self):
        if not self.tracker.is_tracking:
            self.tracker.start_tracking()
            self.label.configure(text="EffiSense is Active (Tracking)", text_color="green")
            self.toggle_btn.configure(text="Stop Monitoring", fg_color="red", hover_color="darkred")
        else:
            self.tracker.stop_tracking()
            self.label.configure(text="EffiSense is Inactive", text_color="white")
            self.toggle_btn.configure(text="Start Monitoring", fg_color=["#3B8ED0", "#1F6AA5"], hover_color=["#36719F", "#144870"])

# --- 3. RUN THE APP ---
if __name__ == "__main__":
    app = EffiSenseApp()
    app.mainloop()