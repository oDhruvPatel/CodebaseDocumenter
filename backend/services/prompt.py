DOCUMENTATION_PROMPT = """
You are a senior software engineer.

Analyze this codebase and return ONLY a JSON object, no markdown, no backticks, nothing else.

## CODEBASE:
{codebase}

Return this EXACT JSON structure:
{{
    "project_name": "name of the project",
    "files": [
        {{
            "name": "filename.ext",
            "purpose": "one sentence what this file does",
            "functions": ["functionName - what it does"],
            "dependencies": ["library1", "library2"]
        }}
    ]
}}

RULES:
- Return ONLY JSON
- If file is empty set purpose to "Empty file"
- Keep everything concise
"""