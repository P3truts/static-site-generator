from src.textnode import TextNode, TextType
from core.extract import Extract
import re

class Split:

    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        if not old_nodes:
            raise ValueError("Nodes are missing!")

        res_list = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                res_list.append(node)
            else:
                new_nodes = node.text.split(delimiter)
                if len(new_nodes) == 1 and delimiter not in new_nodes:
                    res_list.append(node)
                    continue
                if len(new_nodes) < 3 or len(new_nodes) % 2 == 0: 
                    raise Exception("Invalid Markdown syntax!")
                for new_node in new_nodes:
                    if new_nodes.index(new_node) % 2 == 0:
                        res_node = TextNode(new_node, TextType.PLAIN_TEXT)
                    else:
                        res_node = TextNode(new_node, text_type)
                    res_list.append(res_node)

        return res_list

    @staticmethod
    def split_nodes_images(old_nodes):
        if not old_nodes:
            raise ValueError("Nodes are missing!")

        res_list = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                res_list.append(node)
            else:
                patt = r"(\!\[(?:.*?)\]\((?:.*?)\))"
                new_nodes = re.split(patt, node.text)
                if len(new_nodes) == 1 and "![" not in new_nodes[0]:
                    res_list.append(node)
                    continue
                if len(new_nodes) < 3 or len(new_nodes) % 2 == 0: 
                    raise Exception("Invalid Markdown syntax!")
                for new_node in new_nodes:
                    indx = new_nodes.index(new_node)
                    if (indx == 0 or indx == len(new_nodes)) and new_node == "":
                        continue
                    if new_nodes.index(new_node) % 2 == 0:
                        res_node = TextNode(new_node, TextType.PLAIN_TEXT)
                    else:
                        link_extr = Extract.extract_markdown_images(new_node)
                        res_node = TextNode(link_extr[0][0], TextType.IMAGE, link_extr[0][1])
                    res_list.append(res_node)

        return res_list

    @staticmethod
    def split_nodes_links(old_nodes):
        if not old_nodes:
            raise ValueError("Nodes are missing!")

        res_list = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                res_list.append(node)
            else:
                patt = r"(\[(?:.*?)\]\((?:.*?)\))"
                new_nodes = re.split(patt, node.text)
                if len(new_nodes) == 1 and "](" not in new_nodes[0]:
                    res_list.append(node)
                    continue
                if len(new_nodes) < 3 or len(new_nodes) % 2 == 0: 
                    raise Exception("Invalid Markdown syntax!")
                for new_node in new_nodes:
                    indx = new_nodes.index(new_node)
                    if (indx == 0 or indx == len(new_nodes) - 1) and new_node == "":
                        continue
                    if new_nodes.index(new_node) % 2 == 0:
                        res_node = TextNode(new_node, TextType.PLAIN_TEXT)
                    else:
                        link_extr = Extract.extract_markdown_links(new_node)
                        res_node = TextNode(link_extr[0][0], TextType.LINK, link_extr[0][1])
                    res_list.append(res_node)

        return res_list

    @staticmethod
    def markdown_to_blocks(markdown):
        blocks = markdown.split("\n\n")
        trimmed_blocks = []

        for block in blocks:
            trimmed_blocks.append(block.strip())

        final_blocks = []
        for block in trimmed_blocks:
            if block != "":
                final_blocks.append(re.sub(r' {2,}', '', block))

        return final_blocks

    @staticmethod
    def split_text_block_to_list_blocks(block):
        if block == "":
            raise ValueError("List block is empty!")

        res_list = []
        patt = r"\n"
        litems = re.split(patt, block)
        for litem in litems:
            text = f"<li>{litem}</li>\n"
            res_node = TextNode(text, TextType.PLAIN_TEXT)
            res_list.append(res_node)

        return res_list


