from flask import Flask, render_template, request
import os, math

app = Flask(__name__)

template_dir = os.path.abspath('templates')
app.template_folder = template_dir

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    Base_LV = float(request.form['Base_LV'])
    Max_HP = float(request.form['Max_HP'])
    Max_SP = float(request.form['Max_SP'])
    Vit = float(request.form['Vit'])
    Int = float(request.form['Int'])
    Add_HP = float(request.form['Add_HP'])
    Add_SP = float(request.form['Add_SP'])
    Perc_HP = float(request.form['Perc_HP'])
    Perc_SP = float(request.form['Perc_SP'])
    Perc_Skill = float(request.form['Perc_Skill'])
    Perc_LR = float(request.form['Perc_LR'])

    Base_HP = ((Max_HP/(Perc_HP*0.01 + 1)) - Add_HP)/(Vit*0.01 + 1)/1.25
    Base_SP = ((Max_SP/(Perc_SP*0.01 + 1)) - Add_SP)/(Int*0.01 + 1)/1.25
    DB_Damage = (((math.floor(Max_HP/50)+math.floor(Max_SP/4))*10*Base_LV/100*1.4)-5)*(Perc_Skill*0.01+1)*(Perc_LR*0.01+1)

    Vit_new = float(request.form['Vit_new'])
    Int_new = float(request.form['Int_new'])
    Add_HP_new = float(request.form['Add_HP_new'])
    Add_SP_new = float(request.form['Add_SP_new'])
    Perc_HP_new = float(request.form['Perc_HP_new'])
    Perc_SP_new = float(request.form['Perc_SP_new'])
    Perc_Skill_new = float(request.form['Perc_Skill_new'])
    Perc_LR_new = float(request.form['Perc_LR_new'])

    Max_HP_new = (Base_HP*1.25*(Vit_new*0.01 + 1)+Add_HP_new)*(Perc_HP_new*0.01 + 1)
    Max_SP_new = (Base_SP*1.25*(Int_new*0.01 + 1)+Add_SP_new)*(Perc_SP_new*0.01 + 1)
    DB_Damage_new = (((math.floor(Max_HP_new/50)+math.floor(Max_SP_new/4))*10*Base_LV/100*1.4)-5)*(Perc_Skill_new*0.01+1)*(Perc_LR_new*0.01+1)

    return {
        'Base_HP': math.floor(Base_HP),
        'Base_SP': math.floor(Base_SP),
        'DB_Damage': math.floor(DB_Damage),
        'Max_HP_new': math.floor(Max_HP_new),
        'Max_SP_new': math.floor(Max_SP_new),
        'DB_Damage_new': math.floor(DB_Damage_new)
    }

if __name__ == '__main__':
    app.run()