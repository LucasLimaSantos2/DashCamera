import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro na requisição: {str(e)}"}
    except ValueError:
        return {"error": "Resposta não é um JSON válido"}
