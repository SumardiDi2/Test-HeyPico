1. Clone the api with https://github.com/SumardiDi2/Test-HeyPico.git
2. Add google api key in main.py code
3. Open file path in cmd/powershell and run "uvicorn main:app --reload"
4. For testing API use http://localhost:8000/search?query=best+restaurant
5. Install LLM Open WebUI with "pip install open-webui"
6. The run "open-webui serve"
7. Open WebUI in local: http://localhost:8080
8. Then open menu Workspace -> Tools
9. Click New Tool
10. Add code like this
```python
import requests

class Tools:
    def __init__(self):
        self.api_url = "http://localhost:8000/search"

    def search_location(self, query: str) -> str:
        """
        Use this tool to search for restaurants, locations, or addresses.
        Input must include specific search keywords.
        """
        try:
            response = requests.get(self.api_url, params={"query": query})
            data = response.json()

            if not data.get("results"):
                return "Sorry, I didn't find the place."

            formatted_results = "Here are search results:\n\n"

            for p in data["results"]:
                formatted_results += f"### {p['name']}\n"
                formatted_results += f"📍 **Address:** {p['address']}\n"

                formatted_results += f'<iframe width="100%" height="250" style="border:0" loading="lazy" allowfullscreen src="{p["embed_map"]}"></iframe>\n'

                formatted_results += (
                    f"🔗 [Open Directions in Google Maps]({p['direction_link']})\n\n"
                )
                formatted_results += "---\n"

            return formatted_results

        except Exception as e:
            return f"An error occurred while contacting the API: {str(e)}"

```
11. Open new chat, add Intergration logo in bottom chat, the add question in chat
