import os; 

import gradio as gr

def list_files(directory):
    """列出指定目录下的所有文件"""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def download_selected_file(file_name):
    """根据用户选择的文件名，返回文件以供下载"""
    file_path = os.path.join("./record", file_name)
    return file_path

def main():

    # 列出/tmp目录下的所有文件
    files_list = list_files("./record")

    # 创建 Gradio 接口
    iface = gr.Interface(
        fn=download_selected_file,
        inputs=gr.inputs.Dropdown(choices=files_list, label="选择文件"),  # 使用下拉菜单选择文件
        outputs=gr.outputs.File(label="下载文件"),  # 输出为可下载的文件
        title="下载目录下的文件",
        description="从下拉菜单中选择一个文件进行下载。"
    )

    WEB_PORT = 18880
    iface.launch(server_port=WEB_PORT, share=True)
    print(f"http://localhost:{WEB_PORT} Started...")

if __name__ == "__main__":
    main()