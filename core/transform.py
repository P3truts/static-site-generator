from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from core.split import Split
from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


class Transform:
    @staticmethod
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        if text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})

        raise ValueError(f"TextNode is missing text type!")

    @staticmethod
    def text_to_textnodes(text):
        node = TextNode(text, TextType.PLAIN_TEXT)
        bold_nodes = Split.split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        italic_nodes = Split.split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC_TEXT)
        code_nodes = Split.split_nodes_delimiter(italic_nodes, "`", TextType.CODE_TEXT)
        image_nodes = Split.split_nodes_images(code_nodes)
        link_nodes = Split.split_nodes_links(image_nodes)

        return link_nodes

    @staticmethod
    def block_to_blocktype(md_block):
        head_patt = r"#{1,6}\s"
        if "#" in md_block[0] and bool(re.search(head_patt, md_block[:8])):
            return BlockType.HEADING

        code_patt = "```\n"
        code_end_patt = "```"
        if code_patt in md_block[:5] and code_end_patt in md_block[3:]:
            return BlockType.CODE

        quote_patt = ">"
        if quote_patt in md_block[0]:
            return BlockType.QUOTE

        uno_list_patt = "- "
        if uno_list_patt in md_block[:2]:
            return BlockType.UNORDERED_LIST

        o_list_patt = r"1. "
        if o_list_patt in md_block[:3]:
            return BlockType.ORDERED_LIST

        return BlockType.PARAGRAPH
