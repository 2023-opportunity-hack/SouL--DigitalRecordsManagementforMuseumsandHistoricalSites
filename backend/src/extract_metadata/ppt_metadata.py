from pptx import Presentation
from helper import convert_docx_format


def view_ppt_metadata(ppt_path):
    """
    View metadata information from a PowerPoint presentation.

    Parameters:
    - ppt_path (str): The path to the PowerPoint presentation file.

    Returns:
    - dict: A dictionary containing metadata information.
      Example:
      {
          'author': 'Unknown',
          'Create Date': None
      }

    Note:
    This function extracts metadata information, such as author and creation date,
    from the specified PowerPoint presentation. If the information is not available,
    default values are provided.

    Dependencies:
    - Requires the 'pptx' library.
    - The 'convert_docx_format' function from the 'helper' module is used to format dates.

    Example:
    ```python
    metadata = view_ppt_metadata("path/to/presentation.pptx")
    print(metadata)
    ```

    :param ppt_path: The path to the PowerPoint presentation file.
    :type ppt_path: str
    :return: A dictionary containing metadata information.
    :rtype: dict
    """
    ppt = Presentation(ppt_path)

    # Accessing core properties
    core_props = ppt.core_properties
    metadata = {
        'author': 'Unknown',
        'Create Date': None
    }

    # Check if 'author' information is available
    if core_props.author:
        metadata['author'] = core_props.author

    # Check if 'created' information is available
    if core_props.created:
        # Use the 'convert_docx_format' function to format the creation date
        metadata['Create Date'] = convert_docx_format(core_props.created)

    return metadata
