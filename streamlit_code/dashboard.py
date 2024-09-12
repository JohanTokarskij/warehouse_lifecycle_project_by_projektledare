import streamlit as st
from connect_data_warehouse import query_job_listings

#st.set_page_config(layout="wide")

def layout():
    df = query_job_listings()

    st.title("Project Leader job ads")
    st.write("This dashboard shows project leading job ads from Arbetsförmedlingens API")
    
    # Search functionality
    search_term = st.text_input("Search job ads by keyword:")
    if search_term:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]


    ## Metric section ##
    cols = st.columns(2)
    with cols[0]:
        st.metric(label="Total Vacancies", value=df["NUMBER_VACANCIES"].sum())
        
    with cols[1]:
        st.metric(label="Total Employers", value=df["EMPLOYER_NAME"].nunique())
        
    # Vacancies per city
    cols = st.columns(2)
    with cols[0]:
        st.markdown("### Per city")
        city_data = df.groupby("WORKPLACE_CITY")["NUMBER_VACANCIES"].sum().reset_index()
        city_data = city_data.rename(columns={"WORKPLACE_CITY": "City", "NUMBER_VACANCIES": "Vacancies"})
        st.dataframe(city_data)
    
    # Vacancies per company (Top 5)
    with cols[1]:
        st.markdown("### Per company (top 5)")
        company_data = df.groupby("EMPLOYER_NAME")["NUMBER_VACANCIES"].sum().reset_index()
        company_data = company_data.rename(columns={"EMPLOYER_NAME": "Company", "NUMBER_VACANCIES": "Vacancies"})
        company_data["Vacancies"] = company_data["Vacancies"].round(0).astype(int)
        top_5_companies = company_data.nlargest(5, "Vacancies")
        st.bar_chart(top_5_companies, x="Company", y="Vacancies")

    # Time-based trend of job ads
    st.markdown("### Job Ads Over Time")
    time_data = df.groupby("PUBLICATION_DATE_ID")["NUMBER_VACANCIES"].sum().reset_index()
    time_data = time_data.rename(columns={"NUMBER_VACANCIES": "Vacancies", "PUBLICATION_DATE_ID": "Publication Date"})

    time_data["Vacancies"] = time_data["Vacancies"].round(0).astype(int)
    st.line_chart(time_data, x="Publication Date", y="Vacancies")
    

    st.markdown("### Find advertisement")
    # Concatenate company name and headline into one field for the selectbox
    df["company_ad"] = df["EMPLOYER_NAME"] + " - " + df["HEADLINE"]

    # Create a single selectbox
    selected_company_ad = st.selectbox("Select a company and advertisement:", df["company_ad"].sort_values().unique())

    # Extract the selected company and headline
    selected_company, selected_headline = selected_company_ad.split(" - ")

    # Display the selected job ad title as a real title
    st.markdown(f"## {selected_headline}")

    # Display the job description
    job_description = df.query("HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company")["DESCRIPTION_HTML_FORMATTED"].values[0]
    st.markdown(job_description, unsafe_allow_html=True).markdown(df.query("HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company")["DESCRIPTION_HTML_FORMATTED"].values[0], unsafe_allow_html=True)

    # Fetch other relevant information for KPIs
    selected_job = df.query("HEADLINE == @selected_headline and EMPLOYER_NAME == @selected_company")


    st.markdown("### Job Details")


    cols = st.columns(4)

    with cols[0]:
        st.markdown("#### Workplace City")
        st.write(selected_job['WORKPLACE_CITY'].values[0])

    with cols[1]:
        st.markdown("#### Salary Type")
        st.write(selected_job['SALARY_TYPE'].values[0])

    with cols[2]:
        st.markdown("#### Duration")
        st.write(selected_job['DURATION'].values[0])

    with cols[3]:
        st.markdown("#### Scope of Work")
        scope_min = int(round(40 / int(selected_job["SCOPE_OF_WORK_MIN"].values[0]) * 100, 0))
        st.write(f"{scope_min} hours/week")

    cols2 = st.columns(2)

    with cols2[0]:
        st.markdown("#### Publication Date")
        publication_date = selected_job["PUBLICATION_DATE_ID"].values[0]
        st.write(publication_date)

    with cols2[1]:
        st.markdown("#### Application Deadline")
        application_deadline = selected_job["APPLICATION_DEADLINE_ID"].values[0]
        st.write(application_deadline)
if __name__ == "__main__":
    layout()
