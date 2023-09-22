import streamlit as st
from textblob import TextBlob
import pandas as pd 
import emoji

from bs4 import BeautifulSoup
from urllib.request import urlopen

@st.cache_resource
def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

def main():
	st.title("تحلیل احساس مبتنی بر متن")

	activities = ["Sentiment","Text Analysis on URL","About"]
	choice = st.sidebar.selectbox("صفحات",activities)

	if choice == 'Sentiment':
		st.subheader("تحلیل احساس")
		st.write(emoji.emojize('ممنون از انتخاب شما :red_heart:'))
		raw_text = st.text_area("متن انگلیسی خود را وارد کنید","متن نمونه")
		if st.button("تحلیل"):
			blob = TextBlob(raw_text)
			result = blob.sentiment.polarity
			if result > 0.0:
				custom_emoji = ':smile:'
				st.write(emoji.emojize(custom_emoji))
			elif result < 0.0:
				custom_emoji = ':disappointed:'
				st.write(emoji.emojize(custom_emoji))
			else:
				st.write(emoji.emojize(':expressionless:'))
			st.info("امتیاز:: {}".format(result))
			
	if choice == 'Text Analysis on URL':
		st.subheader("تحلیل احساس صفحه‌ی وب")
		raw_url = st.text_input("آدرس را وارد کنید","https://google.com")
		text_preview_length = st.slider("پیش‌نمایش", 50, 100)
		if st.button("تحلیل"):
			if raw_url != "":
				result = get_text(raw_url)
				blob = TextBlob(result)
				len_of_full_text = len(result)
				len_of_short_text = round(len(result)/text_preview_length)
				st.success("طول متن::{}".format(len_of_full_text))
				st.success("طول متن کوتاه شده::{}".format(len_of_short_text))
				st.info(result[:len_of_short_text])
				c_sentences = [ sent for sent in blob.sentences ]
				c_sentiment = [sent.sentiment.polarity for sent in blob.sentences]
				
				new_df = pd.DataFrame(zip(c_sentences,c_sentiment),columns=['Sentence','Sentiment'])
				st.write(new_df.to_html(), unsafe_allow_html=True)

	if choice == 'About':
		st.subheader("گروه برنامه‌نویسان جالب")
		st.info("قدرتمندترین برنامه‌نویسان جهان هستیم")
		st.text("programers.com")

if __name__ == '__main__':
	main()

# MasoudKaviani.ir
# python -m streamlit run app.py --server.port 8080