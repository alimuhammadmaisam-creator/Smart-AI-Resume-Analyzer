"""Module containing job-related data and configurations for Pakistan"""

# Job titles and skills suggestions
JOB_SUGGESTIONS = [
    {"text": "Software Engineer", "icon": "💻"},
    {"text": "Full Stack Developer", "icon": "🔧"},
    {"text": "Data Scientist", "icon": "📊"},
    {"text": "Product Manager", "icon": "📱"},
    {"text": "DevOps Engineer", "icon": "⚙️"},
    {"text": "UI/UX Designer", "icon": "🎨"},
    {"text": "Python Developer", "icon": "🐍"},
    {"text": "Java Developer", "icon": "☕"},
    {"text": "React Developer", "icon": "⚛️"},
    {"text": "Machine Learning Engineer", "icon": "🤖"},
    {"text": "Backend Developer", "icon": "🖧"},
    {"text": "Frontend Developer", "icon": "🎨"},
    {"text": "Node.js Developer", "icon": "🌿"},
    {"text": "Angular Developer", "icon": "📐"},
    {"text": "PHP Developer", "icon": "🐘"},
    {"text": "Ruby Developer", "icon": "💎"},
    {"text": "Go Developer", "icon": "🚀"},
    {"text": "C++ Developer", "icon": "🖥️"},
    {"text": "C# Developer", "icon": "🎮"},
    {"text": "Django Developer", "icon": "🛠️"},
    {"text": "Data Analyst", "icon": "📈"},
    {"text": "Big Data Engineer", "icon": "📡"},
    {"text": "Database Administrator", "icon": "🗄️"},
    {"text": "Business Intelligence Analyst", "icon": "📊"},
    {"text": "Cloud Engineer", "icon": "☁️"},
    {"text": "AWS Engineer", "icon": "☁️🔧"},
    {"text": "Azure Engineer", "icon": "☁️🖥️"},
    {"text": "Google Cloud Engineer", "icon": "☁️📡"},
    {"text": "Network Engineer", "icon": "🔌"},
    {"text": "AI Researcher", "icon": "🧠"},
    {"text": "NLP Engineer", "icon": "🗣️"},
    {"text": "Computer Vision Engineer", "icon": "👁️"},
    {"text": "Deep Learning Engineer", "icon": "🧠📚"},
    {"text": "Cybersecurity Analyst", "icon": "🔒"},
    {"text": "Ethical Hacker", "icon": "🕵️‍♂️"},
    {"text": "Security Engineer", "icon": "🛡️"},
    {"text": "Penetration Tester", "icon": "🔍"},
    {"text": "Cryptography Engineer", "icon": "🔑"},
    {"text": "Game Developer", "icon": "🎮"},
    {"text": "Embedded Systems Engineer", "icon": "🖧⚙️"},
    {"text": "Mobile App Developer", "icon": "📱"},
    {"text": "iOS Developer", "icon": "🍏"},
    {"text": "Android Developer", "icon": "🤖"},
    {"text": "Blockchain Developer", "icon": "🔗"},
    {"text": "IoT Developer", "icon": "🌐"},
    {"text": "AR/VR Developer", "icon": "🕶️"},
    {"text": "Project Manager", "icon": "📋"},
    {"text": "Technical Writer", "icon": "✍️"},
    {"text": "QA Engineer", "icon": "✅"},
    {"text": "Scrum Master", "icon": "🔄"},
    {"text": "Support Engineer", "icon": "📞"},
    {"text": "IT Consultant", "icon": "🧑‍💼"},
    {"text": "Technical Support Specialist", "icon": "🎧"}
]


