states = [
    {"name": "SP", "billing": 67836.43},
    {"name": "RJ", "billing": 36678.66},
    {"name": "MG", "billing": 29229.88},
    {"name": "ES", "billing": 27165.48},
    {"name": "Outros", "billing": 19849.53},
]

def get_states_percentage(states):
    total = sum(state["billing"] for state in states)
    percentages = []
    for state in states:
        state["percentage"] = round((state["billing"] / total * 100), 2)
        percentages.append({ "name": state["name"], "percentage": f"{state['percentage']}%" })
    return percentages

def print_states_billing(states):
    for state in states:
        print(f"Estado: {state['name']} - Faturamento: R$ {state['billing']}")

def print_states_percentage(states):
    for state in states:
        print(f"Estado: {state['name']} - Porcentagem: {state['percentage']}")


if __name__ == "__main__":
    percentages = get_states_percentage(states)
    print_states_billing(states)
    print(f"\nFaturamento total: R$ {round((sum(state['billing'] for state in states)), 2)}\n")
    print_states_percentage(percentages)
        