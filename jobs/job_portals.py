"""Module for handling job portal integrations - Pakistan Edition"""
import urllib.parse
from typing import Dict, List
from .suggestions import LOCATION_SUGGESTIONS, get_cities_by_state

class JobPortal:
    """Class for searching jobs across multiple Pakistani job portals"""
    
    def __init__(self):
        """Initialize job portal URLs and parameters"""
        self.portals = [
            {
                "name": "Rozee.pk",
                "icon": "fas fa-briefcase",
                "color": "#FF6B35",
                "url": "https://www.rozee.pk/job/jsearch/q/{}/fpn/{}",
                "experience_param": ""
            },
            {
                "name": "Mustakbil.com",
                "icon": "fas fa-building",
                "color": "#1E88E5",
                "url": "https://www.mustakbil.com/jobs/keyword-{}-city-{}",
                "experience_param": ""
            },
            {
                "name": "PakJobs.pk",
                "icon": "fas fa-user-tie",
                "color": "#43A047",
                "url": "https://www.pakjobs.pk/search?q={}&l={}",
                "experience_param": ""
            },
            {
                "name": "Bayrozgar.pk",
                "icon": "fas fa-laptop",
                "color": "#F4511E",
                "url": "https://www.bayrozgar.pk/jobs?keywords={}&location={}",
                "experience_param": ""
            },
            {
                "name": "JobsAlert.pk",
                "icon": "fas fa-bell",
                "color": "#7B1FA2",
                "url": "https://www.jobsalert.pk/?s={}&location={}",
                "experience_param": ""
            },
            {
                "name": "LinkedIn",
                "icon": "fab fa-linkedin",
                "color": "#0A66C2",
                "url": "https://www.linkedin.com/jobs/search/?keywords={}&location={}&geoId=102095887&f_E={}",
                "experience_param": ""
            },
            {
                "name": "Indeed",
                "icon": "fas fa-search-dollar",
                "color": "#003A9B",
                "url": "https://pk.indeed.com/jobs?q={}&l={}&explvl={}",
                "experience_param": ""
            },
            {
                "name": "Glassdoor",
                "icon": "fas fa-door-open",
                "color": "#0CAA41",
                "url": "https://www.glassdoor.com/Job/pakistan-{}-jobs-SRCH_IL.0,8_IN192_KO9.htm?l={}",
                "experience_param": ""
            }
        ]

    def get_portal_list(self) -> List[Dict]:
        """Get list of available job portals"""
        return self.portals

    def format_query(self, query: str) -> str:
        """Format query string for URLs"""
        # Replace spaces with appropriate characters based on portal
        return query.replace(" ", "+")

    def format_location(self, location: str) -> str:
        """Format location string for URLs"""
        if not location:
            return ""
            
        # Check if location is a province
        location = location.strip()
        is_province = False
        
        # Check if the location is a province
        for loc in LOCATION_SUGGESTIONS:
            if loc.get("type") == "province" and loc.get("text").lower() == location.lower():
                is_province = True
                break
        
        # If it's a province, get the major city in that province for better job results
        if is_province:
            cities = get_cities_by_state(location)
            if cities:
                # Use the first city in the province (usually the capital or major city)
                location = cities[0]["text"]
        
        # Convert to lowercase and replace spaces with hyphens
        return location.lower().replace(" ", "-")

    def format_job_title(self, title: str) -> str:
        """Format job title for URLs"""
        # Remove common words and special characters
        title = title.lower()
        title = title.replace("developer", "").replace("engineer", "").strip()
        title = title.replace(" ", "-")
        return title.strip("-")

    def format_experience(self, experience: str) -> tuple:
        """Format experience for different job portals"""
        if not experience or experience == "all":
            return "", "0", "0", "entry"
        
        try:
            # Handle dictionary input
            if isinstance(experience, dict):
                exp_id = experience.get('id', 'all')
                if exp_id == 'all':
                    return "", "0", "0", "entry"
                
                # Split experience range (e.g., "1-3" -> ["1", "3"])
                if "-" in exp_id:
                    exp_min, exp_max = exp_id.split('-')
                    if exp_max == "+":
                        exp_max = "15"  # Set a reasonable maximum for 7+ years
                else:
                    # Handle "fresher" or other non-range values
                    exp_min = "0"
                    exp_max = "1"
                
                # Map to portal-specific format
                exp_level = {
                    "fresher": "0",
                    "0-1": "0",
                    "1-3": "1",
                    "3-5": "2",
                    "5-7": "3",
                    "7-10": "4",
                    "10+": "5"
                }.get(exp_id, "0")
                
                return exp_level, exp_min, exp_max, "entry" if exp_min == "0" else "experienced"
            
            return "", "0", "0", "entry"
            
        except Exception as e:
            print(f"Error formatting experience: {str(e)}")
            return "", "0", "0", "entry"

    def get_experience_param(self, portal_name, experience):
        """Get experience parameter for specific portal"""
        experience_id = experience.get("id", "all")
        
        if experience_id == "all":
            if portal_name == "LinkedIn":
                return ""
            elif portal_name == "Indeed":
                return "entry_level"
            else:
                return ""
        
        if portal_name == "LinkedIn":
            if experience_id == "fresher" or experience_id == "0-1":
                return "1"  # Entry level
            elif experience_id == "1-3" or experience_id == "3-5":
                return "2"  # Associate
            elif experience_id == "5-7" or experience_id == "7-10":
                return "3"  # Mid-Senior level
            elif experience_id == "10+":
                return "4"  # Director
        
        elif portal_name == "Indeed":
            if experience_id == "fresher" or experience_id == "0-1":
                return "entry_level"
            elif experience_id == "1-3" or experience_id == "3-5":
                return "mid_level"
            elif experience_id == "5-7" or experience_id == "7-10" or experience_id == "10+":
                return "senior_level"
        
        return ""

    def search_jobs(self, job_title, location, experience=None):
        """Search jobs across multiple portals"""
        if not experience:
            experience = {"id": "all", "text": "All Levels"}
        
        results = []
        
        for portal in self.portals:
            portal_name = portal["name"]
            
            # Format job title based on portal
            if portal_name in ["Rozee.pk", "LinkedIn", "Indeed"]:
                formatted_job = job_title.replace(' ', '%20')
            elif portal_name in ["Mustakbil.com", "PakJobs.pk", "Bayrozgar.pk", "JobsAlert.pk"]:
                formatted_job = job_title.lower().replace(' ', '-')
            elif portal_name == "Glassdoor":
                formatted_job = job_title.replace(' ', '+')
            else:
                formatted_job = job_title
            
            # Format location based on portal
            if portal_name in ["Rozee.pk"]:
                # Rozee uses city codes, use city name directly
                formatted_location = location if location else "Pakistan"
            elif portal_name in ["Mustakbil.com", "PakJobs.pk", "Bayrozgar.pk"]:
                formatted_location = location.lower().replace(' ', '-') if location else "pakistan"
            elif portal_name in ["LinkedIn", "Indeed", "JobsAlert.pk"]:
                formatted_location = location.replace(' ', '%20') if location else "Pakistan"
            elif portal_name == "Glassdoor":
                formatted_location = location if location else "Pakistan"
            else:
                formatted_location = location if location else "Pakistan"
            
            # Get experience parameter
            exp_param = self.get_experience_param(portal_name, experience)
            
            # Build URL based on portal
            try:
                if portal_name == "Rozee.pk":
                    url = portal["url"].format(formatted_job, formatted_location)
                elif portal_name == "Mustakbil.com":
                    url = portal["url"].format(formatted_job, formatted_location)
                elif portal_name in ["PakJobs.pk", "Bayrozgar.pk", "JobsAlert.pk"]:
                    url = portal["url"].format(formatted_job, formatted_location)
                elif portal_name == "LinkedIn":
                    url = portal["url"].format(formatted_job, formatted_location, exp_param)
                elif portal_name == "Indeed":
                    url = portal["url"].format(formatted_job, formatted_location, exp_param)
                elif portal_name == "Glassdoor":
                    url = portal["url"].format(formatted_job, formatted_location)
                else:
                    url = portal["url"]
                
                results.append({
                    "portal": portal_name,
                    "icon": portal["icon"],
                    "color": portal["color"],
                    "title": f"{job_title} jobs in {location if location else 'Pakistan'}",
                    "url": url
                })
            except Exception as e:
                print(f"Error creating URL for {portal_name}: {str(e)}")
                continue
        
        return results