# html node handling


class HTMLNode:
    """
    HTMLNode class will represent a "node" in an HTML document tree.
    It can be block level or inline, and is designed to only output HTML.
    """

    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: "HTMLNode" = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value="{self.value}", children={self.children}, props={self.props})'

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        atributes_string = ""
        for k, v in self.props.items():
            atributes_string += f' {k}="{v}"'
        return atributes_string
