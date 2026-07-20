# === Stage 35: Add active user switching and user-specific records ===
# Project: MentorBoard
import json, os
from datetime import date
PROFILE_DIR = "profiles"
def load_users(): return {u:json.load(open(os.path.join(PROFILE_DIR,u))) for u in os.listdir(PROFILE_DIR) if u.endswith(".json")}
class UserSession:
    def __init__(self,name): self.name=name; self.session_id=None; self.goals=[]; self.questions=[]; self.resources=[]; self.feedback={}
    def start(self,topic,duration=60): import uuid; self.session_id=str(uuid.uuid4())[:8]; print(f"Session started [{self.name}] topic={topic} duration={duration}min")
    def add_goal(self,g): self.goals.append({"text":g,"done":False}); return self
    def ask(self,q): self.questions.append(q); return self
    def share_resource(self,url,title=""): self.resources.append({"url":url,"title":title}); return self
    def give_feedback(self,key,comment): self.feedback[key]=comment; print(f"Feedback saved: {key} -> {comment}")
    def end_report(self): print(f"\n--- Report for {self.name} ---\nSession:{self.session_id}\nGoals remaining:",sum(1 for g in self.goals if not g["done"])); print("Resources shared:",len(self.resources)); print("Feedback notes:",{k:v for k,v in self.feedback.items() if v!="none"})
