from __main__ import app
from flask import Flask, render_template, request,make_response,redirect
import json 
@app.route('/extentions')
def extentions():
  return render_template('extentions/index.html')