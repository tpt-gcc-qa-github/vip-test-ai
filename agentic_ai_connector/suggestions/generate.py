
from agentic_ai_connector.utils.compare_features import compare

# Placeholder for LLM integration (e.g., Ollama)
def generate_suggestions():
    comparison = compare()
    
    suggestions = []
    if comparison["unique_to_me"]:
        suggestions.append("Highlight unique features in marketing and documentation.")
    if not comparison["shared_with_lokalise"]:
        suggestions.append("Consider adding features similar to Lokalise for better parity.")
    if not comparison["shared_with_smartling"]:
        suggestions.append("Explore Smartling's AI tools and consider integration.")

    return suggestions
