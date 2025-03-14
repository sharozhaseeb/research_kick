from pymed import PubMed



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