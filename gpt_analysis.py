import openai

openai.api_key = "sk-svcacct-ljr59NWBz9KjLUjK_k07raalbnCsKthflHad9Oy7fzUepy4s-_snEKhJ-qT6TR2oR4T3BlbkFJdFXtS8qNHGEBNNd7D5PawgPFl3nghrGmgPq-7tDECkpfTxwZxItgoVCX0x5dZIhFwA"  # Thay bằng API Key của bạn

def analyze_content(content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Bạn là một chuyên gia phân tích tài chính."},
            {"role": "user", "content": f"Phân tích báo cáo tài chính sau:\n{content}"}
        ],
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']
