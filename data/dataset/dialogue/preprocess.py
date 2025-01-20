import json
import re

# interviewer にマッチするパターン
pattern_interviewer = re.compile(r"(interviewer:.*?\n\n)", re.DOTALL)
# imma にマッチするパターン
output_file = "output.json"

results = [] 
with open("dialogue_ja.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if not line:
            continue  # 空行をスキップ
        
        # 行を JSON として読み込む
        data = json.loads(line)

        # preprocessed_text を取得
        text = data.get("preprocessed_text", "")

        # 1) interviewer部分を抽出
        interviewer_matches = pattern_interviewer.findall(text)

        # 2) 抽出した interviewer部分 を元の text から削除
        text_removed = pattern_interviewer.sub("", text)
        
        # 3) 次に、imma部分を抽出
        imma_matches = [text_removed.replace("imma:","")]
        
        interviewer_text=interviewer_matches[0].replace("interviewer:","").strip()
        imma_text=imma_matches[0].strip()
        
        iterative = {
                "interviewer": interviewer_text,
                "imma": imma_text,
                "label": 1
            }
        
        results.append(iterative)
        print(iterative)
with open(output_file, "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print(f"完了: {len(results)} 件のデータを {output_file} に書き出しました。")