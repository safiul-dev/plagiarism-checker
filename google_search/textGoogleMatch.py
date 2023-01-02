from googlesearch import search
from plug.plagiarism_check import PlagiarismChecker
from plug.bangla_nltk import BanglaNltk

class PlagResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"PlagResult(url={self.url}, title={self.title}, description={self.description})"

class GooglePlagiarismCheck:

    def searchGoogle (self, query):

        result = []
        if query:
            for i in search('"' + query + '"',  5, "bn", None, True):
                result.append({
                    "url":i.url,
                    "title": i.title,
                    "description": i.description
                }
                )

        return result
    
    def plag_check(self, text):

        result = []
        b_nltk = BanglaNltk()
        text_array = b_nltk.sentence_tokenizer(text)
        for t in text_array:

            googleResults = self.searchGoogle(t)
            plag_obj = PlagiarismChecker()

            if len(googleResults) > 0 :
                for google_obj in googleResults:
                    text2 = google_obj['description']
                    plag_result = plag_obj.levenshtein(t, text2)
                    percent = 0
                    if plag_result >= 50 :
                        percent = 100
                        result.append({
                            "percent": percent,
                            "url": google_obj['url'],
                            "text": t
                        })
        return result
                