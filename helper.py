from pymed import PubMed
import base64
import requests

def save_mermaid_concept_map_as_image(mermaid_code: str, output_file: str = "output.svg"):
    """
    Saves a Mermaid diagram as an image using the Mermaid.ink API.
    
    Args:
        mermaid_code (str): The Mermaid code as a string.
        output_file (str): The output file name (supports .png, .svg, .pdf).
    """
    print("--------------------------------------------")
    print("In save mermaid concept map as image function...")
    if not output_file.endswith((".png", ".svg", ".pdf")):
        raise ValueError("Output file must have a valid extension (.png, .svg, .pdf)")
    elif not mermaid_code:
        raise ValueError("Mermaid code cannot be empty")
    
    if output_file.endswith(".png"):
        mermaid_api_url = "https://mermaid.ink/img/"
    elif output_file.endswith(".svg"):
        mermaid_api_url = "https://mermaid.ink/svg/"
    
    # Encode Mermaid code to Base64
    encoded_diagram = base64.urlsafe_b64encode(mermaid_code.encode()).decode()
    
    # Generate the full API URL
    image_url = f"{mermaid_api_url}{encoded_diagram}"
    
    try:
        # Fetch the image from the API
        response = requests.get(image_url)
        response.raise_for_status()
        
        # Save the image
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"Diagram saved as {output_file}")

        return f"Diagram saved as {output_file}"
    except requests.RequestException as e:
        print(f"Error generating image: {e}")


def pubmed_search(query, max_results=5):
    print("--------------------------------------------")
    print("Searching PubMed for articles...")
    print(f"Query: {query}")
    print(f"Max Results: {max_results}")
    print("--------------------------------------------")
    pubmed = PubMed(tool="MyTool", email="sharozhaseeb1@gmail.com")
    results = pubmed.query(query, max_results=max_results)

    result_list = []
    for article in results:
        child_dict = {}
        child_dict['title'] = article.title
        child_dict['authors'] = [((author['lastname'] or '') + ', ' + (author['firstname'] or '')).strip(', ') for author in article.authors]
        child_dict['abstract'] = article.abstract
        child_dict['publication_date'] = article.publication_date
        result_list.append(child_dict)
    
    return result_list


def convert_pubmed_resp_to_str(articles):
    master_str = ""
    for article in articles:
        formatted_string = f"""Title: {article['title']}
        Authors: {', '.join(article['authors'])}
        Abstract: {article['abstract']}
        Publication Date: {article['publication_date'].strftime('%Y-%m-%d')}
        {'-' * 80}\n"""
        master_str += formatted_string
    return str(master_str)