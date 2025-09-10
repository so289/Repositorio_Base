import streamlit as st
#---------------------------------------------SIDEBAR
st.sidebar.image('movida_logo.png')
st.sidebar.title('Movida - Aluguel de carros')
st.sidebar.write('Seja bem-vido(a)')

carros=['BMW','MUSTANG','HB20','FUSCA','CIVIC']
carro=st.sidebar.selectbox('Selecione um carro', carros)

valor_do_dia=0
if carro=='BMW':
 valor_do_dia=200

elif carro== 'MUSTANG':
  valor_do_dia=500

elif carro== 'HB20':
  valor_do_dia=150

elif carro=='FUSCA':
  valor_do_dia=300

elif carro=='CIVIC':
  valor_do_dia=200

else:
  valor_do_dia=60
  



#----------------------------------------------------PRINCIPAL
st.title ('Movida- aluguel de carros')
st.write('seja bem-vindo(a)')
st.image(f'{carro}.png')
dias= st.text_input('informe a quantidade de dias')
km= st.text_input('Informe a quantidade de quilometros percorridos') 
if st.button ('Calcular'):
    dias= int(dias)
    km= float(km)

    valor_dias= dias* valor_do_dia
    valor_km=km*0.15
    total= valor_dias + valor_km

st.warning(f'Voce roudou {km}km por {dias}dias. O valor a ser pago sera {total}.')