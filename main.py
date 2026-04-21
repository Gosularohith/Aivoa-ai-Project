# --- Simple CRM Agent Example ---

# Simulated database (list instead of SQL for beginners)
interactions = []

# --- Tool Functions ---
def log_interaction_tool(data):
    """Add a new interaction to the list"""
    interactions.append({
        "id": len(interactions) + 1,
        "hcp_name": data["hcp_name"],
        "date": data["date"],
        "notes": data["notes"]
    })
    return {"status": "success", "message": "Interaction logged"}

def edit_interaction_tool(data):
    """Edit an existing interaction by ID"""
    for item in interactions:
        if item["id"] == data["id"]:
            item["notes"] = data["notes"]
            return {"status": "success", "message": "Interaction updated"}
    return {"status": "error", "message": "Interaction not found"}

def schedule_followup_tool(data):
    """Suggest a follow‑up meeting"""
    return {"suggestion": f"Schedule next meeting with {data['hcp_name']} in 30 days"}

def insights_generator_tool(data):
    """Count how many interactions exist for a given HCP"""
    count = sum(1 for i in interactions if i["hcp_name"] == data["hcp_name"])
    return {"insight": f"{data['hcp_name']} has {count} logged interactions"}

def compliance_checker_tool(data):
    """Check if mandatory fields are filled"""
    if not data.get("hcp_name") or not data.get("date"):
        return {"status": "error", "message": "Missing mandatory fields"}
    return {"status": "ok", "message": "Compliant"}

# --- Simple Agent Class ---
class Agent:
    def __init__(self, tools):
        # Convert list of tuples → dictionary
        self.tools = dict(tools)

    def run(self, tool_name, data):
        """Run the selected tool"""
        if tool_name in self.tools:
            return self.tools[tool_name](data)
        return {"status": "error", "message": "Tool not found"}

# --- Register Tools ---
tools = [
    ("log_interaction", log_interaction_tool),
    ("edit_interaction", edit_interaction_tool),
    ("schedule_followup", schedule_followup_tool),
    ("insights_generator", insights_generator_tool),
    ("compliance_checker", compliance_checker_tool),
]

# --- Example Usage ---
agent = Agent(tools)

# Log a new interaction
print(agent.run("log_interaction", {"hcp_name": "Dr. Smith", "date": "2026-04-21", "notes": "Discussed new treatment"}))

# Edit the interaction
print(agent.run("edit_interaction", {"id": 1, "notes": "Updated notes: dosage discussion"}))

# Generate insights
print(agent.run("insights_generator", {"hcp_name": "Dr. Smith"}))

# Check compliance
print(agent.run("compliance_checker", {"hcp_name": "Dr. Smith", "date": "2026-04-21"}))

# Suggest follow‑up
print(agent.run("schedule_followup", {"hcp_name": "Dr. Smith"}))