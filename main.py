#_________________________________import all dependencies_______________________________________________________________
import pandas as pd
import numpy as np
import plotly_express as px
from PIL import Image
import streamlit as st
import babel.numbers
#_________________________________Set Page fig__________________________________________________________________________
st.set_page_config(layout="wide")
#_________________________________Import/Config Chainalysis logos_______________________________________________________
# #insert background logo
Space_col1,Photo_col2,Space_col3=st.columns(3)
with Space_col1:
    "\n"
with Photo_col2:
    ChainalysisLogo1=Image.open("Chainalysis_Logo.png")
    st.image(ChainalysisLogo1, width=290)
with Space_col3:
    "\n"
#insert background logo
ChainalysisLogo2=Image.open("Logo0.png")
st.image(ChainalysisLogo2, use_column_width="always")
"\n"
#_________________________________Introduction Body Text _______________________________________________________________
st.subheader("Introduction")
st.write("<div style='text-align:justify'> ""\n"
         "Satoshi Nakamoto once said, “A lot of people automatically dismiss e-currency as a lost cause because of all the "
         "companies that failed since the 1990’s. I hope it’s obvious it was only the centrally controlled nature of those "
         "systems that doomed them. I think this is the first time we’re trying a decentralized, non-trust-based system.”"
         " This vision of Satoshi Nakamoto was apparent more than ever soon after the 2019 Bitcoin halving. More specifically, "
         "2020-2021 showcased the possibility of cryptocurrency and its adoption for multitudes of use cases. The utilization of decentralized "
         "ledger technology ( DLT) can be observed throughout the world; from the small sub-region of Micronesia to the sub-region of North America. "
         "With the help of on-chain data, transactions from any respective blockchain ledger can be studies and interpreted to aid enterprise functions. "
         "To emphasize this point, this analysis report answers fundamental questions associated with received and deposited transactions throughout the world. "
         "The questions below are analyzed to better understand the geographic distribution of cryptocurrency funds. Further, compelling evidence affiliated with "
         "the volume of these transactions based on a specific time period is discussed. The overarching goal of this report is to inform the reader about cryptocurrency "
         "usage worldwide through statistical methods, and data visualization.",unsafe_allow_html=True)
"\n"
#_________________________________Import Statistical Questions _________________________________________________________
st.info("""
    * Which top 5 sub-regions have received and deposited the most funds during 2019 – 2022? 
    * Within the top 5 sub-regions, which top nation are these transactions originating from?  
    * Within the top 5 sub-regions, which sub-region display most distributed volume of received transactions and what may be the reason(s) for it?
    * Which top 2 sub-regions show the lowest volume of deposits and which countries contribute to this output?
    * For the selected top 5 sub-regions, when are majority of the transactions (received and deposits) taking place?  
    * What are the catalysts that contributed to the enormous growth of cryptocurrency activity during 2020-2021? 
    """)
st.write("____")
#_________________________________Import/Dispaly data___________________________________________________________________
"\n"
#interpredation bodytext
st.subheader("On-chain Cryptocurrency Value Received and Deposits From 2019 - 2022")
df=pd.read_csv("Geography_Analyst_Data_Assignment.csv")
st.dataframe(df)
st.write("<div style='text-align:justify'> ""\n"
         "The table above expresses received and deposit transactions from around the world. The table is interactive and "
         "can be filtered via each respect attribute. The ranking of each sub-regions and countries can be identified by sorting "
         "received or deposited transactions."
         ,unsafe_allow_html=True)
st.write("____")
#_________________________________Visulization histogram charts_________________________________________________________
#sub-regions
st.subheader("Top 5 Sub-regions with Most Transaction Volume During  2019 - 2022")
SubRegion_TotalTransac_plot0=px.histogram(df,x="final_sub_region",y=["final_received_usd","final_deposits"],
                        title="Sub-Region: Received Funds vs. Deposits | Mar '19 - Apr '22",width=1360, height=500)
