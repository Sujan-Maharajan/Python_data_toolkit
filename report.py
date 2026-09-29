def create_report(rows_loaded, rows_cleaned, rows_dropped, drop_reasons, average, cities, oldest, youngest):

    report = ""

    report+= "DATA CLEANING REPORT\n"
    report+= "====================\n\n"

    report+= f"Rows loaded: {rows_loaded}\n"
    report+= f"Rows cleaned: {rows_cleaned}\n"
    report+= f"Rows dropped: {rows_dropped}\n\n"

    report+= "Drop reasons:\n"

    for reason, count in drop_reasons.items():
        report+= f"{reason}: {count}\n"

    report+= "\nKey Statistics:\n"
    report+= f"Average score: {average}\n"
    report+= f"People per city: {cities}\n"
    report+= f"Oldest person: {oldest}\n"
    report+= f"Youngest person: {youngest}\n"

    return report
