from datetime import datetime


def convert_pdf_date(pdf_date):
    """
    Convert a PDF date string to a formatted date.

    Parameters:
    - pdf_date (str): The date string from the PDF.

    Returns:
    - str: Formatted date string in the format 'MM/DD/YYYY'.

    Example:
    ```python
    formatted_date = convert_pdf_date('20231007224453')
    print(formatted_date)
    ```

    :param pdf_date: The date string from the PDF.
    :type pdf_date: str
    :return: Formatted date string.
    :rtype: str
    """
    # Extracting the relevant part of the date string
    date_str = pdf_date[2:15]  # Extracts '20231007224453'

    # Converting the string to a datetime object
    pdf_datetime = datetime.strptime(date_str, "%Y%m%d%H%M%S")

    # Formatting the datetime object to the desired format
    formatted_date = pdf_datetime.strftime("%m/%d/%Y")

    return formatted_date


def convert_docx_format(dt_object):
    """
    Convert a datetime object to a formatted date.

    Parameters:
    - dt_object (datetime): The datetime object.

    Returns:
    - str: Formatted date string in the format 'MM/DD/YYYY'.

    Example:
    ```python
    dt_object = datetime(2023, 10, 7, 22, 44, 53)
    formatted_date = convert_docx_format(dt_object)
    print(formatted_date)
    ```

    :param dt_object: The datetime object.
    :type dt_object: datetime
    :return: Formatted date string.
    :rtype: str
    """
    # Format the datetime object to the desired format
    formatted_date = dt_object.strftime("%m/%d/%Y")

    return formatted_date
