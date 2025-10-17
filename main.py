from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error
import time

set_verbosity_error()

# Use a faster, smaller model for summarization to run efficiently on CPU
# But with better parameters to control summary length
summarization_pipeline = pipeline(
    "summarization", 
    model="sshleifer/distilbart-cnn-12-6",
    model_kwargs={"use_cache": True},
    max_time=30,  # Limit generation time to 30 seconds
    truncation=True
)
summarizer = HuggingFacePipeline(pipeline=summarization_pipeline)

# For QA model
qa_pipeline = pipeline(
    "question-answering", 
    model="deepset/roberta-base-squad2",
    model_kwargs={"use_cache": True}
)

def summarize_text(text, length):
    # Define min and max length based on the desired length
    if length == "short":
        min_length, max_length = 30, 60
    elif length == "medium":
        min_length, max_length = 60, 120
    else:  # long
        min_length, max_length = 100, 200

    # Generate summary with appropriate length
    summary_result = summarization_pipeline(
        text, 
        min_length=min_length, 
        max_length=max_length,
        do_sample=False
    )
    return summary_result[0]['summary_text']

test_prompts = [
    {
        "text": "Artificial intelligence (AI) is a branch of computer science that aims to create software or machines that exhibit human-like intelligence. This can include learning from experience, understanding natural language, solving problems, recognizing patterns, and making decisions. AI technology is being applied in various fields such as healthcare, finance, transportation, and entertainment. The development of AI has raised important questions about ethics, privacy, and the future of work.",
        "length": "short",
        "questions": [
            "What is artificial intelligence?",
            "In which fields is AI applied?",
            "What are some important questions raised by AI development?"
        ]
    },
    {
        "text": "Climate change refers to long-term shifts in global or regional climate patterns. Since the mid-20th century, humans have been the main driver of climate change through the emission of greenhouse gases, primarily from burning fossil fuels like coal, oil, and gas. Effects of climate change include rising sea levels, extreme weather events, changes in ecosystems, and impacts on human health. Addressing climate change requires reducing greenhouse gas emissions and adapting to the changes already underway.",
        "length": "medium",
        "questions": [
            "What causes climate change?",
            "What are the effects of climate change?",
            "How can we address climate change?"
        ]
    },
    {
        "text": "The Internet is a global system of interconnected computer networks that use the standard Internet protocol suite (TCP/IP) to link devices worldwide. It began in the late 1960s with the ARPANET project, initially funded by the U.S. Department of Defense. The World Wide Web, invented by Tim Berners-Lee in 1989, revolutionized how people access and share information online. Today, the Internet connects billions of devices and users, transforming communication, commerce, education, entertainment, and many other aspects of daily life.",
        "length": "long",
        "questions": [
            "When did the Internet begin?",
            "Who invented the World Wide Web?",
            "How has the Internet transformed daily life?"
        ]
    },
    {
        "text": "The sun is a star at the center of our solar system. It is a nearly perfect sphere of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as light and solar wind. It is by far the most important source of energy for life on Earth. Its diameter is about 1.39 million kilometers, or 109 times that of Earth. The sun will continue to shine for another 5 billion years before it exhausts its hydrogen fuel and begins to die.",
        "length": "short",
        "questions": [
            "What is at the center of our solar system?",
            "How long will the sun continue to shine?",
            "What is the sun's diameter?"
        ]
    },
    {
        "text": "The human brain is an amazing organ that serves as the center of the nervous system. It controls thoughts, memory, emotions, touch, motor skills, vision, breathing, temperature, hunger, and every process that regulates our body. Weighing about 3 pounds, the brain contains approximately 86 billion neurons, which form trillions of connections called synapses. The brain uses about 20% of the body's total energy, despite being only about 2% of body weight. It is protected by the skull and a special blood-brain barrier that shields it from harmful substances.",
        "length": "medium",
        "questions": [
            "How much does the human brain weigh?",
            "How many neurons does the brain contain?",
            "What percentage of the body's energy does the brain use?"
        ]
    }
]

# Test prompts to evaluate all aspects of the code
test_prompts = [
    {
        "text": "Artificial intelligence (AI) is a branch of computer science that aims to create software or machines that exhibit human-like intelligence. This can include learning from experience, understanding natural language, solving problems, recognizing patterns, and making decisions. AI technology is being applied in various fields such as healthcare, finance, transportation, and entertainment. The development of AI has raised important questions about ethics, privacy, and the future of work.",
        "length": "short",
        "questions": [
            "What is artificial intelligence?",
            "In which fields is AI applied?",
            "What are some important questions raised by AI development?"
        ]
    },
    {
        "text": "Climate change refers to long-term shifts in global or regional climate patterns. Since the mid-20th century, humans have been the main driver of climate change through the emission of greenhouse gases, primarily from burning fossil fuels like coal, oil, and gas. Effects of climate change include rising sea levels, extreme weather events, changes in ecosystems, and impacts on human health. Addressing climate change requires reducing greenhouse gas emissions and adapting to the changes already underway.",
        "length": "medium",
        "questions": [
            "What causes climate change?",
            "What are the effects of climate change?",
            "How can we address climate change?"
        ]
    },
    {
        "text": "The Internet is a global system of interconnected computer networks that use the standard Internet protocol suite (TCP/IP) to link devices worldwide. It began in the late 1960s with the ARPANET project, initially funded by the U.S. Department of Defense. The World Wide Web, invented by Tim Berners-Lee in 1989, revolutionized how people access and share information online. Today, the Internet connects billions of devices and users, transforming communication, commerce, education, entertainment, and many other aspects of daily life.",
        "length": "long",
        "questions": [
            "When did the Internet begin?",
            "Who invented the World Wide Web?",
            "How has the Internet transformed daily life?"
        ]
    },
    {
        "text": "The sun is a star at the center of our solar system. It is a nearly perfect sphere of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as light and solar wind. It is by far the most important source of energy for life on Earth. Its diameter is about 1.39 million kilometers, or 109 times that of Earth. The sun will continue to shine for another 5 billion years before it exhausts its hydrogen fuel and begins to die.",
        "length": "short",
        "questions": [
            "What is at the center of our solar system?",
            "How long will the sun continue to shine?",
            "What is the sun's diameter?"
        ]
    },
    {
        "text": "The human brain is an amazing organ that serves as the center of the nervous system. It controls thoughts, memory, emotions, touch, motor skills, vision, breathing, temperature, hunger, and every process that regulates our body. Weighing about 3 pounds, the brain contains approximately 86 billion neurons, which form trillions of connections called synapses. The brain uses about 20% of the body's total energy, despite being only about 2% of body weight. It is protected by the skull and a special blood-brain barrier that shields it from harmful substances.",
        "length": "medium",
        "questions": [
            "How much does the human brain weigh?",
            "How many neurons does the brain contain?",
            "What percentage of the body's energy does the brain use?"
        ]
    }
]

# Run tests for each prompt
for i, prompt_data in enumerate(test_prompts, 1):
    print(f"\n--- Test {i} ---")
    text_to_summarize = prompt_data["text"]
    length = prompt_data["length"]
    
    summary = summarize_text(text_to_summarize, length)
    
    print("\n**Generated Summary:**")
    print(summary)
    
    # Ask predetermined questions about the summary
    for question in prompt_data["questions"]:
        print(f"\n**Question:** {question}")
        qa_result = qa_pipeline(question=question, context=summary)
        print("**Answer:**")
        print(qa_result["answer"])