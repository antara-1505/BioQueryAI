import streamlit as st
from app.agent import answer_query

st.set_page_config(page_title="BioQuery AI", layout="centered")
st.title("BioQuery AI — Biomedical Research Assistant")

q = st.text_input("Ask a biomedical question (e.g., CRISPR in Parkinson's):")
if st.button("Search"):
    with st.spinner("Thinking..."):
        res = answer_query(q)
    st.subheader("Answer")
    st.write(res["answer"])
    st.subheader("Top sources")
    for p in res["papers"]:
        st.markdown(f"- **{p['title']}** (PMID: {p['pmid']}) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/{p['pmid']}/)")
