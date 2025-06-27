import streamlit as st
import pandas as pd

st.title("📊 CSV Merger App")

st.write("Upload two CSV files to merge them.")

# Upload two CSV files
file1 = st.file_uploader("Upload First CSV", type="csv")
file2 = st.file_uploader("Upload Second CSV", type="csv")

if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    st.subheader("First CSV Preview")
    st.dataframe(df1.head())

    st.subheader("Second CSV Preview")
    st.dataframe(df2.head())

    # Find common columns
    common_cols = list(set(df1.columns).intersection(set(df2.columns)))
    
    if common_cols:
        st.success(f"Common columns found: {common_cols}")
        merge_col = st.selectbox("Select column to merge on", common_cols)

        if st.button("Merge Files"):
            merged_df = pd.merge(df1, df2, on=merge_col, how="inner")
            st.subheader("🔗 Merged DataFrame")
            st.dataframe(merged_df)
            csv = merged_df.to_csv(index=False).encode("utf-8")
            st.download_button("Download Merged CSV", csv, "merged.csv", "text/csv")
    else:
        st.error("No common columns found to merge on.")