# Location suggestions - organized by provinces and major cities of Pakistan
LOCATION_SUGGESTIONS = [
    # Work modes
    {"text": "Remote", "icon": "🏠", "type": "work_mode"},
    {"text": "Work from Home", "icon": "🏠", "type": "work_mode"},
    {"text": "Hybrid", "icon": "🏢", "type": "work_mode"},
    
    # Major tech hubs
    {"text": "Karachi", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Lahore", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Islamabad", "icon": "📍", "type": "city", "province": "Islamabad Capital Territory"},
    {"text": "Rawalpindi", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Faisalabad", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Multan", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Peshawar", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Quetta", "icon": "📍", "type": "city", "province": "Balochistan"},
    
    # Provinces
    {"text": "Sindh", "icon": "🗺️", "type": "province"},
    {"text": "Punjab", "icon": "🗺️", "type": "province"},
    {"text": "Khyber Pakhtunkhwa", "icon": "🗺️", "type": "province"},
    {"text": "Balochistan", "icon": "🗺️", "type": "province"},
    {"text": "Islamabad Capital Territory", "icon": "🗺️", "type": "province"},
    {"text": "Azad Kashmir", "icon": "🗺️", "type": "province"},
    {"text": "Gilgit-Baltistan", "icon": "🗺️", "type": "province"},
    
    # Sindh cities
    {"text": "Hyderabad", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Sukkur", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Larkana", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Nawabshah", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Mirpur Khas", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Jacobabad", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Shikarpur", "icon": "📍", "type": "city", "province": "Sindh"},
    {"text": "Thatta", "icon": "📍", "type": "city", "province": "Sindh"},
    
    # Punjab cities
    {"text": "Gujranwala", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Sialkot", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Bahawalpur", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Sargodha", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Sheikhupura", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Jhang", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Rahim Yar Khan", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Gujrat", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Kasur", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Sahiwal", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Okara", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Wah Cantt", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Dera Ghazi Khan", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Mirpur", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Hafizabad", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Sadiqabad", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Chakwal", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Jhelum", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Khanewal", "icon": "📍", "type": "city", "province": "Punjab"},
    {"text": "Mandi Bahauddin", "icon": "📍", "type": "city", "province": "Punjab"},
    
    # Khyber Pakhtunkhwa cities
    {"text": "Mardan", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Mingora", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Abbottabad", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Kohat", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Mansehra", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Nowshera", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Swabi", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Dera Ismail Khan", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Charsadda", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    {"text": "Bannu", "icon": "📍", "type": "city", "province": "Khyber Pakhtunkhwa"},
    
    # Balochistan cities
    {"text": "Gwadar", "icon": "📍", "type": "city", "province": "Balochistan"},
    {"text": "Turbat", "icon": "📍", "type": "city", "province": "Balochistan"},
    {"text": "Khuzdar", "icon": "📍", "type": "city", "province": "Balochistan"},
    {"text": "Hub", "icon": "📍", "type": "city", "province": "Balochistan"},
    {"text": "Sibi", "icon": "📍", "type": "city", "province": "Balochistan"},
    {"text": "Zhob", "icon": "📍", "type": "city", "province": "Balochistan"},
    {"text": "Loralai", "icon": "📍", "type": "city", "province": "Balochistan"},
    
    # Azad Kashmir cities
    {"text": "Muzaffarabad", "icon": "📍", "type": "city", "province": "Azad Kashmir"},
    {"text": "Mirpur AJK", "icon": "📍", "type": "city", "province": "Azad Kashmir"},
    {"text": "Kotli", "icon": "📍", "type": "city", "province": "Azad Kashmir"},
    {"text": "Rawalakot", "icon": "📍", "type": "city", "province": "Azad Kashmir"},
    {"text": "Bagh", "icon": "📍", "type": "city", "province": "Azad Kashmir"},
    
    # Gilgit-Baltistan cities
    {"text": "Gilgit", "icon": "📍", "type": "city", "province": "Gilgit-Baltistan"},
    {"text": "Skardu", "icon": "📍", "type": "city", "province": "Gilgit-Baltistan"},
    {"text": "Hunza", "icon": "📍", "type": "city", "province": "Gilgit-Baltistan"},
    {"text": "Chilas", "icon": "📍", "type": "city", "province": "Gilgit-Baltistan"}
]

# Function to get cities by province
def get_cities_by_state(province_name):
    """Get list of cities for a specific province"""
    return [loc for loc in LOCATION_SUGGESTIONS if loc.get("type") == "city" and loc.get("province") == province_name]

# Function to get all provinces
def get_all_states():
    """Get list of all provinces"""
    return [loc for loc in LOCATION_SUGGESTIONS if loc.get("type") == "province"]

# Job types
JOB_TYPES = [
    {"id": "all", "text": "All Types"},
    {"id": "full-time", "text": "Full Time"},
    {"id": "part-time", "text": "Part Time"},
    {"id": "contract", "text": "Contract"},
    {"id": "internship", "text": "Internship"},
    {"id": "remote", "text": "Remote"}
]

# Experience levels
EXPERIENCE_RANGES = [
    {"id": "all", "text": "All Levels"},
    {"id": "fresher", "text": "Fresher"},
    {"id": "1-3", "text": "1-3 years"},
    {"id": "3-5", "text": "3-5 years"},
    {"id": "5-7", "text": "5-7 years"},
    {"id": "7+", "text": "7+ years"}
]

# Salary ranges (in PKR Lakhs per annum)
SALARY_RANGES = [
    {"id": "all", "text": "All Ranges"},
    {"id": "0-5", "text": "0-5 Lac"},
    {"id": "5-10", "text": "5-10 Lac"},
    {"id": "10-15", "text": "10-15 Lac"},
    {"id": "15-25", "text": "15-25 Lac"},
    {"id": "25+", "text": "25+ Lac"}
]