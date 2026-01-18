

SKILLS = {
        # =============================
    # FRONTEND EXTENSIONS
    # =============================
    "Redux": {"difficulty": 3, "market": 0.9, "time": 1},
    "Next.js": {"difficulty": 3, "market": 0.9, "time": 1.5},
    "Web Performance": {"difficulty": 4, "market": 0.85, "time": 1},

    # =============================
    # SOFTWARE ENGINEERING CORE
    # =============================
    "Design Patterns": {"difficulty": 4, "market": 1.0, "time": 1.5},
    "Data Structures & Algorithms": {"difficulty": 5, "market": 1.0, "time": 3},
    "Concurrency": {"difficulty": 5, "market": 0.9, "time": 2},
     # =============================,
    # SYSTEMS & LOW-LEVEL
    # =============================
    "C": {"difficulty": 4, "market": 0.85, "time": 2},
    "Memory Management": {"difficulty": 5, "market": 0.8, "time": 1.5},
    "Operating Systems": {"difficulty": 5, "market": 0.9, "time": 2},


    # =============================
    # CORE PROGRAMMING
    # =============================
    "Python": {"difficulty": 2, "market": 0.95, "time": 1},
    "Java": {"difficulty": 3, "market": 0.9, "time": 2},
    "JavaScript": {"difficulty": 2, "market": 1.0, "time": 1},
    "TypeScript": {"difficulty": 3, "market": 0.9, "time": 1},

    # =============================
    # FRONTEND
    # =============================
    "HTML/CSS": {"difficulty": 1, "market": 0.9, "time": 0.5},
    "React": {"difficulty": 3, "market": 1.0, "time": 2},

    # =============================
    # PYTHON BACKEND
    # =============================
    "FastAPI": {"difficulty": 3, "market": 0.85, "time": 1},
    "Django": {"difficulty": 3, "market": 0.8, "time": 2},
    "REST APIs": {"difficulty": 2, "market": 1.0, "time": 1},

    # =============================
    # JAVA BACKEND
    # =============================
    "OOP (Java)": {"difficulty": 2, "market": 0.9, "time": 1},
    "Spring": {"difficulty": 3, "market": 1.0, "time": 2},
    "Spring Boot": {"difficulty": 3, "market": 1.0, "time": 2},
    "Hibernate": {"difficulty": 3, "market": 0.85, "time": 1.5},
    "Java REST APIs": {"difficulty": 2, "market": 0.95, "time": 1},
    "Spring Security": {"difficulty": 4, "market": 0.9, "time": 1.5},

    # =============================
    # DATABASES
    # =============================
    "SQL": {"difficulty": 2, "market": 1.0, "time": 1},
    "PostgreSQL": {"difficulty": 3, "market": 0.95, "time": 1},
    "MySQL": {"difficulty": 2, "market": 0.9, "time": 1},
    "Redis": {"difficulty": 3, "market": 0.75, "time": 0.5},

    # =============================
    # DEVOPS & CLOUD
    # =============================
    "Git": {"difficulty": 1, "market": 1.0, "time": 0.5},
    "Docker": {"difficulty": 3, "market": 0.9, "time": 1},
    "Kubernetes": {"difficulty": 5, "market": 1.0, "time": 2},
    "AWS": {"difficulty": 4, "market": 1.0, "time": 2},
    "CI/CD": {"difficulty": 4, "market": 0.9, "time": 1},

    # =============================
    # ARCHITECTURE
    # =============================
    "System Design": {"difficulty": 5, "market": 1.0, "time": 3},
    "Microservices": {"difficulty": 5, "market": 0.9, "time": 2},
    "Microservices (Java)": {"difficulty": 5, "market": 0.9, "time": 2},

    # =============================
    # STREAMING & MESSAGING
    # =============================
    "Kafka": {"difficulty": 4, "market": 0.9, "time": 1.5},
    "RabbitMQ": {"difficulty": 3, "market": 0.7, "time": 1},

    # =============================
    # CORE CS & QUALITY
    # =============================
    "Testing": {"difficulty": 2, "market": 0.9, "time": 1},

    # =============================
    # ML / DATA
    # =============================
    "NumPy": {"difficulty": 1, "market": 0.9, "time": 0.5},
    "Pandas": {"difficulty": 2, "market": 0.9, "time": 1},
    "Scikit-learn": {"difficulty": 3, "market": 0.95, "time": 1.5},

    # =============================
    # DEEP LEARNING
    # =============================
    "TensorFlow": {"difficulty": 4, "market": 0.9, "time": 2},
    "PyTorch": {"difficulty": 4, "market": 1.0, "time": 2},
    "Neural Networks": {"difficulty": 4, "market": 1.0, "time": 2},
    "Deep Learning": {"difficulty": 5, "market": 1.0, "time": 3},

    # =============================
    # GEN AI
    # =============================
    "NLP": {"difficulty": 4, "market": 0.9, "time": 2},
    "Transformers": {"difficulty": 5, "market": 1.0, "time": 2},
    "LLMs": {"difficulty": 5, "market": 1.0, "time": 2},
    "Prompt Engineering": {"difficulty": 2, "market": 0.9, "time": 0.5},
    "Vector Databases": {"difficulty": 3, "market": 0.85, "time": 1},

    # =============================
    # MLOPS
    # =============================
    "Model Serving": {"difficulty": 4, "market": 0.85, "time": 1.5},
    "Data Pipelines": {"difficulty": 4, "market": 0.9, "time": 1.5}
}



