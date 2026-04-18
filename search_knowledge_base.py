def search_knowledge_base(query):
    try:
        with open("knowledge-base.md", "r") as f:
            kb = f.read().lower()

        if query.lower() in kb:
            return {"found": True, "snippet": query}
        else:
            return {"found": False}

    except Exception as e:
        return {"error": str(e)}