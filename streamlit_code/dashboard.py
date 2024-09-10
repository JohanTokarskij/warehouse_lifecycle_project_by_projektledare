import streamlit as st
from connect_data_warehouse import query_job_listings


def layout():
    df = query_job_listings()
    
    st.title("Project Leader job ads")
    st.write("This dashboard shows project leading job ads from Arbetsförmedlingens API")
    st.markdown("## Vacancies")
    cols = st.columns(3)
    with cols[0]:
        st.metric(label = "Total", value = df["NUMBER_VACANCIES"].sum())
        
    with cols[1]:
        st.metric(label = "In Stockholm",
        value = df[df["WORKPLACE_CITY"].str.lower() == 'stockholm']["NUMBER_VACANCIES"].sum())
        
    with cols[2]:
        st.metric(label = "In Göteborg",
        value = df[df["WORKPLACE_CITY"].str.lower() == 'göteborg']["NUMBER_VACANCIES"].sum())
    
    cols = st.columns(2)
        
    with cols[0]:
        st.markdown("### Per city")
        st.dataframe(
            query_job_listings(
                """
                SELECT 
                    sum(number_vacancies) as vacancies,
                    workplace_city
                FROM 
                    mart_job_listings
                GROUP BY
                    workplace_city
                ORDER BY
                    vacancies desc; 
                """
            )
        )
        
    with cols[1]:
        st.markdown("### Per company (top 5)")
        st.bar_chart(
            query_job_listings(
                """
                SELECT 
                    sum(number_vacancies) as vacancies,
                    employer_name
                FROM 
                    mart_job_listings
                GROUP BY
                    employer_name
                ORDER BY
                    vacancies desc LIMIT 5; 
                """
            ),
            x = "EMPLOYER_NAME",
            y = "VACANCIES"
        )
    
    st.markdown("### Find advertisment")
    
    cols = st.columns(2)
    
    with cols[0]:
        selected_company = st.selectbox("Select a company:", df["EMPLOYER_NAME"].unique())
        
    with cols[1]:
        selected_headline = st.selectbox("Select an advertisment:", df.query("EMPLOYER_NAME == @selected_company")["HEADLINE"])
        
    st.markdown("### Job ad")
    st.markdown(df.query("HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company")["DESCRIPTION_HTML_FORMATTED"].values[0], unsafe_allow_html = True)
    st.markdown("### Job listings data")
    
    st.dataframe(df)

if __name__ == "__main__":
    layout()