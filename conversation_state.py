class ConversationState:

    def __init__(self):
        self.resume_text = None
        self.job_description = None
        self.resume_skills = []
        self.job_skills = []
        self.matched_skills = []
        self.missing_skills = []

    def update_resume(self, resume_text):
        self.resume_text = resume_text

    def update_job(self, job_description):
        self.job_description = job_description

    def update_resume_skills(self, skills):
        self.resume_skills = skills

    def update_job_skills(self, skills):
        self.job_skills = skills

    def set_match_results(self, matched, missing):
        self.matched_skills = matched
        self.missing_skills = missing

    def get_state(self):
        return {
            "resume_provided": self.resume_text is not None,
            "job_provided": self.job_description is not None,
            "resume_skills": self.resume_skills,
            "job_skills": self.job_skills,
            "matched_skills": self.matched_skills,
            "missing_skills": self.missing_skills
        }