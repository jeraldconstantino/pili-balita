def get_url(news):
    generated_URL = "https://pilibalita-api.herokuapp.com" # Kindly replace it based on your generated URL. 
    final_URL = f"{generated_URL}/hula?balita={news}"
    return final_URL
