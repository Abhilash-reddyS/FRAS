# report_generator.py - Handles attendance report generation

import os
import pandas as pd
from datetime import datetime
from fpdf import FPDF

class ReportGenerator:
    def __init__(self):
        self.attendance_log = 'attendance_log.csv'
    
    def generate_attendance_report(self):
        """Generate PDF report of attendance"""
        if not os.path.exists(self.attendance_log) or os.path.getsize(self.attendance_log) == 0:
            print("No attendance records found")
            return
            
        # Read attendance data
        df = pd.read_csv(self.attendance_log)
        
        # Get unique dates
        dates = df['Date'].unique()
        
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Attendance Report", ln=True, align='C')
        pdf.ln(10)
        
        for date in dates:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"Date: {date}", ln=True)
            
            # Filter data for this date
            date_df = df[df['Date'] == date]
            
            # Get first attendance entry per student (within 75 min window)
            unique_students = date_df.groupby('Name', as_index=False).agg({'Time': 'first'})
            
            # Create table
            pdf.set_font("Arial", "B", 10)
            pdf.cell(90, 10, "Name", border=1)
            pdf.cell(90, 10, "Time", border=1, ln=True)
            
            pdf.set_font("Arial", "", 10)
            for _, row in unique_students.iterrows():
                pdf.cell(90, 10, row['Name'], border=1)
                pdf.cell(90, 10, row['Time'], border=1, ln=True)
            
            pdf.ln(10)
        
        # Save PDF
        report_file = f"attendance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(report_file)
        print(f"Attendance report generated: {report_file}")