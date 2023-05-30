from .advance_search import search
from plug.plagiarism_check import PlagiarismChecker
from plug.bangla_nltk import BanglaNltk


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
        googleResults = self.searchGoogle(text)
        plag_obj = PlagiarismChecker()

        if len(googleResults) > 0 :
            for google_obj in googleResults:
                text2 = google_obj['description']
                plag_result = plag_obj.levenshtein(text, text2)
                percent = 0
                if plag_result >= 50 :
                    percent = 100
                    result.append({
                        "percent": percent,
                        "url": google_obj['url'],
                        "text": text
                    })
        return result
                