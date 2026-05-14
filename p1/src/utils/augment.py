class Augment:
    def __init__(self, context: list[str], query: str):
        self.context = context
        self.query = query

    def _chat_llm(self):
        return None

    def augment(self):
        context = " ".join(contexts for contexts in self.context)
        
        augmentation_rules = """
        ### **Augmentation Rules**
        - **Expand on key points**: Use retrieved context to provide a well-structured, in-depth response.
        - **Ensure coherence**: Maintain logical flow and readability in your response.
        - **Maintain factual accuracy**: Do not introduce unverified information.
        - **Provide comprehensive details**: Expand on concepts where necessary to enhance understanding.
        - **Use structured formatting**: Utilize bullet points or paragraphs for clarity.
        - **Avoid unnecessary repetition**: Ensure that the response remains informative and concise.
        - **Respect query intent**: Answer directly based on retrieved data without making assumptions.
        """

        augmented_text = f"""" 
        Here is the retrieved context: {context}.

        Based on the retrieved content, please answer the following query: {self.query}

        {augmentation_rules}
        """

        return augmented_text