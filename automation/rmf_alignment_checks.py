# Check for risk table
if not re.search(r'\| Risk Category \| Description \| Potential Impact \|', content):
    print("WARNING: Missing Identified Risk Scenarios table")
