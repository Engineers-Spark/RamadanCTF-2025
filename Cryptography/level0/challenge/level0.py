import random

questions = [
    {
        "question": "What does RSA stand for?",
        "options": ["A) Rivest, Shamir, Adleman", "B) Randomized Secure Algorithm", "C) Reliable Symmetric Authentication", "D) Rotating Security Algorithm"],
        "answer": "A"
    },
    {
        "question": "What type of cryptographic algorithm is RSA?",
        "options": ["A) Symmetric", "B) Asymmetric", "C) Hashing", "D) Stream cipher"],
        "answer": "B"
    },
    {
        "question": "Which mathematical problem is the security of RSA based on?",
        "options": ["A) Discrete logarithm problem", "B) Integer factorization problem", "C) Elliptic curve problem", "D) Diffie-Hellman problem"],
        "answer": "B"
    },
    {
        "question": "What are the two prime numbers p and q used for in RSA?",
        "options": ["A) Generating the public key", "B) Encrypting the message", "C) Computing the modulus n", "D) Decrypting the ciphertext"],
        "answer": "C"
    },
    {
        "question": "Which of the following is true about the RSA public key?",
        "options": ["A) It consists of a single prime number", "B) It is made up of n and d", "C) It is kept secret", "D) It is made up of n and e"],
        "answer": "D"
    },
    {
        "question": "What is the purpose of the private key in RSA?",
        "options": ["A) To encrypt messages", "B) To generate prime numbers", "C) To decrypt messages", "D) To factorize numbers"],
        "answer": "C"
    },
    {
        "question": "Which mathematical function is used to compute φ(n) in RSA?",
        "options": ["A) φ(n) = p + q - 1", "B) φ(n) = (p-1) × (q-1)", "C) φ(n) = p × q", "D) φ(n) = (p+1) × (q+1)"],
        "answer": "B"
    },
    {
        "question": "What condition must the public exponent e satisfy?",
        "options": ["A) It must be prime", "B) It must be even", "C) It must be coprime with φ(n)", "D) It must be greater than n"],
        "answer": "C"
    },
    {
        "question": "What is a common value used for the public exponent e in RSA?",
        "options": ["A) 65537", "B) 1024", "C) 12345", "D) 8192"],
        "answer": "A"
    },
    {
        "question": "Which step is required to decrypt a ciphertext in RSA?",
        "options": ["A) Raising it to the power of e modulo n", "B) Raising it to the power of d modulo n", "C) Multiplying it by φ(n)", "D) Adding p and q"],
        "answer": "B"
    }
]


def banner():
    print("""
██████╗ ███████╗ █████╗      ██████╗ ██╗   ██╗██╗███████╗
██╔══██╗██╔════╝██╔══██╗    ██╔═══██╗██║   ██║██║╚══███╔╝
██████╔╝███████╗███████║    ██║   ██║██║   ██║██║  ███╔╝ 
██╔══██╗╚════██║██╔══██║    ██║▄▄ ██║██║   ██║██║ ███╔╝  
██║  ██║███████║██║  ██║    ╚██████╔╝╚██████╔╝██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
                                                         
""")

flag = "FLAG{90ef9e0c61da9fa5e70b982adeab628d}"
score = 0

banner()
random.shuffle(questions)

for idx, q in enumerate(questions, start=1):
    print(f"Question {idx}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

if score == len(questions):
    print(f"🎉 Congratulations! You answered all questions correctly. Here is your flag: {flag}")
else:
    print(f"Your final score: {score}/{len(questions)}. Try again to get the flag!")
