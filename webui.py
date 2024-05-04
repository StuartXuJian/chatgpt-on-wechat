import os; 

import gradio as gr

def list_files(directory):
    """列出指定目录下的所有文件"""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def main():
    # 确保'./record'目录存在
    if not os.path.exists("./record"):
        os.makedirs("./record")
    
    # 列出/tmp目录下的所有文件
    files_list = list_files("./record")

    WEB_PORT = 18880

    with gr.Blocks(title=f"下载文件") as index:

        file_dropdown=gr.Dropdown(choices=files_list, label="选择文件"), 
        download_button = gr.DownloadButton("📂 点击下载", value = os.path.join("./record", file_dropdown))

    print(f"http://localhost:{WEB_PORT} Started...")
    index.queue(concurrency_count=10).launch(server_name="0.0.0.0", server_port=WEB_PORT)

if __name__ == "__main__":
    main()