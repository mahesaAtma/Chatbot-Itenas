# ==========================================================
# CREATOR : Mahesa Atmawidya Negara Ekha Salawangi
# DATE CREATED : 20 JUNE 2020
# ABOUT : Simple Chatbot Itenas
# ==========================================================


import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from colorama import Fore,Style

text = open("itenasDoc.txt","r",errors='ignore').read()
text = text.lower()

factory = StopWordRemoverFactory()
stopwords_indonesia = factory.get_stop_words()

sents_tokenize = nltk.sent_tokenize(text)

# Inisialisasi kata yang akan digunakan
sapa_user = ['hello','hallo','hi','hallo itenas']
greet_user = ['Hallo juga :D',"Senang bertemu dengan mu, apa yang bisa aku bantu?","Hiiiiii ^_^"]
kelimat_perpisahan = ['selesai','quit','dadah','berhenti']


def tokenize_function(data): 
    # Menghilangkan tanda baca yang nantinya tidak akan terpakai di pencari kesamaan
    texts = [token for token in data if token not in string.punctuation]
    new_text = ''.join(texts)
    # Menghilangkan kata-kata Indonesia yang tidak penting
    stopwords = [token for token in new_text if token not in stopwords_indonesia]
    # Return kata per kata
    return nltk.word_tokenize(''.join(stopwords))

def bot_response(user_response):
    bot_res = ' '
    sents_tokenize.append(user_response)
    # Term Frequency dan Inver Document Frequency
    tfidf_vec = TfidfVectorizer(tokenizer=tokenize_function)
    tfidf_convert = tfidf_vec.fit_transform(sents_tokenize) 
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
        bot_res = bot_res + sents_tokenize[idx]
        return bot_res


running = True
admin_respon = "Itenas : "
print(admin_respon + "Hallo, selamat datang ke Itenas, dan terimakasih telah memilih untuk berbicara dengan saya adalah sebuah robot")
print(admin_respon + "Untuk memulai percakapan denganku, kamu harus mengetikan 'hello',atau 'hi',atau 'hallo itenas' ^_^")
print(admin_respon + "Jika kamu ingin selesai atau keluar, silahkan ketikan 'Selesai','Quit','Berhenti',atau 'Dadah'")

while running:
    
    user_input = input("Kamu : ")
    user_input = user_input.lower()

    if user_input in sapa_user:
        print(admin_respon + random.choice(greet_user))
        print(admin_respon + "Silahkan mencoba mencari informasi tentang Itenas :)")
        running_inside = True
        while running_inside:
            new_input = input("Kamu : ")
            print(admin_respon + bot_response(new_input))
            sents_tokenize.remove(new_input)
            if new_input in kelimat_perpisahan:
                print(admin_respon + "Terimakasih ^_^, sampai jumpa kembali!!")
                running = False
                running_inside = False
        if user_input in kelimat_perpisahan:
            print(admin_respon + "Terimakasih ^_^, sampai jumpa kembali!!")
            running = False
    else:
        print(admin_respon + "Biasakan 5S (Senyum,Sapa,Sopan,Santun,Salam) :)")
    

