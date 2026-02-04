from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, database

app = FastAPI(title="Ritesh Karki - Me-API Playground")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/profile")
def get_profile(db: Session = Depends(database.get_db)):
    return db.query(models.Profile).first()

@app.get("/projects")
def list_projects(skill: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Project)
    if skill:
        query = query.filter(models.Project.tech_stack.contains(skill.capitalize()))
    return query.all()

@app.get("/skills/top")
def get_top_skills(db: Session = Depends(database.get_db)):
    profile = db.query(models.Profile).first()
    return {"top_skills": profile.skills[:5]}

# Seeding logic with new B.Com + AI Projects
def seed_data():
    db = database.SessionLocal()
    # Check if data already exists to avoid duplicates
    if not db.query(models.Profile).first():
        ritesh = models.Profile(
            name="Ritesh Karki",
            email="karkiritesh11@gmail.com",
            education=[{"school": "IIT Mandi", "degree": "MBA - DS & AI"}],
            skills=["Python", "SQL", "Machine Learning", "FastAPI", "Financial Modeling"],
            links={"github": "https://github.com/Riteshkarki11", "linkedin": "https://www.linkedin.com/in/ritesh-karki"}
        )
        
        # New B.Com + AI projects
        new_projects = [
            models.Project(
                title="AI Tax Compliance Auditor",
                description="Automating tax savings identification using NLP on financial records from Anand Tax Solutions.",
                tech_stack=["NLP", "Python", "TaxTech"],
                links="https://github.com/Riteshkarki11"
            ),
            models.Project(
                title="Intelligent Insurance Risk Profiler",
                description="ML model to generate customized insurance quotes based on client risk assessments.",
                tech_stack=["ML", "Python", "Scikit-Learn"],
                links="https://github.com/Riteshkarki11"
            ),
            models.Project(
                title="Automated Ledger Anomaly Detector",
                description="Detecting fraudulent entries in accounting datasets using unsupervised learning.",
                tech_stack=["Python", "Pandas", "Anomaly Detection"],
                links="https://github.com/Riteshkarki11"
            ),
            models.Project(
                title="Predictive LBO Valuation Engine",
                description="Integrating finance knowledge with predictive modeling for Leveraged Buyout valuations.",
                tech_stack=["Python", "Finance", "Regression"],
                links="https://github.com/Riteshkarki11"
            )
        ]
        db.add(ritesh)
        db.add_all(new_projects)
        db.commit()
    db.close()

seed_data()