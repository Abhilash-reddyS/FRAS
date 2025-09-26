# main.py - Entry point for Facial Recognition Attendance System

from student_registration import StudentRegistration
from attendance_system import AttendanceSystem
from report_generator import ReportGenerator

def main_menu():
    """Main menu function to navigate the system"""
    print("\n===== Facial Recognition Attendance System =====")
    print("1. Register New Student")
    print("2. Start Attendance System")
    print("3. Generate Attendance Report")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    return choice

if __name__ == "__main__":
    # Initialize system components
    registration = StudentRegistration()
    attendance = AttendanceSystem()
    reports = ReportGenerator()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            registration.register_student(spacebar_capture=True, max_images=10)
        elif choice == '2':
            attendance.run_attendance_system()
        elif choice == '3':
            reports.generate_attendance_report()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")