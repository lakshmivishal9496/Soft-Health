questions = [
    {
        'question': 'You feel more energetic when:',
        'options': ['Socializing with others', 'Spending time alone'],
        'traits': ['E', 'I']
    },
    {
        'question': 'You focus more on:',
        'options': ['Facts and details', 'Big picture and possibilities'],
        'traits': ['S', 'N']
    },
    {
        'question': 'You usually make decisions based on:',
        'options': ['Logical analysis', 'Personal values and emotions'],
        'traits': ['T', 'F']
    },
    {
        'question': 'You prefer:',
        'options': ['A structured and organized lifestyle',
                    'A spontaneous and flexible lifestyle'],
        'traits': ['J', 'P']
    }

]


personality_list = {
    "ISTJ": "Introverted, Sensing, Thinking, Judging",
    "ISFJ": "Introverted, Sensing, Feeling, Judging",
    "INFJ": "Introverted, Intuitive, Feeling, Judging",
    "INTJ": "Introverted, Intuitive, Thinking, Judging",
    "ISTP": "Introverted, Sensing, Thinking, Perceiving",
    "ISFP": "Introverted, Sensing, Feeling, Perceiving",
    "INFP": "Introverted, Intuitive, Feeling, Perceiving",
    "INTP": "Introverted, Intuitive, Thinking, Perceiving",
    "ESTP": "Extroverted, Sensing, Thinking, Perceiving",
    "ESFP": "Extroverted, Sensing, Feeling, Perceiving",
    "ENFP": "Extroverted, Intuitive, Feeling, Perceiving",
    "ENTP": "Extroverted, Intuitive, Thinking, Perceiving",
    "ESTJ": "Extroverted, Sensing, Thinking, Judging",
    "ESFJ": "Extroverted, Sensing, Feeling, Judging",
    "ENFJ": "Extroverted, Intuitive, Feeling, Judging",
    "ENTJ": "Extroverted, Intuitive, Thinking, Judging"
}


