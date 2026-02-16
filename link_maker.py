import re

CONTRIBUTOR_ID = "wt.mc_id=studentamb_506539"

def clean_and_add_id(url):
    # remove any existing WT.mc_id or wt.mc_id parameters
    url = re.sub(r'[?&]WT\.mc_id=[^&]*', '', url)
    url = re.sub(r'[?&]wt\.mc_id=[^&]*', '', url)

    # fix leftover ? or &
    url = url.rstrip('?').rstrip('&')

    # add your contributor id correctly
    if "?" in url:
        return f"{url}&{CONTRIBUTOR_ID}"
    else:
        return f"{url}?{CONTRIBUTOR_ID}"

print("Microsoft Ambassador Link Generator")
print("Type 'exit' to quit\n")

while True:
    link = input("Paste Microsoft link: ")

    if link.lower() == "exit":
        break

    result = clean_and_add_id(link)
    print("✅ Final Link:")
    print(result)
    print()
