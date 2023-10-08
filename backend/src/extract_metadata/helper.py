from datetime import datetime


def convert_pdf_date(pdf_date):
    # Extracting the relevant part of the date string
    date_str = pdf_date[2:15]  # Extracts '20231007224453'

    # Converting the string to a datetime object
    pdf_datetime = datetime.strptime(date_str, "%Y%m%d%H%M%S")

    # Formatting the datetime object to the desired format
    formatted_date = pdf_datetime.strftime("%m-%d-%Y")

    return formatted_date


def convert_docx_format(dt_object):
    # Format the datetime object to the desired format
    formatted_date = dt_object.strftime("%m-%d-%Y")

    return formatted_date
