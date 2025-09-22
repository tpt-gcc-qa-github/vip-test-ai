
from agentic_ai_connector.features.my_features import my_features
from agentic_ai_connector.competitors.scrape_competitors import scrape_lokalise, scrape_smartling

# Compare features
def compare():
    lokalise = scrape_lokalise()
    smartling = scrape_smartling()
    
    comparison = {
        "unique_to_me": [],
        "shared_with_lokalise": [],
        "shared_with_smartling": []
    }

    for feature in my_features:
        if feature in lokalise:
            comparison["shared_with_lokalise"].append(feature)
        elif feature in smartling:
            comparison["shared_with_smartling"].append(feature)
        else:
            comparison["unique_to_me"].append(feature)

    return comparison
