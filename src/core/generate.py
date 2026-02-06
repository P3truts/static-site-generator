import os, shutil
from src.core.transform import Transform
from src.core.extract import Extract

class Generate:
    @staticmethod
    def move_files(src_dir, dest_dir):
        if os.path.exists(src_dir) and os.path.isdir(src_dir):
            print(f"The source {src_dir} directory exists!")
        else:
            raise FileNotFoundError(f"The source {src_dir} directory does not exist!")

        if os.path.exists(dest_dir) and os.path.isdir(dest_dir):
            print(f"The destination {dest_dir} directory exists!")
            if "/" not in src_dir:
                shutil.rmtree(dest_dir)
                os.mkdir(dest_dir)
                print(f"The destination {dest_dir} has been recreated!")
            for item in os.listdir(src_dir):
                item_path = os.path.join(src_dir, item)
                if os.path.isfile(item_path):
                    shutil.copy(item_path, dest_dir)
                else:
                    dest_path = os.path.join(dest_dir, item)
                    Generate.move_files(item_path, dest_path)
            print(f"Files from the source {src_dir} directory have been copied to the destination {dest_dir} directory!")
        else:
            os.mkdir(dest_dir)
            for item in os.listdir(src_dir):
                item_path = os.path.join(src_dir, item)
                if os.path.isfile(item_path):
                    shutil.copy(item_path, dest_dir)
                else:
                    dest_path = os.path.join(dest_dir, item)
                    Generate.move_files(item_path, dest_path)
            print(f"Files from the source {src_dir} directory have been copied to the destination {dest_dir} directory!")

    @staticmethod
    def generate_page(from_path, template_path, dest_path, basepath):
        print(f"Generating page from source '{from_path}' to destination '{dest_path}' using the template '{template_path}'!")

        src_file_cont = ""
        if os.path.exists(from_path) and os.path.isfile(from_path):
            with open(from_path, 'r') as f:
                src_file_cont = f.read()
        else:
            raise FileNotFoundError(f"File not found or directory at path '{from_path}'!")

        templ_file_cont = ""
        if os.path.exists(template_path) and os.path.isfile(template_path):
            with open(template_path, 'r') as t:
                templ_file_cont = t.read()
        else:
            raise FileNotFoundError(f"File not found or directory at path '{template_path}'!")

        html_node = Transform.markdown_to_html_node(src_file_cont)
        html_text = html_node.to_html()

        title = Extract.extract_title(src_file_cont)

        templ_file_cont = templ_file_cont.replace("{{ Title }}", title)
        templ_file_cont = templ_file_cont.replace("{{ Content }}", html_text)
        templ_file_cont = templ_file_cont.replace("href=\"/", f"href=\"{basepath}")
        templ_file_cont = templ_file_cont.replace("src=\"/", f"src=\"{basepath}")


        # overwrites existing html page
        with open(dest_path, 'w') as p:
            p.write(templ_file_cont)

        print(f"Static site page '{dest_path}' generated!")

    @staticmethod
    def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
        print(f"Generating pages recursively from source '{dir_path_content}' to destination '{dest_dir_path}' using the template '{template_path}'!")

        if os.path.exists(dir_path_content) and os.path.isdir(dir_path_content):
            print(f"The source {dir_path_content} directory exists!")
        else:
            raise FileNotFoundError(f"The source {dir_path_content} directory does not exist!")

        if os.path.exists(dest_dir_path) and os.path.isdir(dest_dir_path):
            print(f"The source {dest_dir_path} directory exists!")
        else:
            os.mkdir(dest_dir_path)
            if not os.path.exists(dest_dir_path):
                raise FileNotFoundError(f"The source {dest_dir_path} directory does not exist!")

        for item in os.listdir(dir_path_content):
            item_path = os.path.join(dir_path_content, item)
            if os.path.isfile(item_path) and item_path.endswith(".md"):
                html_item_dest = os.path.join(dest_dir_path, item)
                html_item_path = html_item_dest.replace(".md", ".html")
                print(f"Generating page {item_path}!")
                Generate.generate_page(item_path, template_path, html_item_path, basepath)
            else:
                if os.path.isdir(item_path):
                    dest_path = os.path.join(dest_dir_path, item)
                    print(f"Directory {item_path} found! Moving inside to check for pages!")
                    Generate.generate_pages_recursive(item_path, template_path, dest_path, basepath)
        print(f"Pages from the source {dir_path_content} directory have been created to the destination {dest_dir_path} directory!")

