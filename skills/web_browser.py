import webbrowser


class WebBrowser:
    def __init__(self, text_to_search_for):
        self.text = text_to_search_for
        self.google_chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        self.google_search_url = f"www.google.com/search?query={text_to_search_for}"

    def orchestrate_flow(self):
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(self.google_chrome_path))
        webbrowser.get("chrome").open_new_tab(self.google_search_url)
        return "This is what I found on the web!"
