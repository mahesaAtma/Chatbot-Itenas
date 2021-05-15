# ==========================================================
# CREATOR : Mahesa Atmawidya Negara Ekha Salawangi
# DATE CREATED : 20 JUNE 2020
# ABOUT : Simple Chatbot Itenas
# ==========================================================

# nltk untuk membantu dalam memproses data text
import nltk
# string untuk membantu membuang tanda baca yang nantinya
# akan menganggu proses kemiripan text dataset dengan
# text input-an
import string
# Import random untuk memilih secara acak
import random
# Import sklearn digunakan untuk memproses text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Sastrawi digunakan untuk mengambil stop_words versi Indonesia, seperti
# atau,dan,sebagainya,lalu dan yang lain lainnya yang pada umumnya
# sering dipakai
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

class jalanBot():
    def __init__(self):
        # Memuat atau Membaca dataset text itenasDoc.txt
        self.text = open("itenasDoc.txt","r",errors='ignore').read()
        # Membust semua text didalam dataset menjadi lowercase
        self.text = self.text.lower()

        # Mengambil stopwords versi Indonesia
        self.factory = StopWordRemoverFactory()
        self.stopwords_indonesia = self.factory.get_stop_words()

        # Memisahkan dataset menjadi dalam bentuk array dengan
        # pemisahnya . atau per kalimat
        self.sents_tokenize = nltk.sent_tokenize(self.text)

        # Inisialisasi kata yang akan digunakan
        self.sapa_user = ['hello', 'hallo', 'hi', 'hallo itenas']
        self.greet_user = ['Hallo juga :D',"Senang bertemu dengan mu, apa yang bisa aku bantu?","Hiiiiii ^_^"]
        self.kelimat_perpisahan = ['selesai', 'quit', 'dadah', 'berhenti']

        # Inisialisasi respon 
        self.admin_respon = "Itenas : "

    def tokenize_function(self,data): 
        # Menghilangkan tanda baca yang nantinya tidak akan terpakai di pencari kesamaan
        texts = [token for token in data if token not in string.punctuation]
        new_text = ''.join(texts)
        # Menghilangkan kata-kata Indonesia yang tidak penting
        stopwords = [token for token in new_text if token not in self.stopwords_indonesia]
        # Return kata per kata
        return nltk.word_tokenize(''.join(stopwords))

    def bot_response(self,user_response):
        bot_res = ' '
        self.sents_tokenize.append(user_response)
        # Term Frequency dan Inver Document Frequency
        tfidf_vec = TfidfVectorizer(tokenizer=self.tokenize_function)
        tfidf_convert = tfidf_vec.fit_transform(self.sents_tokenize)
        # Mencari kesamaan antara input user dengan dataset
        similarity = cosine_similarity(tfidf_convert[-1],tfidf_convert)
        # Mencari probabilitas tertinggi
        idx = similarity.argsort()[0][-2]
        flatten = similarity.flatten()
        flatten.sort()
        if flatten[-2] == 0:
            bot_res = bot_res + "Tidak dapat mengerti kata yang kamu berikan"
            return bot_res
        else:
            bot_res = bot_res + self.sents_tokenize[idx]
            return bot_res

    def runBot(self,user_input):
        user_input = user_input.lower()

        if user_input in self.sapa_user:
            return [[self.admin_respon, random.choice(self.greet_user) + ", silahkan mencoba mencari informasi tentang Itenas :)"]]
        
        elif user_input in self.kelimat_perpisahan:
            return [[self.admin_respon , "Terimakasih ^_^, sampai jumpa kembali!!"]]
        else:
            hasil = [[self.admin_respon , self.bot_response(user_input)]]
            self.sents_tokenize.remove(user_input)
            return hasil
        

