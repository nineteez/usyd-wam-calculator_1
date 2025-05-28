import sys
import models

# Define learning outcomes and topic mappings for program development
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
# Define topic mappings for program development
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

# Define topic mappings for program development
# specialisation_to_units = {
#     "Algorithms And Theory": ["COMP9101", "COMP9201"],
#     "Cybersecurity": ["COMP9447", "COMP6445"],
#     "Data Science And AI": ["COMP5310", "COMP5329"],
#     "Digital Media": ["COMP5827", "COMP5424"],
#     "Human Computer Interaction": ["COMP5456", "COMP5416"],
#     "Networks And Distributed Systems": ["COMP5349", "COMP5415"],
#     "Software Engineering": ["COMP5806", "COMP5045"]
# }

def handle_exit():
    print("👋 Exiting the program. Goodbye!")
    sys.exit()

