def load_faq(filepath="faq.txt"):
    faq = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, val = line.split(":", 1)
                faq[key.strip().lower()] = val.strip()
    return faq

def main():
    faq = load_faq()
    print("=== Чат-бот репетиции запущен (напишите 'exit' для выхода) ===")
    
    while True:
        query = input("\nВы: ").strip().lower()
        if query == "exit":
            break
            
        answer = "не знаю"
        for key, val in faq.items():
            if key in query:
                answer = val
                break
                
        print(f"Бот: {answer}")

if __name__ == "__main__":
    main()