class WordScoreFilter:
    """Detectors 1 and 2: learned word scores.
    The preprocessor and min_count decide which detector this is.
    """

    def __init__(self, preprocessor, min_count: int = 1):
        """Words seen fewer than min_count times in training are ignored."""
        self.preprocessor = preprocessor
        self.min_count = min_count

    def fit(self, emails: list):
        
        """Count each word in spam and in normal training emails.

        Store the counts in two dicts: self.spam_counts and self.normal_counts.
        """
        self.spam_counts = {}
        self.normal_counts = {}
        for email in emails:
            words_list = self.preprocessor.tokenize(email)
            if email.is_spam:
                for word in words_list:
                    if word not in self.spam_counts:
                        self.spam_counts[word]=1
                    else:
                        self.spam_counts[word]+=1
            else: 
                for word in words_list:
                    if word not in self.normal_counts:
                        self.normal_counts[word]=1
                    else:
                        self.normal_counts[word]+=1
        return self.spam_counts, self.normal_counts 
    
    def calculate_word_score(self,email) -> list:
        """Return the list of pair of (word, word score) for known word. Return an empty list if no word is known"""
        email_words_list = self.preprocessor.tokenize(email)
        score_list=[] 
        for word in email_words_list:
            s = self.spam_counts.get(word,0)
            h = self.normal_counts.get(word,0)
            if s+h < self.min_count:
                continue
            word_score = s/(s+h)
            score_list.append((word,word_score))
        return score_list
    
    def score(self, email) -> float:
        """Return the average word score. Skip unknown words. Return 0.0 if none are known."""
        score_list = self.calculate_word_score(email)
        if score_list ==[]:
            return 0.0
        return sum([score[1] for score in score_list])/len(score_list)

    def predict(self,email,threshold=0.5) -> bool:
        """Return True (spam) when score(email) > threshold."""
        average_score = self.score(email)
        if average_score > threshold:
            return True
        else:
            return False


    def top_spam_words(self, email, k: int = 5) -> list:
        """Return the email's k known words with the highest scores, as (word, score) pairs."""
        word_and_score_list = self.calculate_word_score(email)
        desc_sorted_word_list = sorted(word_and_score_list,key = lambda x: x[1],reverse=True)

        #Return the whole (word,score) list if k larger than number of known words
        if k > len(word_and_score_list): 
            return desc_sorted_word_list
        return desc_sorted_word_list[:k]