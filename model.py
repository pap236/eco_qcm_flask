from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def emb_similarity(question, options):
    # Embedding

    q_emb = model.encode(question, convert_to_tensor=True)
    opt_embs = model.encode(options, convert_to_tensor=True)

    # Similarité
    scores = util.pytorch_cos_sim(q_emb, opt_embs)[0]
    best_idx = scores.argmax().item()
    best_option = options[best_idx]
    best_score = round(scores[best_idx].item(), 4)
    return best_option, best_score
