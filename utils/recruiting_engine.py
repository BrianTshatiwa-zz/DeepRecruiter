import transformers 
from sentence_transformers import SentenceTransformer, util

ranking_model = SentenceTransformer('sentence-transformers/all-distilroberta-v1')

class DeepRecruiter:
    """
    an interface for presenting words or sentences into their embedding representations
    Args:
       model (str): a language model
    """
    def __init__(self, model):
        self.model = model 

    def generate_embeddings(self, customer_problem, candidate_abilities):
        """
        Given two sentences or paragraphs, encode them to their 
        embeddings representation 
        """
        customer_problem_embeddings = self.model.encode(customer_problem)
        candidate_abilities_embeddings = self.model.encode(candidate_abilities)
        return customer_problem_embeddings, candidate_abilities_embeddings
    
    def compute_similarity(self, customer_problem, candidate_abilities):
        """
        Given word embeddings, compute their cosine similarity 
        """
        customer_problem_embeddings, candidate_abilities_embeddings = self.generate_embeddings(customer_problem, candidate_abilities)
        cos_score = util.pytorch_cos_sim(customer_problem_embeddings, candidate_abilities_embeddings)
        return cos_score.item()*100

