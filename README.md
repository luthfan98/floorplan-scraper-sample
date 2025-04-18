# 🏠 Floorplan Scraper Sample Project

This project demonstrates a simple Python-based data scraper and organizer focused on collecting **floor plans** for architecture and real estate datasets.

It is a sample prototype designed to show capability in:
- Downloading and organizing files
- Creating structured metadata for AI/ML purposes
- Preparing scalable workflow for larger-scale data collection projects

---

## ✨ Features

- Download floor plan images from a list of public URLs
- Save and organize files into structured folders
- Automatically generate a metadata spreadsheet (CSV) including:
  - File name
  - Project type
  - Region
  - File format
  - Source URL
- Basic error handling for failed downloads

---

## ⚙️ Tech Stack

- **Python 3.12**
- **Requests** - for HTTP requests
- **Pandas** - for metadata CSV generation
- **OS & mimetypes** - for folder/file operations and format detection

---

## 📂 Project Structure

```
floorplan-scraper-sample/
├── scraper.py               # Main script for downloading and organizing data
├── requirements.txt         # Python libraries required
├── README.md                 # Project documentation
├── data/
│   └── FloorPlans/           # Downloaded floor plan files
├── metadata/
│   └── floorplan_metadata.csv # Metadata of downloaded files
```

---

## 🚀 Future Enhancements

This prototype focuses on a simple demonstration. In a full project, it can be extended to:
- Automatically crawl websites starting from a main URL (e.g., Zillow, ArchDaily)
- Parse floor plans dynamically using BeautifulSoup or Selenium
- Scrape Bill of Materials (BOMs) alongside floor plans
- Handle different formats (PDF, CAD, DWG)

---

## 📜 Disclaimer

This project is intended for demonstration purposes only.  
All sample data are collected from publicly accessible, open-license sources.

---

## 📞 Contact

For project inquiries, please contact:

**Luthfan**  
Software Engineer | Automation Specialist  