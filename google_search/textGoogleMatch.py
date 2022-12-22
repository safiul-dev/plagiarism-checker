from googlesearch import search

class GooglePlagiarismCheck:

    def searchGoogle (self, query):

        result = []
        for i in search('"' + query + '"',  5, "bn", None, True, 2):
            result.append({
                "url":i.url,
                "title": i.title,
                "description": i.description
            })

        return result