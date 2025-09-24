import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# --- Load & Clean Data ---
df = pd.read_csv("metadata_sample.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# --- Streamlit Layout ---
st.title("CORD-19 Data Explorer")
st.write("Exploring a sample of COVID-19 research papers")

# Year filter
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Sample of Filtered Data")
st.write(filtered.head())

# --- Analysis + Visualizations ---

# 1. Publications by Year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Publications by Year")
st.pyplot(fig)

# 2. Top Journals
st.subheader("Top 10 Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="bar", ax=ax)
ax.set_xlabel("Journal")
ax.set_ylabel("Paper Count")
ax.set_title("Top 10 Journals Publishing COVID-19 Research")
st.pyplot(fig)



# 4. Distribution by Source
st.subheader("Distribution of Papers by Source")
fig, ax = plt.subplots()
filtered['source_x'].value_counts().plot(kind="bar", ax=ax)
ax.set_xlabel("Source")
ax.set_ylabel("Paper Count")
ax.set_title("Distribution by Source")
st.pyplot(fig)
