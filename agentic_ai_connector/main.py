
from agentic_ai_connector.suggestions.generate import generate_suggestions

if __name__ == "__main__":
    suggestions = generate_suggestions()
    print("
Suggested Improvements:")
    for s in suggestions:
        print(f"- {s}")
