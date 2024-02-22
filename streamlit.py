import pickle
import base64
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Setting page congiuration and Background

st.set_page_config(page_title = 'price_Prediction',layout='wide') 

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('img1.png')

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #9899AA;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:white;'>Rental Price Predictions</h1>", unsafe_allow_html=True)

# Encoder instantiation
le = LabelEncoder()

# Reading the datasets
data = pd.read_csv('final_data.csv')
df1 = pd.read_csv('df_for_eda.csv')

# Decoding Label Encoded columns

def encoder(col):
    encoded_col = list(data[col].unique())
    original_col = list(df1[col].unique())
    col_dic = {}
    for key in original_col:
        for value in encoded_col:
            col_dic[key] = value
            encoded_col.remove(value)
            break
    return col_dic

Type = encoder('type')
l_type = encoder('lease_type')
furn = encoder('furnishing')
parking = encoder('parking')
direc = encoder('facing')
water = encoder('water_supply')
b_type = encoder('building_type')
local = encoder('locality')

c1,c2,c3 =  st.columns(3)

with c1:

    area = st.selectbox('Locality',options= list(local.keys()))
    area1 = local[area]

    lat = list(df1[df1['locality']== area]['latitude'])[0]

    long = list(df1[df1['locality']== area]['longitude'])[0]

    typ = st.selectbox('Locality',options= list(Type.keys()))
    typ1 = Type[typ]

    size = st.selectbox('Area(sqft)',options= list(data['property_size'].unique()))

    building = st.selectbox('Building Type',options= list(b_type.keys()))
    building1 = b_type[building]

    interior = st.selectbox('Furnishing',options= list(furn.keys()))
    interior1 = furn[interior]
    face = st.selectbox('Facing',options= list(direc.keys()))
    face1 = direc[face]
with c2:

    age = st.slider('Property Age', 1, 80, 10)

    tot = st.slider('Total floors', 0, 26, 0)

    floor = st.slider('Floor',0,25,0)

    wat = st.selectbox('Water Supply',options= list(water.keys()))
    wat1 = water[wat]

    par = st.selectbox('Parking',options= list(parking.keys()))
    par1 = parking[par]

    lease = st.selectbox('Lease Type',options = list(l_type.keys()))
    lease1 = l_type[lease]

with c3:    
    st.markdown("<h6 style='text-align: center; color:white;'>Activation Date</h6>", unsafe_allow_html=True)
    a1,a2,a3 = st.columns(3)
    with a1:
        day = st.selectbox('Day',options = list(range(1,32)))
    with a2:
        month = st.selectbox('Month',options = list(range(1,13)))
    with a3:
        year = st.selectbox('Year',options = [2017,2018])

    bal = st.selectbox('Balcony',options = [0,1,2,3,4,5])
    
    bath =st.selectbox('Bathrooms',options=[1,2,3,4,5,6,7])

    cup = st.slider('CupBoards',0,40,5)
    
    neg = st.selectbox('Negotiable',options = ['Yes','No'])
    if neg == 'Yes':
        neg1 = 1
    else:
        neg1 = 0

    value = st.multiselect('Amenities',['GYM','LIFT','SWIMMING_POOL', 'INTERNET','AC', 'CLUB', 'INTERCOM', 'CPA', 'FS', 'SERVANT',
       'SECURITY', 'SC', 'GP', 'PARK', 'RWH', 'STP', 'HK', 'PB', 'VP'],['AC'])    
    
    total_amen = len(value)
    
    if 'GYM' in value:
        GYM =1
    else:
        GYM = 0 
    if 'LIFT' in value:
        LIFT =1
    else:
        LIFT = 0 
    if 'SWIMMING_POOL' in value:
        SWIMMING_POOL =1
    else:
        SWIMMING_POOL = 0 
    if 'INTERNET' in value:
        INTERNET=1
    else:
        INTERNET = 0 
    if 'AC' in value:
        AC =1
    else:
        AC = 0 
    if 'CLUB' in value:
        CLUB =1
    else:
        CLUB= 0 
    if 'INTERCOM' in value:
        INTERCOM =1
    else:
        INTERCOM = 0 
    if 'CPA' in value:
        CPA=1
    else:
        CPA = 0 
    if 'FS' in value:
        FS =1
    else:
        FS = 0 
    if 'SERVANT' in value:
        SERVANT=1
    else:
        SERVANT = 0 
    
    if 'SECURITY' in value:
        SECURITY =1
    else:
        SECURITY = 0 
    if 'SC' in value:
        SC =1
    else:
        SC = 0 
    if 'GP' in value:
        GP =1
    else:
        GP = 0 
    if 'PARK' in value:
        PARK=1
    else:
        PARK= 0 
    if 'RWH' in value:
        RWH =1
    else:
        RWH = 0
    if 'STP' in value:
        STP =1
    else:
        STP = 0 
    if 'HK' in value:
        HK =1
    else:
        HK = 0 
    if 'PB' in value:
        PB =1
    else:
        PB = 0 
    if 'VP' in value:
        VP =1
    else:
        VP = 0 


button = st.button('Predict Rental Price')
if button:
    ip = [[typ1,area1,lat,long,lease1,GYM,LIFT,SWIMMING_POOL,neg1,interior1,par1,size,age,bath,face1,cup,floor,tot,wat1,building1,bal,INTERNET,AC,CLUB,INTERCOM,CPA,FS,SERVANT,SECURITY,SC,GP,PARK,RWH,STP,HK,PB,VP,day,month,year,total_amen]]

   
    with open('xg_model.pkl','rb') as file:
            model = pickle.load(file)

    pr = model.predict(np.array(ip))[0]
    price = round(pr,2)
    st.markdown(f'<h2 style="text-align: center;color:white;">Predicted Rental Price : ₹ {price} </h2>', unsafe_allow_html=True)
    
     