ROLE_SKILLS = {

    # ==================================================
    # JUNIOR ROLES
    # ==================================================
    "Junior Backend Developer": {
        "experience": (0, 2),
        "skills": {
            "Python": 0.9,
            "FastAPI": 0.7,
            "SQL": 0.8,
            "PostgreSQL": 0.6,
            "Git": 0.9,
            "Testing": 0.6
        }
    },

    "Junior Java Backend Developer": {
        "experience": (0, 2),
        "skills": {
            "Java": 1.0,
            "OOP (Java)": 0.9,
            "Spring Boot": 0.6,
            "Java REST APIs": 0.7,
            "SQL": 0.7,
            "Git": 0.9
        }
    },

    # ==================================================
    # MID-LEVEL ROLES
    # ==================================================
    "Backend Developer": {
        "experience": (2, 4),
        "skills": {
            "Python": 1.0,
            "FastAPI": 0.9,
            "SQL": 0.9,
            "PostgreSQL": 0.8,
            "Redis": 0.6,
            "Docker": 0.7,
            "CI/CD": 0.6,
            "Git": 1.0,
            "Testing": 0.8
        }
    },

    "Java Backend Developer": {
        "experience": (2, 4),
        "skills": {
            "Java": 1.0,
            "Spring Boot": 1.0,
            "Hibernate": 0.8,
            "Java REST APIs": 1.0,
            "SQL": 0.9,
            "Redis": 0.6,
            "Docker": 0.7,
            "Git": 1.0,
            "Testing": 0.8
        }
    },

    "Full Stack Developer": {
        "experience": (2, 4),
        "skills": {
            "Python": 0.8,
            "JavaScript": 1.0,
            "React": 0.9,
            "FastAPI": 0.8,
            "TypeScript": 0.8,
            "HTML/CSS": 0.9,
            "SQL": 0.9,
            "PostgreSQL": 0.8,
            "Docker": 0.7,
            "Git": 1.0,
            "Testing": 0.8
        }
    },

    # ==================================================
    # SENIOR ROLES
    # ==================================================
    "Senior Backend Developer": {
        "experience": (4, 7),
        "skills": {
            "Python": 1.0,
            "FastAPI": 0.9,
            "SQL": 1.0,
            "PostgreSQL": 0.9,
            "Redis": 0.8,
            "Docker": 0.8,
            "CI/CD": 0.8,
            "AWS": 0.8,
            "System Design": 1.0,
            "Microservices": 0.9,
            "Git": 1.0,
            "Testing": 0.9
        }
    },

    "Senior Java Backend Engineer": {
        "experience": (4, 7),
        "skills": {
            "Java": 1.0,
            "Spring Boot": 1.0,
            "Hibernate": 0.9,
            "Java REST APIs": 1.0,
            "Microservices (Java)": 0.9,
            "Kafka": 0.8,
            "Redis": 0.8,
            "Docker": 0.8,
            "Kubernetes": 0.6,
            "AWS": 0.8,
            "CI/CD": 0.8,
            "System Design": 1.0,
            "Spring Security": 0.8,
            "Git": 1.0,
            "Testing": 0.9
        }
    },

    "Senior Full Stack Developer": {
        "experience": (3, 5),
        "skills": {
            "Python": 0.9,
            "FastAPI": 0.8,
            "JavaScript": 1.0,
            "React": 1.0,
            "TypeScript": 0.9,
            "HTML/CSS": 0.8,
            "SQL": 1.0,
            "PostgreSQL": 0.9,
            "Redis": 0.7,
            "Docker": 0.8,
            "Kubernetes": 0.6,
            "AWS": 0.9,
            "CI/CD": 0.7,
            "System Design": 1.0,
            "Microservices": 0.8,
            "Testing": 0.8,
            "Git": 1.0
        }
    },

    # ==================================================
    # DATA / ANALYST ROLES
    # ==================================================
    "Data Analyst": {
        "experience": (1, 3),
        "skills": {
            "Python": 0.8,
            "SQL": 1.0,
            "Pandas": 0.9,
            "Testing": 0.5,
            "Git": 0.6
        }
    },

    # ==================================================
    # ML / AI ROLES
    # ==================================================
    "Machine Learning Engineer": {
        "experience": (2, 5),
        "skills": {
            "Python": 1.0,
            "NumPy": 0.9,
            "Pandas": 0.9,
            "Scikit-learn": 1.0,
            "SQL": 0.7,
            "Docker": 0.7,
            "AWS": 0.7,
            "CI/CD": 0.6,
            "Git": 1.0,
            "Testing": 0.7
        }
    },

    "Deep Learning Engineer": {
        "experience": (3, 6),
        "skills": {
            "Python": 1.0,
            "PyTorch": 1.0,
            "TensorFlow": 0.8,
            "Neural Networks": 1.0,
            "Deep Learning": 1.0,
            "Docker": 0.8,
            "AWS": 0.8,
            "Model Serving": 0.7,
            "Git": 1.0
        }
    },

    "Generative AI Engineer": {
        "experience": (3, 6),
        "skills": {
            "Python": 1.0,
            "PyTorch": 1.0,
            "Transformers": 1.0,
            "LLMs": 1.0,
            "Prompt Engineering": 0.9,
            "Vector Databases": 0.8,
            "NLP": 0.8,
            "Docker": 0.8,
            "AWS": 0.8,
            "Model Serving": 0.9,
            "Git": 1.0
        }
    },

    "MLOps Engineer": {
        "experience": (3, 6),
        "skills": {
            "Python": 0.8,
            "Docker": 1.0,
            "AWS": 1.0,
            "CI/CD": 0.9,
            "Model Serving": 0.9,
            "Data Pipelines": 0.8,
            "System Design": 0.8,
            "Git": 1.0
        }
    },
    # ==================================================
# DATA SCIENTIST ROLES
# ==================================================

"Junior Data Scientist": {
    "experience": (0, 2),
    "skills": {
        "Python": 0.9,
        "NumPy": 0.8,
        "Pandas": 0.9,
        "SQL": 0.7,
        "Testing": 0.5,
        "Git": 0.6
    }
},

"Data Scientist": {
    "experience": (2, 4),
    "skills": {
        "Python": 1.0,
        "NumPy": 0.9,
        "Pandas": 1.0,
        "Scikit-learn": 1.0,
        "SQL": 0.8,
        "Git": 0.8,
        "Testing": 0.7
    }
},

"Senior Data Scientist": {
    "experience": (4, 7),
    "skills": {
        "Python": 1.0,
        "NumPy": 1.0,
        "Pandas": 1.0,
        "Scikit-learn": 1.0,
        "Deep Learning": 0.8,
        "System Design": 0.7,
        "SQL": 0.8,
        "Git": 1.0,
        "Testing": 0.8
    }
},
# ==================================================
# SOFTWARE DEVELOPER ROLES
# ==================================================

"Junior Software Developer": {
    "experience": (0, 2),
    "skills": {
        "Python": 0.7,
        "Java": 0.7,
        "JavaScript": 0.6,
        "SQL": 0.6,
        "Git": 0.9,
        "Testing": 0.6
    }
},

"Software Developer": {
    "experience": (2, 4),
    "skills": {
        "Python": 0.9,
        "Java": 0.9,
        "JavaScript": 0.8,
        "REST APIs": 0.8,
        "SQL": 0.8,
        "Docker": 0.6,
        "Git": 1.0,
        "Testing": 0.8
    }
},

"Senior Software Developer": {
    "experience": (4, 7),
    "skills": {
        "Python": 1.0,
        "Java": 1.0,
        "JavaScript": 0.9,
        "REST APIs": 1.0,
        "System Design": 1.0,
        "Microservices": 0.9,
        "Docker": 0.8,
        "CI/CD": 0.8,
        "Git": 1.0,
        "Testing": 0.9
    }
},
# ==================================================
# SOFTWARE ENGINEER ROLES
# ==================================================

"Junior Software Engineer": {
    "experience": (0, 2),
    "skills": {
        "Python": 0.7,
        "Java": 0.7,
        "JavaScript": 0.6,
        "SQL": 0.6,
        "Git": 0.9,
        "Testing": 0.6
    }
},

"Software Engineer": {
    "experience": (2, 4),
    "skills": {
        "Python": 0.9,
        "Java": 0.9,
        "JavaScript": 0.8,
        "REST APIs": 0.8,
        "SQL": 0.8,
        "Docker": 0.6,
        "Git": 1.0,
        "Testing": 0.8
    }
},

"Senior Software Engineer": {
    "experience": (4, 7),
    "skills": {
        "Python": 1.0,
        "Java": 1.0,
        "JavaScript": 0.9,
        "REST APIs": 1.0,
        "System Design": 1.0,
        "Microservices": 0.9,
        "Docker": 0.8,
        "CI/CD": 0.8,
        "AWS": 0.8,
        "Git": 1.0,
        "Testing": 0.9
    }
}
,
# ==================================================
# FRONTEND ENGINEER ROLES
# ==================================================

"Junior Frontend Engineer": {
    "experience": (0, 2),
    "skills": {
        "HTML/CSS": 1.0,
        "JavaScript": 0.9,
        "React": 0.7,
        "Git": 0.8,
        "Testing": 0.5
    }
},

"Frontend Engineer": {
    "experience": (2, 4),
    "skills": {
        "HTML/CSS": 1.0,
        "JavaScript": 1.0,
        "React": 1.0,
        "TypeScript": 0.8,
        "Redux": 0.7,
        "Git": 1.0,
        "Testing": 0.7
    }
},

"Senior Frontend Engineer": {
    "experience": (4, 7),
    "skills": {
        "HTML/CSS": 1.0,
        "JavaScript": 1.0,
        "React": 1.0,
        "TypeScript": 1.0,
        "Redux": 0.9,
        "Next.js": 0.8,
        "Web Performance": 0.9,
        "System Design": 0.8,
        "Git": 1.0,
        "Testing": 0.9
    }
}


}
