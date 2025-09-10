import  streamlit as st
st.title('VENDAS DE CASAS')
st.write('Seja bem vindo(a)!!')


#------------------------------------------------SIDEBAR
st.sidebar.title('VENDAS DE CASAS')
st.sidebar.write('Seja bem vindo(a)!!')

casas= ['CASA AZUL(4 CÔMODOS)','CASA ROSA(8 CÔMODOS)','CASA AMARELA(2 CÔMODOS)','CASA BRANCA(10 CÔMODOS)']
casa = st.sidebar.selectbox('Selecione uma das casas:', casas)

if casa=='CASA AZUL(4 CÔMODOS)':
    aluguel= 1500 
    comprar=150.000

if casa== 'CASA ROSA(8 CÔMODOS)':
    aluguel= 2000
    comprar= 400.000

if casa=='CASA AMARELA(2 CÔMODOS)':
    aluguel= 1000
    comprar= 100.000

if casa=='CASA BRANCA(10 CÔMODOS)':
    aluguel= 10.000
    comprar= 10000.000

#-----------------------------------------------PRINCIPAL


st.title(casa)
col1, col2 = st.columns(2)

with col1:
    st.write('Alugar')
    st.write(aluguel)
with col2:
    st.write('Comprar')
    st.write(comprar)
st.image(f'{casa}.png')