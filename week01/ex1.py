from collections import defaultdict


def sums_by_category_loop(transactions: list[dict]) -> dict[str, int]:
    sums = defaultdict(int)
    for transaction in transactions:
        sums[transaction['category']] += transaction['amount']
    return dict(sums)

def sums_by_category_comp(transactions: list[dict]) -> dict[str, int]:
    return {
        category: sum(t['amount'] for t in transactions if t['category'] == category)
        for category in {t['category'] for t in transactions}
    }

def big_expenses(transactions: list[dict], threshold: int = 1000) -> list[dict]:
    return sorted([t for t in transactions if t['amount'] > threshold], key=lambda x: x['amount'], reverse=True)

def words(s: str) -> list[str]:
    s = s.replace(' ', ',')
    s = s.replace(';', ',')
    return [w for w in s.lower().split(',') if w]

def categories_set(transactions: list[dict]) -> set[str]:
    return {t['category'] for t in transactions}

def group_amounts_plain(transactions: list[dict]) -> dict[str, list[int]]:
    grouped = {}
    for transaction in transactions:
        grouped.setdefault(transaction['category'], [])
        grouped[transaction['category']].append(transaction['amount'])
    return grouped


def group_amounts_default(transactions: list[dict]) -> dict[str, list[int]]:
    grouped_transactions = defaultdict(list)
    for transaction in transactions:
        grouped_transactions[transaction['category']] = grouped_transactions[transaction['category']]
        grouped_transactions[transaction['category']].append(transaction['amount'])
    return grouped_transactions


if __name__ == '__main__':
    transactions = [
        {"category": "food", "amount": 1200},
        {"category": "taxi", "amount": 300},
        {"category": "food", "amount": 800},
        {"category": "rent", "amount": 40000},
        {"category": "food", "amount": 1500},
        {"category": "taxi", "amount": 450},
        {"category": "fun", "amount": 2000},
        {"category": "rent", "amount": 38000},
        {"category": "fun", "amount": 500},
        {"category": "salary", "amount": 150000},
    ]

    print(sums_by_category_comp(transactions))
    print(sums_by_category_loop(transactions))
    print(big_expenses(transactions, 30000))
    print(big_expenses(transactions))
    print(words(" ToП-3, категории; БАНКА "))
    print(categories_set(transactions))
    print(group_amounts_plain(transactions))
    print(group_amounts_default(transactions))

    assert sums_by_category_comp(transactions) == dict(sums_by_category_loop(transactions))
    assert group_amounts_plain(transactions) == dict(group_amounts_default(transactions))