personality_recommendation = {
    "ISTJ": "Practice adaptability,\
    embrace change, and explore creative problem-solving. \
    Make time for leisure and social activities\
    to balance work and personal life.\
    <br>(Costa Jr, P. T., & McCrae, R. R. (1992).\
    Revised NEO Personality Inventory (NEO-PI-R) and\
    NEO Five-Factor Inventory (NEO-FFI) manual.\
    Psychological Assessment Resources.)",
    "ISFJ": "Develop assertiveness, set boundaries, and\
    engage in self-care practices.\
    Explore new experiences and ideas to expand perspectives.\
    <br>(Judge, T. A., & Bono, J. E. (2001).\
    Relationship of core self-evaluations traits--self-esteem,\
    generalized self-efficacy, locus of control, and emotional stability\
    --with job satisfaction and job performance: A meta-analysis.\
    Journal of Applied Psychology, 86(1), 80-92.)",
    "ISFJ": "Develop assertiveness, set boundaries, and engage \
    in self-care practices. Explore new experiences and ideas \
    to expand perspectives. <br>(Judge, T. A., & Bono, J. E. (2001).\
    Relationship of core self-evaluations traits--self-esteem,\
    generalized self-efficacy, locus of control, and emotional\
    stability--with job satisfaction and job performance:\
    A meta-analysis. Journal of Applied Psychology, 86(1), 80-92.)",
    "INFJ": "Prioritize self-care and set boundaries to avoid burnout.\
    Practice open-mindedness and engage in activities that promote\
    self-awareness and self-growth. <br>(Ashton, M. C., & Lee, K. (2009).\
    The HEXACO-60: A short measure of the major dimensions of personality.\
    Journal of Personality Assessment, 91(4), 340-345.)",
    "INTJ": "Develop emotional intelligence, practice empathy, and \
    engage in team-building activities to strengthen social connections.\
    Balance intellectual pursuits with physical exercise and relaxation.\
    <br>(Goleman, D. (1995). Emotional intelligence. Bantam Books.)",
    "ISTP": "Cultivate long-term goals, practice time management,\
    and develop organizational skills. Engage in social activities\
    and build a support network. <br>(Macan, T. H.,\
    Shahani, C., Dipboye, R. L., & Phillips, A. P. (1990).\
    College students' time management: Correlations with \
    academic performance and stress. Journal of Educational \
    Psychology, 82(4), 760-768.)",
    "ISFP": "Develop assertiveness, practice communication skills,\
    and set personal goals. Engage in creative pursuits and\
    explore new experiences.\
    <br>(Riggio, R. E., & Reichard, R. J. (2008).\
    The emotional and social intelligences of effective\
    leadership: An emotional and social skill approach.\
    Journal of Managerial Psychology, 23(2), 169-185.)",
    "INFP": "Set realistic goals, develop practical skills, and \
    practice self-compassion. Engage in mindfulness and stress\
    management techniques. <br>(Neff, K. D. (2011).\
    Self-compassion, self-esteem, and well-being.\
    Social and Personality Psychology Compass, 5(1), 1-12.)",
    "INTP": "Develop emotional intelligence, practice active listening,\
    and engage in social activities. Balance intellectual\
    interests with physical exercise and self-care.\
    <br>(Goleman, D. (1995). Emotional intelligence. Bantam Books.)",
    "ESTP": "Develop long-term goals, practice patience,\
    and engage in mindfulness techniques. Cultivate deeper\
    connections through meaningful conversations.\
    <br>(Kabat-Zinn, J. (2003). \
    Mindfulness-based interventions in context:\
    past, present, and future. Clinical Psychology: \
    Science and Practice, 10(2), 144-156.)",
    "ESFP": "Develop time management and organizational skills,\
    and set personal goals. Engage in activities that promote\
    self-reflection and personal growth.\
    <br>(Macan, T. H., Shahani,\
    C.,Dipboye, R. L., & Phillips, A. P. (1990).\
    College students' time management: Correlations with\
    academic performance and stress. Journal of Educational Psychology, 82(4), 760-768.)",
    "ENFP": "Practice setting boundaries, develop self-discipline,\
    and work on follow-through. Engage in relaxation techniques\
    and mindfulness to manage stress. \
    <br>(Kabat-Zinn, J. (2003).\
    Mindfulness-based interventions in context: past,\
    present, and future.\
    Clinical Psychology: Science and Practice, 10(2), 144-156.)",
    "ENTP": "Develop active listening skills, practice empathy, \
    and cultivate emotional intelligence.\
    Balance exploration of new ideas with self-care\
    and relaxation. <br>(Goleman, D. (1995).\
    Emotional intelligence. Bantam Books.)",
    "ESTJ": "Develop flexibility, practice empathy,\
    and engage in open-minded discussions. Balance work\
    and personal life by making time for leisure activities\
    and self-care. <br>(Goleman, D. (1995).\
    Emotional intelligence. Bantam Books.)",
    "ESFJ": "Practice self-compassion, develop assertiveness,\
    and set boundaries. Engage in activities that\
    promote self-awareness and personal growth. \
    <br>(Neff, K. D. (2011). Self-compassion,\
    self-esteem, and well-being. Social and Personality Psychology\
    Compass, 5(1), 1-12.)",
    "ENFJ": "Prioritize self-care, set personal boundaries,\
    and avoid overcommitting. Engage in stress management\
    techniques and relaxation activities. \
    <br>(Kabat-Zinn, J. (2003).\
    Mindfulness-based interventions in \
    context: past, present, and future.\
    Clinical Psychology: Science and Practice, 10(2), 144-156.)",
    "ENTJ": "Develop emotional intelligence, practice active listening,\
    and engage in team-building activities. Balance work and\
    personal life with leisure activities and self-care. \
    (Goleman, D. (1995). Emotional intelligence. Bantam Books.)"
}

personality_quote = {
    "ISTJ": "Integrity is doing the right thing, even when no one is watching. - C.S. Lewis",
    "ISFJ": "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "INFJ": "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "INTJ": "The only way to do great work is to love what you do. - Steve Jobs",
    "ISTP": "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "ISFP": "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "INFP": "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. - Ralph Waldo Emerson",
    "INTP": "Genius is one percent inspiration and ninety-nine percent perspiration. - Thomas Edison",
    "ESTP": "Life is either a daring adventure or nothing at all. - Helen Keller",
    "ESFP": "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "ENFP": "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "ENTP": "I am not afraid of storms, for I am learning how to sail my ship. - Louisa May Alcott",
    "ESTJ": "Success in any endeavor requires single-minded attention to detail and total concentration. - Willie Sutton",
    "ESFJ": "We must learn to live together as brothers or perish together as fools. - Martin Luther King Jr.",
    "ENFJ": "Leadership is not about being in charge. It's about taking care of those in your charge. - Simon Sinek",
    "ENTJ": "If you want to go fast, go alone. If you want to go far, go together. - African proverb."
}




