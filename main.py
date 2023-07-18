# # This is a sample Python script.
# import streamlit
# import plotly.graph_objects as go
# from test_file import add
# import plotly.express as px
# import pandas as pd
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     add(3,5)
#
# # See PyCharm help   at https://www.jetbrains.com/help/pycharm/
# import streamlit as st
# st.title('This My first Practice web app')
# st.header('Krishna Love')
# if st.sidebar.button("Click me"):
#     st.sidebar.write("Button clicked!")
# from PIL import Image
# img=Image.open('OIP (2).jpg')
# st.image(img,caption="Krishna Image")
#
# # control,+,/ to comment multiple lines.
# # #Success
# #st.success("Correct Statement")
# #Error
# #st.error("Error Statement")
# #st.exception("This is Exception")
# #st.help("This is for help cell")
# # st.video("kanha.mp4")
# # if st.checkbox('Show/hide'):
# #     st.write("You will always bless by krishna")
# # status=st.radio("What is your Status about chanting",('Active',"Inactive"))
# # if status is 'Active':
# #     st.success('You are forture entity')
# # else:
# #     st.warning("you need the correct way of life.")
# # #Select Box
# # occupation=st.selectbox('What do you do for living',["","Data Analyst","Data Scientist","Data Engineer","Machine Learning Engineer"])
# # st.write("You are a", occupation)
# # skill=st.multiselect("Select your skills",["Python","Machine Learning","Deep Learning","NLP","R","SQL","SAS","Computer Vision"])
# # st.write("You selected",len(skill),'skills')
# # #Slider
# # age=st.slider("What is your Age",6,100)
# # st.write("You are",age,"year old.")
# # if st.button("About me"):
# #     st.text('I am Chetan Salunke')
# # #text input
# # gmail=st.text_input("Enter your Gmail Id")
# # if '@gmail.com' in gmail:
# #     st.success(f'Gmail Confirmed {gmail}')
# # else:
# #     st.error("Check your mail its Invalid")
# #  #Long Messege
# # st.text_area("Give me your fidback about Chanting")
# #
# # #Date
# # import datetime
# # st.date_input("Today is",datetime.datetime.now())
# #
# # #Time
# # import time
# # st.time_input("Current time",datetime.time())
# #  #Display  code
# # st.write("How to install stremlit")
# # st.code("pip install streamlit")
#
# # with st.echo():
# #     #How to import streamlit
# #     import streamlit
# #     import pandas
#
#
#
# #Import Excel file
# st.title("T20 Data Analysis")
# df=pd.read_excel(io='T20.xlsx',sheet_name='Sheet1',engine='openpyxl',nrows=38478)
#
# # st.sidebar.header("Please Filtre here")
# #
# # batting_team=st.sidebar.multiselect("Select the Batting_team:",options=df['batting_team'].unique(),
# #                        default=df['batting_team'].unique()
# #                        )
# # selection_df=df.query("batting_team==@batting_team")
#
#
# #---------------------------------------------------------------------------------------
# st.sidebar.write("Get sum of Total Score in T20 matches done by individual team")
# if st.sidebar.button("Get Total Run"):
#     grouped_df = df.groupby('batting_team')['runs_x'].sum()
#     grouped_df = grouped_df.sort_values(ascending=False)
#     # Create two columns
#     col1, col2 = st.columns([1, 1])
#     # Display the DataFrame in the first column
#     with col1:
#         st.dataframe(grouped_df)
#
#     # Extract the data for the chart
#     labels = grouped_df.index
#     values = grouped_df.values
#
#     # Create a pie chart using Plotly
#     fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
#
#     # Display the chart in the second column
#     with col2:
#         st.plotly_chart(fig)
# #---------------------------------------------------------------------------------------
# st.sidebar.write("Get Max Score in T20 matches done by individual team")
# if st.sidebar.button("Get Max Run"):
#     grouped_df1 = df.groupby('batting_team')['runs_x'].max()
#     grouped_df1=grouped_df1.sort_values(ascending=False)
#
#     col3,col4=st.columns([1,1])
#     with col3:
#         st.dataframe(grouped_df1)
#     with col4:
#         fig1=px.bar(grouped_df1)
#         st.plotly_chart(fig1)
#
# #---------------------------------------------------------------------------------------
# st.sidebar.write("Get Max Run Rate in T20 matches of individual team")
# if st.sidebar.button("Get Max Run Rate"):
#     grouped_df2 = df.groupby('batting_team')['crr'].max()
#     grouped_df2=grouped_df2.sort_values(ascending=False)
# # ---------------------------------------------------------------------------------------
#     col5,col6=st.columns([1,1])
#     with col5:
#         st.dataframe(grouped_df2)
#     with col6:
#         fig1=px.bar(grouped_df2)
#         st.plotly_chart(fig1)
# # ---------------------------------------------------------------------------------------
#
# # Group the data by batting_teams and wicket_left, calculate the maximum values, and sort the results
# grouped_df = df.groupby(['batting_team', 'wickets_left']).agg({'runs_x': 'max', 'crr': 'max'}).reset_index()
# grouped_df_sorted = grouped_df.sort_values(['runs_x', 'crr'], ascending=False)
#
# # Sidebar selectbox for batting_team selection
# selected_teams = st.sidebar.selectbox('Select Batting Team', grouped_df_sorted['batting_team'].unique())
#
# # Filter the grouped and sorted DataFrame based on selected teams
# filtered_df = grouped_df_sorted[grouped_df_sorted['batting_team']==selected_teams]
#
# # Display the filtered DataFrame
# st.dataframe(filtered_df)
# fig3 = go.Figure()
# fig3.add_trace(go.Bar(x=filtered_df['wickets_left'], y=filtered_df['runs_x'], name='Runs_x'))
# fig3.add_trace(go.Bar(x=filtered_df['wickets_left'], y=filtered_df['crr'], name='CRR'))
# fig3.update_layout(barmode='group')
# st.plotly_chart(fig3)
# # ---------------------------------------------------------------------------------------
#
 #st.balloons()
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set page configuration
st.set_page_config(page_title='T20 Data Analysis', page_icon=':cricket:', layout='wide')

