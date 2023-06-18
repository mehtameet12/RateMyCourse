import requests
from bs4 import BeautifulSoup
import csv
import re


urls = [
  'http://catalogue.uottawa.ca/en/courses/cpt/',
  'http://catalogue.uottawa.ca/en/courses/adm/',
  'http://catalogue.uottawa.ca/en/courses/amm/',
  'http://catalogue.uottawa.ca/en/courses/afr/',
  'http://catalogue.uottawa.ca/en/courses/ana/',
  'http://catalogue.uottawa.ca/en/courses/anp/',
  'http://catalogue.uottawa.ca/en/courses/ane/',
  'http://catalogue.uottawa.ca/en/courses/ant/',
  'http://catalogue.uottawa.ca/en/courses/arb/',
  'http://catalogue.uottawa.ca/en/courses/cla/',
  'http://catalogue.uottawa.ca/en/courses/lcl/',
  'http://catalogue.uottawa.ca/en/courses/cli/',
  'http://catalogue.uottawa.ca/en/courses/cml/',
  'http://catalogue.uottawa.ca/en/courses/cmn/',
  'http://catalogue.uottawa.ca/en/courses/cpl/',
  'http://catalogue.uottawa.ca/en/courses/ceg/',
  'http://catalogue.uottawa.ca/en/courses/csi/',
  'http://catalogue.uottawa.ca/en/courses/ech/',
  'http://catalogue.uottawa.ca/en/courses/crm/',
  'http://catalogue.uottawa.ca/en/courses/sec/',
  'http://catalogue.uottawa.ca/en/courses/arb/',
  'http://catalogue.uottawa.ca/en/courses/acp/',
  'http://catalogue.uottawa.ca/en/courses/amt/',
  'http://catalogue.uottawa.ca/en/courses/asi/',
  'http://catalogue.uottawa.ca/en/courses/bil/',
  'http://catalogue.uottawa.ca/en/courses/bch/',
  'http://catalogue.uottawa.ca/en/courses/bnf/',
  'http://catalogue.uottawa.ca/en/courses/bio/',
  'http://catalogue.uottawa.ca/en/courses/bmg/',
  'http://catalogue.uottawa.ca/en/courses/bim/',
  'http://catalogue.uottawa.ca/en/courses/bps/',
  'http://catalogue.uottawa.ca/en/courses/cdn/',
  'http://catalogue.uottawa.ca/en/courses/cts/',
  'http://catalogue.uottawa.ca/en/courses/cmm/',
  'http://catalogue.uottawa.ca/en/courses/clt/',
  'http://catalogue.uottawa.ca/en/courses/tox/',
  'http://catalogue.uottawa.ca/en/courses/chg/',
  'http://catalogue.uottawa.ca/en/courses/chm/',
  'http://catalogue.uottawa.ca/en/courses/chn/',
  'http://catalogue.uottawa.ca/en/courses/cvg/',
  'http://catalogue.uottawa.ca/en/courses/drc/',
  'http://catalogue.uottawa.ca/en/courses/sds/',
  'http://catalogue.uottawa.ca/en/courses/dcn/',
  'http://catalogue.uottawa.ca/en/courses/dhn/',
  'http://catalogue.uottawa.ca/en/courses/dti/',
  'http://catalogue.uottawa.ca/en/courses/thd/',
  'http://catalogue.uottawa.ca/en/courses/eas/',
  'http://catalogue.uottawa.ca/en/courses/ecc/',
  'http://catalogue.uottawa.ca/en/courses/ees/',
  'http://catalogue.uottawa.ca/en/courses/ele/',
  'http://catalogue.uottawa.ca/en/courses/epd/',
  'http://catalogue.uottawa.ca/en/courses/ecm/',
  'http://catalogue.uottawa.ca/en/courses/efs/',
  'http://catalogue.uottawa.ca/en/courses/egs/',
  'http://catalogue.uottawa.ca/en/courses/egm/',
  'http://catalogue.uottawa.ca/en/courses/egi/',
  'http://catalogue.uottawa.ca/en/courses/egy/',
  'http://catalogue.uottawa.ca/en/courses/che/',
  'http://catalogue.uottawa.ca/en/courses/sve/',
  'http://catalogue.uottawa.ca/en/courses/eng/',
  'http://catalogue.uottawa.ca/en/courses/fra/',
  'http://catalogue.uottawa.ca/en/courses/fys/',
  'http://catalogue.uottawa.ca/en/courses/gen/',
  'http://catalogue.uottawa.ca/en/courses/geo/',
  'http://catalogue.uottawa.ca/en/courses/ger/',
  'http://catalogue.uottawa.ca/en/courses/gsm/',
  'http://catalogue.uottawa.ca/en/courses/his/',
  'http://catalogue.uottawa.ca/en/courses/hps/',
  'http://catalogue.uottawa.ca/en/courses/hss/',
  'http://catalogue.uottawa.ca/en/courses/ise/',
  'http://catalogue.uottawa.ca/en/courses/ins/',
  'http://catalogue.uottawa.ca/en/courses/ita/',
  'http://catalogue.uottawa.ca/en/courses/jpn/',
  'http://catalogue.uottawa.ca/en/courses/geo/',
  'http://catalogue.uottawa.ca/en/courses/llm/',
  'http://catalogue.uottawa.ca/en/courses/mas/',
  'http://catalogue.uottawa.ca/en/courses/mat/',
  'http://catalogue.uottawa.ca/en/courses/mbi/',
  'http://catalogue.uottawa.ca/en/courses/mic/',
  'http://catalogue.uottawa.ca/en/courses/mne/',
  'http://catalogue.uottawa.ca/en/courses/mpi/',
  'http://catalogue.uottawa.ca/en/courses/mtg/',
  'http://catalogue.uottawa.ca/en/courses/mus/',
  'http://catalogue.uottawa.ca/en/courses/neu/',
  'http://catalogue.uottawa.ca/en/courses/nur/',
  'http://catalogue.uottawa.ca/en/courses/phi/',
  'http://catalogue.uottawa.ca/en/courses/phy/',
  'http://catalogue.uottawa.ca/en/courses/pcs/',
  'http://catalogue.uottawa.ca/en/courses/pmp/',
  'http://catalogue.uottawa.ca/en/courses/pap/',
  'http://catalogue.uottawa.ca/en/courses/psc/',
  'http://catalogue.uottawa.ca/en/courses/psy/',
  'http://catalogue.uottawa.ca/en/courses/pub/',
  'http://catalogue.uottawa.ca/en/courses/rel/',
  'http://catalogue.uottawa.ca/en/courses/sab/',
  'http://catalogue.uottawa.ca/en/courses/sdp/',
  'http://catalogue.uottawa.ca/en/courses/soc/',
  'http://catalogue.uottawa.ca/en/courses/sps/',
  'http://catalogue.uottawa.ca/en/courses/slh/',
  'http://catalogue.uottawa.ca/en/courses/spa/',
  'http://catalogue.uottawa.ca/en/courses/spm/',
  'http://catalogue.uottawa.ca/en/courses/sta/',
  'http://catalogue.uottawa.ca/en/courses/chi/',
  'http://catalogue.uottawa.ca/en/courses/ces/',
  'http://catalogue.uottawa.ca/en/courses/syu/',
  'http://catalogue.uottawa.ca/en/courses/tmm/',
  'http://catalogue.uottawa.ca/en/courses/the/',
  'http://catalogue.uottawa.ca/en/courses/tpd/',
  'http://catalogue.uottawa.ca/en/courses/tur/',
  'http://catalogue.uottawa.ca/en/courses/ukr/',
  'http://catalogue.uottawa.ca/en/courses/vpm/',
  'http://catalogue.uottawa.ca/en/courses/zoo/'
]

# Create a list to store the extracted data
data = []

for url in urls:
    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the course elements on the page
    course_elements = soup.find_all("div", class_="courseblock")

    # Extract the course code and description from each course element
    for course_element in course_elements:
        course_code_element = course_element.find("p", class_="courseblocktitle noindent")
        course_description_element = course_element.find("p", class_="courseblockdesc noindent")

        # Check if the elements exist before accessing their text attribute
        if course_code_element is not None and course_description_element is not None:
            course_code = course_code_element.text.strip()

            # Clean the course code
            cleaned_code = re.sub(r'\([^)]*\)', '', course_code)
            cleaned_code = re.sub(r'([A-Z]{3})(\d{4})', r'\1,\2', cleaned_code)
            cleaned_code = re.sub(r'(\d{4})', r'\1,', cleaned_code)

            # Add the cleaned course code to the data list
            data.append([cleaned_code])

# Save the data as a CSV file
filename = "course_data.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("CSV file saved successfully!")

