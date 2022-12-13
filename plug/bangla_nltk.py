class BanglaNltk:

    def sentence_tokenizer(self, text: str) -> list:
        terminator = ["।", "?", "!"]
        tokens = []
        for i in text:
            if i in terminator:
                my_string = text[:text.index(i)+1]
                text = text[text.index(i)+1:]
                tokens.append(my_string.strip())
        return tokens