from lxml import etree ,objectify

def extract_text_from_ssml(ssml_string):
    try:
        root = etree.fromstring(ssml_string)
        print(root)
        text_parts = []
        for element in root.iter():  # Iterate through all elements
            print(element.tag)
            if element.text:
                text_parts.append(element.text)
            # Handle tail text (text after a closing tag)
            if element.tail:
                text_parts.append(element.tail)

        return "".join(text_parts).strip() # Join and strip whitespace

    except etree.XMLSyntaxError as e:
        print(f"Error parsing SSML: {e}")
        return ""  # Or handle the error as needed

# Example usage:
ssml_input = """
<speak>
  <prosody rate="slow">Hello,</prosody> <break time="500ms"/>
  My name is <say-as interpret-as="characters">IBM</say-as>.
</speak>
"""

extracted_text = extract_text_from_ssml(ssml_input)
print(f"Extracted text: '{extracted_text}'")

ssml_input_with_tail = """
<speak>
  Hello,<break time="500ms"/>World
</speak>
"""
extracted_text_with_tail = extract_text_from_ssml(ssml_input_with_tail)
print(f"Extracted text with tail: '{extracted_text_with_tail}'")