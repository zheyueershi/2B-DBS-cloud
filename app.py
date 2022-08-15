#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates =float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1=model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2=model2.predict([[rates]])
        model3 = joblib.load("neural_network_DBS")
        r3=model3.predict([[rates]])
        return(render_template("index.html",result1=r1,result2=r2,result3=r3))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting",result3="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5002"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




