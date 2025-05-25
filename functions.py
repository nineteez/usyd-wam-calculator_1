import sys
import models

# Define learning outcomes and topic mappings here for use in logic
learning_outcomes = {
    'computer architecture': [
        'instruction sets', 'memory hierarchy', 'processor architecture',
        'cache replacement policies', 'number representations', 'basic assembly language'
    ],
    'network architecture and protocols': ['application level protocols', 'TCP', 'IP'],
    'IT management': [
        'ethics and professional responsibility', 'software testing', 'data security',
        'quality assurance', 'human resource management', 'change management',
        'SLDC', 'written & oral communication', 'conflict resolution',
        'research methods', 'IT tools'
    ],
    'DBMS': [
        'relational database design', 'transactions', 'SQL',
        'indexed databases', 'query optimisation'
    ],
    'innovation and invention': [
        'importance to a country', 'diffusion, adoption and maturity of innovation',
        'dominant design', 'Disruptive Innovation Model', 'capital and fundraising pathways'
    ],
    'project management in IT': ['knowledge, tools and techniques', 'team and management skills'],
    'machine learning and data mining': [
        'classification', 'clustering', 'decision trees', 'feature selection',
        'overfitting', 'cross-validation', 'unsupervised learning', 'supervised learning',
        'model evaluation'
    ],
    'introductory statistics for data science': [
        'sampling and probability', 'descriptive statistics', 'statistical inference',
        'confidence intervals', 'hypothesis testing', 'linear regression',
        'data visualization', 'categorical data analysis'
    ],
    'python programming': [
        'procedural programming', 'programming principles',
        'data types', 'variables and operators', 'control-flow',
        'functional programming', 'OOP programming'
    ]
}

unit_to_topic = {
    'INFO5990': ['IT management'],
    'COMP9120': ['DBMS'],
    'COMP9601': ['computer architecture', 'network architecture and protocols'],
    'INFO5992': ['innovation and invention'],
    'INFO6007': ['project management in IT'],
    'COMP9123': ['machine learning and data mining'],
    'STAT5002': ['introductory statistics for data science'],
    'COMP9001': ['python programming']
}

specialisation_to_units = {
    "Algorithms And Theory": ["COMP9101", "COMP9201"],
    "Cybersecurity": ["COMP9447", "COMP6445"],
    "Data Science And AI": ["COMP5310", "COMP5329"],
    "Digital Media": ["COMP5827", "COMP5424"],
    "Human Computer Interaction": ["COMP5456", "COMP5416"],
    "Networks And Distributed Systems": ["COMP5349", "COMP5415"],
    "Software Engineering": ["COMP5806", "COMP5045"]
}

def calculate_required_wam(student):
    stream = models.Stream(student.stream)
    required = stream.required_wam

    grades = {}
    while not grades:
        raw_grades = input("Enter your current subjects and pre-exam marks (e.g., COMP9601:75,COMP9120:68): ")
        entries = raw_grades.split(',')
        for pair in entries:
            try:
                unit, mark = pair.strip().split(':')
                grades[unit.strip().upper()] = float(mark.strip())
            except ValueError:
                print(f"⚠️ Invalid format for entry '{pair.strip()}'. Use format UNITCODE:MARK, e.g., COMP9601:75")
        if not grades:
            print("❌ No valid entries. Please try again.")

    student.grades = grades
    avg = sum(grades.values()) / len(grades)
    exam_weight = 0.5

    output_lines = []
    output_lines.append(f"\n🎯 Required WAM for {stream.name} stream: {required}")
    output_lines.append(f"📊 Your current average (pre-exam): {avg:.2f}")

    if student.semester == 1:
        exam_avg = (required - avg * (1 - exam_weight)) / exam_weight
        output_lines.append(f"You need an average of {exam_avg:.2f} in your final exams this semester.")
        output_lines.append(f"And you'll need an average of {required:.2f} in next semester's subjects.")

        output_lines.append("\n📚 Recommended areas to study based on your current subjects:")
        seen_units = set()
        for unit in grades:
            if unit in seen_units:
                continue
            seen_units.add(unit)
            topics = unit_to_topic.get(unit, [])
            for topic in topics:
                if topic in learning_outcomes:
                    output_lines.append(f"- {unit}: {', '.join(learning_outcomes[topic])}")

        spec_units = specialisation_to_units.get(student.specialisation, [])
        

    elif student.semester == 2:
        try:
            current_wam = float(input("Enter your current WAM: "))
        except ValueError:
            print("Invalid WAM input.")
            return

        exam_avg = (required * 2 - current_wam - avg * (1 - exam_weight)) / exam_weight
        output_lines.append(f"You need an average of {exam_avg:.2f} in your final exams to qualify for the {stream.name} stream.")

        output_lines.append("\n📚 Recommended areas to study based on your current units:")
        seen_units = set()
        for unit in grades:
            if unit in seen_units:
                continue
            seen_units.add(unit)
            topics = unit_to_topic.get(unit, [])
            for topic in topics:
                if topic in learning_outcomes:
                    output_lines.append(f"- {unit}: {', '.join(learning_outcomes[topic])}")
    else:
        output_lines.append("⚠️ Semester must be 1 or 2.")

    print('\n'.join(output_lines))
