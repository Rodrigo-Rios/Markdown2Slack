import re


class Convert:
    def __init__(self):
        self.markdown_link_pattern = r"\[([^\[]+)\]\((https?://[^\)]+)\)"
        self.escape_chars = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
        }

    def __replace_markdown_link(self, match):
        text = match.group(1)
        url = match.group(2)
        return f"<{url}|{text}>"

    def __escape_slack_chars(self, text):
        for char, escape in self.escape_chars.items():
            text = text.replace(escape, char)
        return text

    def __replace_markdown(self, text):
        # italic
        text = re.sub(r"(?<!\*)\*(?!\*)(.*?)\*(?!\*)", r"_\1_", text)

        # bold
        text = re.sub(r"\*\*(.*?)\*\*", r"*\1*", text)

        # Underlined
        text = re.sub(r"\\_(.*?)\\_", r"__\1__", text)

        # Markdown list (-, *, +) to Slack format (•)
        text = re.sub(r"(?m)^\s*[-*+]\s+", "• ", text)

        # Markdown (h2) to Slack format (*Subtítulo*)
        text = re.sub(r"(^|\n)## (.*+)(\n|$)", r"\1*\2*\n", text)

        # Markdown (h1) to Slack format (*Título*)
        text = re.sub(r"(^|\n)#\s*(.*+)\s*(\n|$)", r"\1*\2*\n\n", text)

        return text

    def markdown_to_slack_format(self, text):
        text = re.sub(self.markdown_link_pattern, self.__replace_markdown_link, text)

        text = self.__escape_slack_chars(text)
        text = self.__replace_markdown(text)

        return text
