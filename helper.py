from pymed import PubMed
import base64
import requests
import requests
import io
import matplotlib.pyplot as plt
import networkx as nx



def generate_and_upload_mindmap(mermaid_code):
    """
    Parses Mermaid mindmap code, generates a mind map, and uploads it as an SVG to GoFile.
    
    Args:
        mermaid_code (str): Mermaid mindmap syntax.
    
    Returns:
        str: GoFile download link for the generated mind map SVG.
    """
    def parse_mermaid_mindmap(code):
        """Converts Mermaid mindmap syntax into a list of edges for graph plotting."""
        lines = code.strip().split("\n")
        edges = []
        parent_stack = []

        for line in lines:
            indent_level = len(line) - len(line.lstrip())  # Count leading spaces
            node = line.strip()

            if node:
                while parent_stack and parent_stack[-1][1] >= indent_level:
                    parent_stack.pop()

                if parent_stack:
                    edges.append((parent_stack[-1][0], node))

                parent_stack.append((node, indent_level))

        return edges

    def hierarchy_pos(G, root=None, width=1., vert_gap=0.4, xcenter=0.5, pos=None, level=0):
        """Assigns hierarchical positions for nodes in the tree."""
        if pos is None:
            pos = {root: (xcenter, 1)}
        children = list(G.successors(root))
        if not children:
            return pos

        dx = width / max(1, len(children))
        next_x = xcenter - width / 2 - dx / 2
        for child in children:
            next_x += dx
            pos[child] = (next_x, 1 - vert_gap * (level + 1))
            pos = hierarchy_pos(G, root=child, width=dx, vert_gap=vert_gap, xcenter=next_x, pos=pos, level=level+1)
        return pos

    # Step 1: Parse Mermaid mind map structure
    edges = parse_mermaid_mindmap(mermaid_code)
    if not edges:
        raise ValueError("Invalid Mermaid mindmap format.")

    # Step 2: Create a graph using NetworkX
    G = nx.DiGraph()
    G.add_edges_from(edges)
    root = edges[0][0]  # Take the first node as root
    pos = hierarchy_pos(G, root)

    # Step 3: Generate the mind map image in SVG format
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray",
            node_size=4500, font_size=4.5, font_weight="bold", alpha=0.8, arrows=False)

    svg_buffer = io.BytesIO()
    plt.savefig(svg_buffer, format="svg", bbox_inches="tight")
    plt.close()
    svg_buffer.seek(0)

    # Step 4: Upload the SVG to GoFile
    files = {"file": ("mindmap.svg", svg_buffer, "image/svg+xml")}
    response = requests.post("https://store1.gofile.io/uploadFile", files=files)
    response.raise_for_status()
    data = response.json()["data"]

    # Construct the direct download link
    server = data["servers"][0]  # Use the first available server
    file_id = data["id"]
    file_name = data["name"]
    return f"https://{server}.gofile.io/download/web/{file_id}/{file_name}"
# def save_mermaid_concept_map_as_image(mermaid_code: str, output_file: str = "output.svg"):
#     """
#     Saves a Mermaid diagram as an image using the Mermaid.ink API.
    
#     Args:
#         mermaid_code (str): The Mermaid code as a string.
#         output_file (str): The output file name (supports .png, .svg, .pdf).
#     """
#     print("--------------------------------------------")
#     print("In save mermaid concept map as image function...")
#     if not output_file.endswith((".png", ".svg", ".pdf")):
#         raise ValueError("Output file must have a valid extension (.png, .svg, .pdf)")
#     elif not mermaid_code:
#         raise ValueError("Mermaid code cannot be empty")
    
#     if output_file.endswith(".png"):
#         mermaid_api_url = "https://mermaid.ink/img/"
#     elif output_file.endswith(".svg"):
#         mermaid_api_url = "https://mermaid.ink/svg/"
    
#     # Encode Mermaid code to Base64
#     encoded_diagram = base64.urlsafe_b64encode(mermaid_code.encode()).decode()
    
#     # Generate the full API URL
#     image_url = f"{mermaid_api_url}{encoded_diagram}"
    
#     try:
#         # Fetch the image from the API
#         response = requests.get(image_url)
#         response.raise_for_status()
        
#         # Save the image
#         with open(output_file, "wb") as file:
#             file.write(response.content)
#         print(f"Diagram saved as {output_file}")

#         return f"Diagram saved as {output_file}"
#     except requests.RequestException as e:
#         print(f"Error generating image: {e}")


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