SubRegion_TotalTransac_plot0.update_layout(legend_title="Transaction Type",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total descending'})
SubRegion_TotalTransac_plot0.update_yaxes(title="Sum of Transactions ($)")
SubRegion_TotalTransac_plot0.update_xaxes(title="Sub-Region")
#SubRegion_TotalTransac_plot0.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(SubRegion_TotalTransac_plot0)
#sub-regions
st.subheader("Top Country with the Most Total Value Received During  2019 - 2022")
Country_TotalTransac_plot0=px.histogram(df,x="final_country",y=["final_received_usd","final_deposits"],
                        title="Country: Received Funds vs. Deposits | Mar '19 - Apr '22",width=1360, height=700)
Country_TotalTransac_plot0.update_layout(legend_title="Transaction Type",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total descending'})
Country_TotalTransac_plot0.update_yaxes(title="Sum of Transactions ($)")
Country_TotalTransac_plot0.update_xaxes(title="Country")
st.plotly_chart(Country_TotalTransac_plot0)
"\n"
"\n"
                        #_____________________calculation/display metrics_______________
#calculate the sum of both final_received_usd and final_deposits
SUM_Received_funds=df["final_received_usd"].sum()
SUM_Deposited_funds=df["final_deposits"].sum()
#calculate the sum of each respective region for metric formation
A=df.loc[df["final_sub_region"]=="Eastern Asia"].sum()
B=df.loc[df["final_sub_region"]=="Northern America"].sum()
C=df.loc[df["final_sub_region"]=="Eastern Europe"].sum()
D=df.loc[df["final_sub_region"]=="Western Europe"].sum()
E=df.loc[df["final_sub_region"]=="Latin America and the Caribbean"].sum()
#calculate total Received and Deposited transactions against top 5 regions for metric output
TotalReceived_Top5Regions=A["final_received_usd"]+B["final_received_usd"]+C["final_received_usd"]+D["final_received_usd"]+E["final_received_usd"]
TotalDeposits_Top5Regions=A["final_deposits"]+B["final_deposits"]+C["final_deposits"]+D["final_deposits"]+E["final_deposits"]
TotalReceived_Top5Regions_USDConversion=babel.numbers.format_currency(float(TotalReceived_Top5Regions), "USD", locale='en_US')
TotalDeposits_Top5Regions_USDConversion=babel.numbers.format_currency(float(TotalDeposits_Top5Regions), "USD", locale='en_US')
#Calculate percentage of total received and deposited transactions for top 5 regions
Top5_VS_TotalReceived=(TotalReceived_Top5Regions/SUM_Received_funds)
Top5_VS_TotalDeposits=format((TotalDeposits_Top5Regions/SUM_Deposited_funds)*100,".2f")
#insert metric columns
metric_col0,metric_col1,metric2=st.columns(3)
metric_col0.metric("Top Sub-regions", "5")
metric_col1.metric("Total Cryptocurrency Value Received", TotalReceived_Top5Regions_USDConversion)
with metric2:
    percent_metric="{:.0%}".format(Top5_VS_TotalReceived)
    st.metric(" Market Share of Total Worldwide Value Received", percent_metric)
#interpredation bodytext
st.write("<div style='text-align:justify'> ""\n"
         "Eastern Asia, Northern America, Eastern Europe, Latin America and the Caribbean as well as Western Europe make "
         "up the top 5 sub-regions with the largest total received value. Together they make up $17,575,237,887,498.85, which "
         "is 59.43% of the total received funds from all sub-regions. The United States ranks 1st for the nation with largest volume"
         " of cryptocurrency value received. The transactions in the United States accrue to approximately $3.07 trillion."
         ,unsafe_allow_html=True)
"\n"
                            #_____________________insert figure button_______________
PlotA_button=st.expander(label="figures 1.0 - 1.B : Sub-region, Country Total Received and Deposits Transactions")
PlotA_button.write("""
    Note: Chart is interactive, select transaction type for comparison, Zoom in for low volume data points
    
    figures 1.0 : Data transactions  
    
    figures 1.A : Sub-region total Received and Deposits 
    
    figures 1.B : Country total Received and Deposits 
    
    Datasource: Chainalysis
    
    Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
st.write("____")
#recieved
st.subheader("The Sub-region in the Top 5 with Most Distributed Value Received per Country During  2019 - 2022")
received_TotalTransac_plot0=px.histogram(df,x="final_sub_region" ,y="final_received_usd", color="final_country",
                        title="Received Funds vs. Sub-Region per Country | Mar '19 - Apr '22",width=1360, height=500)
received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total descending'})
received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)")
received_TotalTransac_plot0.update_xaxes(title="Sub-Region")
st.plotly_chart(received_TotalTransac_plot0)
#deposits
"\n"
#interpredation bodytext
st.write("<div style='text-align:justify'> ""\n"
         "The sub-region of Latin America and the Caribbean is the 4th largest sub-region based on its volume of value received "
         "More importantly, the sub-region displays a volume that is more evenly distributed among all countries compare to other sub-regions "
         "in the selected top 5. Among all 30+ nations, Argentina and Brazil are responsible for majority of the value received in the region, "
         "which accounts for a total of approximately 1.53 trillion dollars. It is no surprise Latin America ranks 4th as many of these nations "
         "utilize cryptocurrency to transact internationally for remittance and other commercial use cases. Aside from El Salvador adopting Bitcoin "
         "as a legal tender, the sub-region accounts for $134 billion in remittance according to Statista."
         ,unsafe_allow_html=True)
"\n"
"\n"
#deposite
st.subheader("Top 2 Sub-regions with the Least Deposits per Country During  2019 - 2022")
deposits_TotalTransac_plot0=px.histogram(df,x="final_sub_region" ,y="final_deposits", color="final_country",
                                         title="Deposits vs. Sub-Region per Country | Mar '19 - Apr '22",width=1360, height=500)
deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total ascending'})
deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposit Transactions ($)")
deposits_TotalTransac_plot0.update_xaxes(title="Sub-Region")
st.plotly_chart(deposits_TotalTransac_plot0)
"\n"
#interpredation bodytext
st.write("<div style='text-align:justify'> ""\n"
         "Although North America leads in most value deposits, Micronesia and Polynesia ranks as top two sub-region with least cryptocurrency value deposits "
         "French Polynesia and Guam together accumulate for approximately $611,924 in deposits."
         ,unsafe_allow_html=True)
"\n"
#_____________________insert figure button_______________
PlotB_button=st.expander(label="figures 2.0 - 2.A : Sub-region Total Received and Deposits Transactions per country")
PlotB_button.write("""
    Note: Chart is interactive, select country for comparison, Zoom in for low volume data points
    
    figures 2.0 : Received Funds vs. Sub-region per country 
    
    figures 1.A : Deposits Funds vs. Sub-region per country   
    
    Datasource: Chainalysis
    
    Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
st.write("___")
#_________________________________Create/Display DF for Eastern Asia_____________________________________________________
Eastern_Asia_Df=df.loc[df["final_sub_region"]=="Eastern Asia"]
#st.dataframe(Eastern_Asia_Df)
#_________________________________Visulization line charts______________________________________________________________
st.subheader("2020 - 2021 Led to an Increase of Cryptocurrency Value Received")
#EasternAsia_Recieved
EasternAsia_Received_TotalTransac_plot0=px.line(Eastern_Asia_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                         title="Eastern Asia: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
EasternAsia_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
EasternAsia_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
EasternAsia_Received_TotalTransac_plot0.update_xaxes(showgrid=False,title="Date")
st.plotly_chart(EasternAsia_Received_TotalTransac_plot0)
#EasternAsia_Deposits
EasternAsia_Deposits_TotalTransac_plot0=px.line(Eastern_Asia_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                title="Eastern Asia: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
EasternAsia_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
EasternAsia_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
EasternAsia_Deposits_TotalTransac_plot0.update_xaxes(showgrid=False,title="Date")
#st.plotly_chart(EasternAsia_Deposits_TotalTransac_plot0)
#_________________________________Create/Display DF for North America_____________________________________________________
Northern_America_Df=df.loc[df["final_sub_region"]=="Northern America"]
#Northern_America_Df
#_________________________________Visulization line charts______________________________________________________________
#NorthAmerica_Recieved
NorthAmerica_Received_TotalTransac_plot0=px.line(Northern_America_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                title="North America: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
NorthAmerica_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
NorthAmerica_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
NorthAmerica_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
st.plotly_chart(NorthAmerica_Received_TotalTransac_plot0)
#NorthAmerica_Deposits
NorthAmerica_Deposits_TotalTransac_plot0=px.line(Northern_America_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                title="North America: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
NorthAmerica_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
NorthAmerica_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
NorthAmerica_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
#st.plotly_chart(NorthAmerica_Deposits_TotalTransac_plot0)
#interpredation bodytext
st.write("<div style='text-align:justify'> ""\n"
         "When looking at the biggest sub-region for value received, China appears to be the country with the largest volume of "
         "received transactions over the given time period. Between March, 2019 and Oct 2020, China shows a relatively constant trend. "
         "We see a significant positive trend during Oct 2020 and May 2021, resulting to an 8.2 multiple. The volume of received transactions "
         "jumped from 30.53 billion dollars to 251.43 billion dollars. Soon after, we see a tremendous bull-back as low as 20.32 billion dollars. "
         "The Republic of Korea, Japan, Taiwon followed the China trend with a much lower volume.",unsafe_allow_html=True)
"\n"
#interpredation bodytext
st.write("<div style='text-align:justify'> ""\n"
         "United States leads in volume of value received within North America in the given time period. The volume remains "
         "predictably constant for most of the time period until Oct 2020, where the volume increases from 29.55 billion dollars to 337.84 billions dollars in May 2021."
         "The total received funds increased by a multiple of 11.43. This is a significant increase in less than 12 months. Canada mimics the trend of the United States "
         "with a lower volume. Bermuda remained constant with no noticeable improvement in value received.",unsafe_allow_html=True)
"\n"
#_____________________insert figure button_______________
PlotC_button=st.expander(label="figures 3.0 - 3.A : Eastern Asia and Northern America Monthly Value Received per Country")
PlotC_button.write("""
    Note: Chart is interactive, select country for comparison, Zoom in for low volume data points
    
    figures 3.0 : Eastern Asia: Monthly Value Received Per Country
    
    figures 3.A : Northern America: Monthly Value Received Per Country   
    
    Datasource: Chainalysis
    
    Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
st.write("___")

#_________________________________Create/Display DF for Eastern Europe_____________________________________________________
Eastern_Europe_Df=df.loc[df["final_sub_region"]=="Eastern Europe"]
#Eastern_Europe_Df
#_________________________________Visulization line charts______________________________________________________________
#EasternEurope_Recieved
EasternEurope_Received_TotalTransac_plot0=px.line(Eastern_Europe_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                 title="Eastern Europe: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
EasternEurope_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
EasternEurope_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
EasternEurope_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
#st.plotly_chart(EasternEurope_Received_TotalTransac_plot0)
#EasternEurope_Deposits
EasternEurope_Deposits_TotalTransac_plot0=px.line(Eastern_Europe_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                 title="Eastern Europe: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
EasternEurope_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
EasternEurope_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
EasternEurope_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
#st.plotly_chart(EasternEurope_Deposits_TotalTransac_plot0)
"\n"
"\n"
st.write("___")
#_________________________________Create/Display DF for LatinAmerica & Caribbean_____________________________________________________
LatinAmerica_Caribbean_Df=df.loc[df["final_sub_region"]=="Latin America and the Caribbean"]
#LatinAmerica_Caribbean_Df
#_________________________________Visulization line charts______________________________________________________________
#WesternEurope_Recieved
st.subheader("2020 - 2021 Led to an Increase of Cryptocurrency Deposits")
LatinAmerica_Caribbean_Received_TotalTransac_plot0=px.line(LatinAmerica_Caribbean_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                           title="Latin America and the Caribbean: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
LatinAmerica_Caribbean_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
LatinAmerica_Caribbean_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
LatinAmerica_Caribbean_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
#st.plotly_chart(LatinAmerica_Caribbean_Received_TotalTransac_plot0)
#WesternEurope_Deposits
LatinAmerica_Caribbean_Deposits_TotalTransac_plot0=px.line(LatinAmerica_Caribbean_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                           title="Latin America and the Caribbean: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
LatinAmerica_Caribbean_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
LatinAmerica_Caribbean_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
LatinAmerica_Caribbean_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
st.plotly_chart(LatinAmerica_Caribbean_Deposits_TotalTransac_plot0)
#_________________________________Create/Display DF for Western Europe_____________________________________________________
Western_Europe_Df=df.loc[df["final_sub_region"]=="Western Europe"]
#Western_Europe_Df
#_________________________________Visulization line charts______________________________________________________________
#WesternEurope_Recieved
WesternEurope_Received_TotalTransac_plot0=px.line(Western_Europe_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                  title="Western Europe: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
WesternEurope_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
WesternEurope_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
WesternEurope_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
#st.plotly_chart(WesternEurope_Received_TotalTransac_plot0)
#WesternEurope_Deposits
WesternEurope_Deposits_TotalTransac_plot0=px.line(Western_Europe_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                  title="Western Europe: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
WesternEurope_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
WesternEurope_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
WesternEurope_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
st.plotly_chart(WesternEurope_Deposits_TotalTransac_plot0)
#interpredation bodytext
st.write("<div style='text-align:justify'> ""\n"
         "The sub-region of the Latin America and the Caribbean show significant volume distribution among all the respective "
         "countries when it comes to value received and deposits. Unlike previous value received charts, the activity level noticeable "
         "since March 1, 2019, especially in Brazil. Drastic increase in deposits begin on July 2020. Brazil, the leading country, shows significant increase from 1.11 million dollars to 4.59 million dollars. "
         "This increase is a 4.13x from its volume on July 1, 2020. Similarly, most of the countries in the sub-region experience an enormous increase in deposits. During this bull-run, some countries with"
         "increasing deposit activity are; Argentina(3.35 million dollars), Venezuela (1.51 million dollars), Mexico (1.50 million dollars), Columbia (1.11 million dollars), Chile "
         "(954.13 thousand dollars), Peru (693.92 thousand dollars), Dominican Republic (454.73 thousand dollars). A deeper look of the data of all "
         "the countries in the sub-region illustrates a widespread of the total cryptocurrency value deposits",unsafe_allow_html=True)
"\n"
"\n"
st.write("<div style='text-align:justify'> ""\n"
         "In the sub-region of Western Europe, more fluctuation in the total volume of deposits is apparent from March 1, 2019 to May 1, 2021."
         "Many peaks and valleys can be identified from December 1, 2019 to present time. May 1, 2021 and Jan 1, 2022 appears to be the peaks with the highest deposit volume "
         "for Germany as the leader. The volume rose from 555.05 thousand dollars to 4.23 million dollars in deposits. With a similar trend, Germany, France and the Netherlands "
         "are the leading nations in the sub-region of Western Europe. Luxembourg, Monaco and Liechtenstein show very little asctivity in compare to the leading countries. "
        ,unsafe_allow_html=True)
"\n"
#_____________________insert figure button_______________
PlotD_button=st.expander(label="figures 4.0 - 4.A : Latin America and the Caribbean and Western Europe Monthly Deposits per Country")
PlotD_button.write("""
    Note: Chart is interactive, select country for comparison, Zoom in for low volume data points
    
    figures 4.0 : Latin America and the Caribbean: Monthly Deposits Per Country
    
    figures 4.A : Western Europe: Monthly Deposits Per Country   
    
    Datasource: Chainalysis
    
    Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
st.write("___")
#_____________________insert figure button_______________
st.subheader("Catalysts Associated with the 2020 - 2021 Increase of Cryptocurrency Activity ")
st.info("""
    * 2020 Bitcoin Halving
    * COVID-19 Pandemic 
    * Quantitative Easing (QE) by Central Governments Worldwide
    * Institutional Defi activity
    * Peer-to-peer Platforms 
    """)
st.write("____")
#insert button for references
References=st.expander(label="REFERENCES")
References.write("""
    
    [Chainalysis ]
        (on-chain data)
    
    [Value of remittances received in selected countries in Latin America in 2021]
        (https://www.statista.com/statistics/439126/value-of-remittances-received-latin-america-by-country/#:~:text=In%202021%2C%20Mexico%20received%20nearly,amounting%20to%2015.3%20billion%20dollars.)
   
    ["Quantitative easing in the U.S. - statistics & facts"]
        (https://www.statista.com/statistics/439126/value-of-remittances-received-latin-america-by-country/#:~:text=In%202021%2C%20Mexico%20received%20nearly,amounting%20to%2015.3%20billion%20dollars.)
    
    [chainalysis.com, Chainalysis Research Team (2021), "2021 Geography of Cryptocurrency Report"]
        (https://go.chainalysis.com/2021-geography-of-crypto.html)
    
    """)
st.write("____")
st.info("Download Report 👇")
#Insert report for Download
with open("2022 Geography of Cryptocurrency Report.pdf", "rb") as file:
    Button = st.download_button(
        label="2022 Geography of Cryptocurrency Report ",
        data=file,
        file_name="2022 Geography of Cryptocurrency Report.pdf",
        mime="image/png")
