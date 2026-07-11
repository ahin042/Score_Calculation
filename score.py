def score_input(name):
    while True:
        value = input(f"  - {name} 점수 (안 쳤음 = X): ").strip()
        if value.lower() == "x":
            return None
        try:
            score = float(value)
            if 0 <= score <= 100:
                return score
            print("    0~100 사이로 입력")
        except ValueError:
            print("    숫자 또는 X로 입력")

def weight_input(name):
    while True:
        value = input(f"  - {name} 비중(%): ").strip()
        try:
            weight = float(value)
            if weight >= 0:
                return weight
            print("    0 이상으로 입력")
        except ValueError:
            print("    숫자로 입력")

def main():
    subject = input("과목 이름 : ").strip()
    while True:
        try:
            count = int(input("항목 수(ex 수행1 / 수행 / 중간 / 기말 = 4): ").strip())
            if count > 0:
                break
            print("1개 이상 입력")
        except ValueError:
            print("숫자로 입력")
    items = []
    for i in range(count):
        print(f"\n[{i + 1}번째 항목]")
        name = input("  - 항목 이름 (ex. 중간고사): ").strip()
        weight = weight_input(name)
        score = score_input(name)
        items.append({"name": name, "weight": weight, "score": score})
    weight_sum = sum(item["weight"] for item in items)
    if weight_sum != 100:
        print(f"\n입력한 비중의 합 : {weight_sum}%")
    print("\n" + "=" * 40)
    print(f"  [{subject}]")
    print("-" * 40)
    total = 0
    for item in items:
        if item["score"] is None:
            print(f"  {item['name']}: 아직 안 침 = 0점 (비중 {item['weight']}%)")
        else:
            converted = item["score"] / 100 * item["weight"]
            total += converted
            print(f"  {item['name']}: {item['score']}점 × {item['weight']}% = {converted:.2f}점")
    print("-" * 40)
    result = int(total) if total == int(total) else round(total, 2)
    print(f"  총점 : {result}점")
    print("-" * 40)

print("=" * 40)
print(" " * 13 + "과목 점수 계산기")
print("=" * 40)
main()