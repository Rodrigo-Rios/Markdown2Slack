# Markdown to Slack Format Conversion Tool

This tool was developed to simplify the conversion of Markdown text to the format accepted by Slack. By using this tool, you can complement the Slack API and easily send formatted messages to channels, groups, and direct conversations on Slack, leveraging the platform's unique formatting.

## Features

Automatic Conversion: Automatically converts Markdown text to Slack format.

## How to use

1. Install the library:

    ```bash
    pip install markdown2slack

    ```

2. Import the library and create an instance in your code:

    ```python
    from markdown2slack.app import Convert

    converter = Convert()
    ```

3. Convert the Markdown text to Slack format:

    ```python
    markdown_text = """
    # Heading
    **Bold text**
    *Italic text*
    [Link](https://example.com)
    """
    slack_text = converter.markdown_to_slack_format(markdown_text)
    print(slack_text)
    ```

## Example

### Before

```text
**Bold text**
*Italic text*
[Link](https://example.com)
```

## After

```text
*Bold text*
_Italic text_
<https://example.com|Link>
```
