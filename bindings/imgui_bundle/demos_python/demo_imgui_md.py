from imgui_bundle import imgui_md, immapp


def example_markdown_string() -> str:
    markdown = r"""
# Markdown example

Hello World! <br>
![World](images/world.jpg)

## Acknowledgments
This markdown renderer is based on [imgui_md](https://github.com/mekhontsev/imgui_md), by Dmitry Mekhontsev.

### Supported features

imgui_md currently supports the following markdown functionality:

* Wrapped text
* Headers
* *Emphasis* (\*Emphasis\*)
* **Bold** (\*\*Bold\*\*)
* Ordered and unordered list, sub-lists
* [Link](https://github.com/mekhontsev/imgui_md)  ( \[Link\](https://github.com/mekhontsev/imgui_md) )
* Image
* Horizontal rule (add "\-\-\-" on a line)
* Tables
* <u>Underline</u> via \<u>...\</u>
* ~~Strikethrough~~
* HTML elements: \<br> \<hr> \<u> \<div> \&nbsp;
* Backslash Escapes

Most format tags can be mixed!

### Known limitations

1. table rendering: text might overflow the borders
2. div: needs to be corrected
    """
    return markdown


def demo_imgui_md():
    s = example_markdown_string()
    imgui_md.render(s)


def demo_imgui_md_main():
    immapp.run(demo_imgui_md, with_markdown=True, window_size=(800, 800))


if __name__ == "__main__":
    demo_imgui_md_main()