import os
import json
from utils import analyze_data

def main():
    workflow_file = os.path.join(os.path.dirname(__file__), '../workflow.json')

    if not os.path.exists(workflow_file):
        print(f"Error: Workflow file '{workflow_file}' not found.")
        return

    print("Starting the social media performance analysis workflow...")

    # Load workflow configuration
    with open(workflow_file, "r") as file:
        workflow = json.load(file)

    # Analyze data based on the workflow
    result = analyze_data(workflow)

    # Display results
    print("\nAnalysis Complete. Results:")
    for key, value in result.items():
        print(f"{key}: {value}")

    # Save results to a file
    results_file = os.path.join(os.path.dirname(__file__), '../results.json')
    with open(results_file, "w") as result_file:
        json.dump(result, result_file, indent=4)
        print(f"\nResults saved to '{results_file}'.")

if __name__ == "__main__":
    main()
