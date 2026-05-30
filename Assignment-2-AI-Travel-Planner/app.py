import json

with open("knowledge_base.json") as f:
    data = json.load(f)

budget = input("Budget (low/medium/high): ")
activity = input("Preferred activity: ")

recommendations = []

for place in data["destinations"]:
    if place["budget"] == budget:
        if activity in place["activities"]:
            recommendations.append(place["name"])

if recommendations:
    print("\nRecommended Destinations:")
    for r in recommendations:
        print("-", r)
else:
    print("No matching destinations found.")
