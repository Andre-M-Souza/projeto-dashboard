from flask import Flask, request
import json
import pdb

app = Flask(__name__)


@app.route("/")
def main():
    pass


@app.route("/users")
def usersvalue():
    f = open("./users/users.json")
    data = json.load(f)
    return data


@app.route("/passw", methods=['POST'])
def passw():

    passwok = ''

    passwd = request.get_json()
    f = open("./passw/passw.json")
    results = json.load(f)

    for y in results['passw']:
        if passwd['userText'] == y['username']:
            if passwd['passText'] == y['password']:
                passwok = 'OK'
                break

    return passwok


@app.route("/periods", methods=['POST'])
def periods():

    periods = []

    data = request.get_json()
    f = open("./results.json")
    results = json.load(f)

    for i in results:

        period = []
        v_ano = i[0][0:4]
        v_mes = i[0][4:6]

        if data['choosedoption']['value'] == 'Comparativo Mensal':
            v_period = str(v_ano) + '-' + str(v_mes)
            if v_period in periods:
                pass
            else:
                period.append(v_period)

        if data['choosedoption']['value'] == 'Comparativo Anual':
            v_period = str(v_ano)
            if v_period in periods:
                pass
            else:
                period.append(v_period)

        period.append(i[1])
        period.append(i[2])
        period.append(i[3])
        period.append(i[4])
        period.append(i[5])
        period.append(i[6])
        period.append(i[7])

        periods.append(period)

        if data['choosedoption']['value'] == 'Comparativo Mensal':
            periods_last = periods[-12:]
        else:
            periods_last = periods

    periods_json = json.dumps(periods_last)

    return periods_json


if __name__ == "__main__":
    app.run(debug=True)