# Apply CSS styling
st.markdown("""
<style>
    .title {
        color: #FF4500;
        text-align: center;
        font-size: 40px;
        margin-bottom: 50px;
    }

    .sidebar {
        background-color: #f4f4f4;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Add title styling
st.markdown('<p class="title">T20 Data Analysis</p>', unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("Dashbord")
st.sidebar.image("image20_2.jpg")
st.sidebar.markdown('<p class="sidebar">Please Filter Here</p>', unsafe_allow_html=True)

#---------------------------------------------------------------------------------------
# Import Excel file

df = pd.read_excel(io='T20.xlsx', sheet_name='Sheet1', engine='openpyxl', nrows=38478)
st.sidebar.write("Get sum of Total Score in T20 matches done by individual team")
if st.sidebar.button("Get Total Run"):
    grouped_df = df.groupby('batting_team')['runs_x'].sum().sort_values(ascending=False)
    # Create a colorful pie chart using Plotly Express
    fig = px.pie(grouped_df, values='runs_x', names=grouped_df.index, title='Total Score by Team')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5))
    fig.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig)

#---------------------------------------------------------------------------------------
st.sidebar.write("Get Max Score in T20 matches done by individual team")
if st.sidebar.button("Get Max Run"):
    grouped_df1 = df.groupby('batting_team')['runs_x'].max().sort_values(ascending=False)

    # Create a colorful bar chart using Plotly Express
    fig1 = px.bar(grouped_df1, title='Max Score by Team')
    fig1.update_layout(xaxis_title='Team', yaxis_title='Max Runs')
    fig1.update_traces(marker_color=['#FFA07A', '#FF4500', '#FF6347', '#FF7F50'])
    fig1.update_layout(plot_bgcolor='white')
    st.plotly_chart(fig1)

#---------------------------------------------------------------------------------------
st.sidebar.write("Get Max Run Rate in T20 matches of individual team")
if st.sidebar.button("Get Max Run Rate"):
    grouped_df2 = df.groupby('batting_team')['crr'].max().sort_values(ascending=False)

    # Create a colorful bar chart using Plotly Express
    fig2 = px.bar(grouped_df2, title='Max Run Rate by Team')
    fig2.update_layout(xaxis_title='Team', yaxis_title='Max CRR')
    fig2.update_traces(marker_color=['#9370DB', '#8A2BE2', '#800080', '#9932CC'])
    fig2.update_layout(plot_bgcolor='white')
    st.plotly_chart(fig2)

#---------------------------------------------------------------------------------------

# Group the data by batting_teams and wickets_left, calculate the maximum values, and sort the results
grouped_df = df.groupby(['batting_team', 'wickets_left']).agg({'runs_x': 'max', 'crr': 'max'}).reset_index()
grouped_df_sorted = grouped_df.sort_values(['runs_x', 'crr'], ascending=False)

# Main Streamlit app
def main():

    st.write("Select a batting team and press 'Run Analysis' to perform analysis.")

    # Selectbox for batting team
    batting_teams = grouped_df_sorted['batting_team'].unique()
    selected_batting_team = st.selectbox("Select Batting Team", batting_teams)

    # Run Analysis button
    if st.sidebar.button("Run Analysis"):
        if selected_batting_team:
            # Filter the grouped and sorted DataFrame based on selected batting team
            filtered_df = grouped_df_sorted[grouped_df_sorted['batting_team'] == selected_batting_team]

            # Display the filtered DataFrame
            st.dataframe(filtered_df)

            # Plotting the bar chart with eye-catching and colorful styles
            fig3 = go.Figure()
            fig3.add_trace(go.Bar(x=filtered_df['wickets_left'], y=filtered_df['runs_x'], name='Runs_x',
                                  marker_color='#FFA07A'))
            fig3.add_trace(go.Bar(x=filtered_df['wickets_left'], y=filtered_df['crr'], name='CRR',
                                  marker_color='#9370DB'))
            fig3.update_layout(barmode='group', plot_bgcolor='#F0F2F6', paper_bgcolor='#F0F2F6')
            fig3.update_xaxes(showline=True, linewidth=1, linecolor='#333333')
            fig3.update_yaxes(showline=True, linewidth=1, linecolor='#333333')
            fig3.update_layout(title='Max Runs and CRR by Wickets Left', xaxis_title='Wickets Left',
                               yaxis_title='Values', font=dict(family='Arial', size=12, color='#333333'))
            fig3.update_traces(hovertemplate='<b>%{x}</b><br>%{y}', textposition='auto', textfont=dict(color='white'))

            st.plotly_chart(fig3)
        else:
            st.warning("Please select a batting team before running the analysis.")

# Run the app
if __name__ == "__main__":
    main()

