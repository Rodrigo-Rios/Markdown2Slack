from markdown2slack.app import Convert

convert = Convert()


def test_convert_link():
    link = "[Saiba mais](https://slack.com/)"
    expected = "<https://slack.com/|Saiba mais>"

    result = convert.markdown_to_slack_format(link)

    assert result == expected


def test_convert_escape_slack_chars():
    text = "&amp; &lt; &gt;"

    expected = "& < >"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_italic():
    text = "*italic*"

    expected = "_italic_"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_bold():
    text = "**bold**"

    expected = "*bold*"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_underlined():
    text = r"\_underlined\_"

    expected = "__underlined__"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_list():
    text = "- Item 1"

    expected = "• Item 1"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_h2():
    text = "## h2"

    expected = "*h2*\n\n"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_h1():
    text = "# h1"

    expected = "*h1*\n\n"

    result = convert.markdown_to_slack_format(text)

    assert result == expected


def test_convert_full_text():
    text = r"""# Welcome to Slack

## Main Features

- **Real-Time Communication**: Use Slack to exchange messages in real time with your team.
- **Integrations**: Connect with tools like [Google Drive](https://www.google.com/drive/), [Trello](https://trello.com/), and [GitHub](https://github.com/).
- **Advanced Search**: Quickly find past messages, files, and conversations.

## Text Formatting

- Bold: **Important**
- Italic: *emphasis*
- Underlined: \_highlight\_
- Italic: *This text will be italic*
- Bold: **This text will be bold**

## Lists

- List item 1
- List item 2
- List item 3

## Tasks

1. **Set up your profile**
2. **Join channels**
3. **Configure notifications**

[Learn more](https://slack.com/)

## Quotes

&gt; "Slack is an essential tool for modern collaboration." - Slack Team

For more information, visit [our website](https://slack.com/).

## Special Characters

Test special characters: &amp; &lt; &gt;
"""

    expected = """*Welcome to Slack*


*Main Features*


• *Real-Time Communication*: Use Slack to exchange messages in real time with your team.
• *Integrations*: Connect with tools like <https://www.google.com/drive/|Google Drive>, <https://trello.com/|Trello>, and <https://github.com/|GitHub>.
• *Advanced Search*: Quickly find past messages, files, and conversations.

*Text Formatting*


• Bold: *Important*
• Italic: _emphasis_
• Underlined: __highlight__
• Italic: _This text will be italic_
• Bold: *This text will be bold*

*Lists*


• List item 1
• List item 2
• List item 3

*Tasks*


1. *Set up your profile*
2. *Join channels*
3. *Configure notifications*

<https://slack.com/|Learn more>

*Quotes*


> "Slack is an essential tool for modern collaboration." - Slack Team

For more information, visit <https://slack.com/|our website>.

*Special Characters*


Test special characters: & < >
"""

    result = convert.markdown_to_slack_format(text)

    assert result == expected
