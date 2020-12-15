import pickle #Para cargar el modelo
import streamlit as st


#Cargamos el modelo del disco
pickle_in = open('finalized_model.sav', 'rb')    
clf = pickle.load(pickle_in)


def Prediccion(Gender, Education_Level, Marital_Status, Income_Category):
    
#Asignamos los valores recibidos del usuario

    if Gender == "M":
        M = 1
    else:
        M = 0
        
   # if Education_Level == "Collegiatura":
     #   College = 1
    #else:
      #  College = 0
        
    if Education_Level == "Graduado":
        Graduate = 1
    else:
        Graduate = 0
        
    if Education_Level == "Doctorado":
        Doctorate = 1
    else:
        Doctorate = 0
            
    if Education_Level == "Secundaria":
        HighSchool = 1    
    else:
        HighSchool = 0
            
    if Education_Level == "Post-Grado":
        PostGraduate = 1  
    else:
        PostGraduate = 0
        
    if Education_Level == "Desconocido":
        Unknown = 1  
    else:
        Unknown = 0
        
    if Education_Level == "Ninguno":
        Uneducated = 1 
    else:
        Uneducated = 0
        
   # if Marital_Status == "Divorciado":
  #      Divorced = 1
   # else:
    #    Divorced = 0
    
    if Marital_Status == "Casado":
        Married = 1
    else:
        Married = 0
        
    if Marital_Status == "Soltero":
        Single = 1 
    else:
        Single = 0
        
    if Marital_Status == "Desconocido":
        Unknown_marital = 1 
    else:
        Unknown_marital = 0
        
    #if Income_Category == "$120K +":
    #    K120 = 1 
    #else:
    #    K120 = 0
        
    if Income_Category == "$40K - $60K":
        K40K60 = 1 
    else:
        K40K60 = 0
        
    if Income_Category == "$60K - $80K":
        K60K80 = 1 
    else:
        K60K80 = 0
    
    if Income_Category == "$80K - $120K":
        K80K120 = 1 
    else:
        K80K120 = 0
        
    if Income_Category == "Menos de $40K":
        Less40K = 1 
    else:
        Less40K = 0
        
    if Income_Category == "Desconocido":
        Unknown_income = 1 
    else:
        Unknown_income = 0
        

    #Realizamos las predicciones
    
    predict = clf.predict([[M, Doctorate, Graduate, HighSchool, PostGraduate,Uneducated, Unknown, Married, Single, Unknown_marital,K40K60, K60K80, K80K120, Less40K, Unknown_income]])
    
  
        
    return predict
    #return M, College, Doctorate, Graduate, "High School", Post-Graduate, Unknown, Uneducated, Divorced, Married, Single, Unknown_marital, "$120K +", "$40K - $60K", "$60K - $80K", "$80K - $120K", "Less than $40K", Unknown_income 
        
def main():
    #Elementos del front end
    html_temp="""
    <div style ]="padding:13px">
    <h1 style = "color:black;text.align:center;">Proyecto IA para predecir la pérdida o rotación de clientes del banco</h1>
    </div>
    
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    st.write('Con este modelo podrás predecir la relación de los clientes con el banco según sus características')
    st.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    Gender = st.selectbox('Genero', ("Masculino", "Femenino"))
    Education_Level = st.selectbox('Nivel de educación', ("Graduado", "Secundaria", "Post-Grado", "Doctorado", "Ninguno", "Desconocido"))
    Marital_Status = st.selectbox('Estado Civil', ("Casado", "Soltero", "Desconocido"))
    Income_Category = st.selectbox('Rango de Ingresos', ("$40K - $60K", "$60K - $80K", "$80K - $120K","Menos de $40K", "Desconocido" ))
    #predict = Prediccion("F", "Doctorate", "Married", "Unknown")
   # resultado=""
    
  #  st.button("Realizar predicción")
    #[[M, College, Doctorate, Graduate, HighSchool, PostGraduate, Unknown, Uneducated, Divorced, Married, Single, Unknown_marital, K120, K40K60, K60K80, K80K120, Less40K, Unknown_income]])
    if st.button("Realizar predicción"):
        resultado = Prediccion(Gender, Education_Level, Marital_Status, Income_Category)
        if resultado == 1:
            prediccion = "Cliente con relación existente en el banco"
        else:
            prediccion = "Cliente con relación abandonada"
        st.write("La predicción para estos datos es: {}".format(prediccion))
        st.write(resultado)
        
if __name__ == "__main__":
	main()
