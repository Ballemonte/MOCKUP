from flask import Flask, render_template, request, flash

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():    
   return render_template('mockup1.html')
        