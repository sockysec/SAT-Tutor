def print_ascii_art():
    art = '''
   
   _____ ___  ______  ______      __            
  / ___//   |/_  __/ /_  __/_  __/ /_____  _____
  \__ \/ /| | / /_____/ / / / / / __/ __ \/ ___/
 ___/ / ___ |/ /_____/ / / /_/ / /_/ /_/ / /    
/____/_/  |_/_/     /_/  \__,_/\__/\____/_/     
                                               
This is a python script to guide analysts in the application of Structured Analytical Techniques (SATs) for intelligence analysis.
    
When a user is ready to move to the next section, they should type ‘done’ on a new line and hit enter.
    
    '''
    print(art)


# Call the function to print the ASCII art
print_ascii_art()


# Rest of your script goes here...

def prompt_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "done":
            break
        lines.append(line)
    return lines


def print_report(brief, hypothesis, evidence, assumptions, alternate_explanations):
    print("\n--- Report ---")
    print(f"Brief: {brief}")
    print(f"\nHypothesis: {hypothesis}")
    print("\nEvidenced by:")
    for line in evidence:
        print(f"- {line}")
    print("\nAssumptions:")
    for line in assumptions:
        print(f"- {line}")
    print("\nAlternate Explanations:")
    for line in alternate_explanations:
        print(f"- {line}")


def main():
    # Describe the current situation
    current_situation = prompt_input("Describe the current situation?")

    # What is your current leading hypothesis?
    leading_hypothesis = prompt_input("What is your current leading hypothesis?")

    # What assumptions are you making?
    assumptions = prompt_input("What assumptions are you making?")

    # Are there any alternative explanations for this?
    alternative_explanations = prompt_input("Are there any alternative explanations for this?")

    # Based on this, now list all possible hypotheses.
    possible_hypotheses = prompt_input("Based on this, now list all possible hypotheses.")

    # Input the evidence that supports the following hypotheses.
    hypotheses_evidence = {}
    for hypothesis in possible_hypotheses:
        evidence = prompt_input(
            f"Input the evidence that supports the hypothesis: '{hypothesis}'"
        )
        hypotheses_evidence[hypothesis] = evidence

    # Which hypothesis is currently most supported by the evidence?
    print("\n--- Select Leading Hypothesis ---")
    for i, hypothesis in enumerate(possible_hypotheses):
        print(f"{i + 1}. {hypothesis}")
        print("   Evidence:")
        for line in hypotheses_evidence[hypothesis]:
            print(f"   - {line}")

    selection = input("Enter the number of the most supported hypothesis: ")
    selected_hypothesis = possible_hypotheses[int(selection) - 1]

    # Print report
    print_report('\n'.join(current_situation), selected_hypothesis, hypotheses_evidence[selected_hypothesis],
                 assumptions, alternative_explanations)

    # Ask if user wants to print the report
    print_report_option = input("\nPrint report? (Y/N): ")
    if print_report_option.upper() == 'Y':
        print_report('\n'.join(current_situation), selected_hypothesis, hypotheses_evidence[selected_hypothesis],
                     assumptions, alternative_explanations)
    else:
        print("Report not printed.")


if __name__ == "__main__":
    main()
