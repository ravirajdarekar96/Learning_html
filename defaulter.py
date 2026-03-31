def classify_complaint(complaint):
    complaint = complaint.lower()

    if "wifi" in complaint or "system" in complaint or "laptop" in complaint:
        return "Technical"
    
    elif "exam" in complaint or "marks" in complaint or "assignment" in complaint:
        return "Academic"
    
    elif "fee" in complaint or "office" in complaint or "staff" in complaint:
        return "Administrative"
    
    else:
        return "Unknown Category"

# Input from user
user_input = input("Enter your complaint: ")

# Output
category = classify_complaint(user_input)
print("Complaint Category:", category)