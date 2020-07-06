from flask import Flask, render_template, redirect, request, url_for
from data import *
from Explanation import *


app = Flask(__name__)


@app.route('/')
@app.route('/<int:num>')
def inputTest():

    return render_template('test.html', data_1=data_1, data_2=data_2)


@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        user_data = []
        for item in request.form:
            user_data.append(request.form[item])
        print(user_data)

        result = {'다':0, '담':0, '우':0, '점':0}
        for i in user_data:
            if i in pros_temperament_dic:
                result[pros_temperament_dic[i]] += 1
            else:
                result[cons_temperament_dic[i]] += 1
        print(result)


        user_result = {'Bloody':result['다'], 'gall':result['담'], 'depressed':result['우'], 'mucus':result['점']}
        '''
        if max(user_result.values()) > 19:
            v = list(user_result.values())
            k = list(user_result.keys())
            user_temperament = k[v.index(max(v))]
            result_explanation = explanation_dic[user_temperament]
            user_temperament_summary = user_temperament + '_summary'
            result_explanation_summary = explanation_dic[user_temperament_summary]
            image = 'only.jpg'
            return render_template('result.html', image=image, result_explanation=result_explanation,
                                   result_explanation_summary=result_explanation_summary)
        '''
        v = list(user_result.values())
        k = list(user_result.keys())
        first_user_temperament = k[v.index(max(v))]
        k.remove(first_user_temperament)
        v.remove(max(v))
        second_user_temperament = k[v.index(max(v))]

        user_temperament = first_user_temperament + '_' + second_user_temperament
        user_temperament_summary = user_temperament + '_summary'

        imagee = image_dic[user_temperament]
        image = imagee + '.jpg'
        print(image)
        result_explanation = '설명 : ' + explanation_dic[user_temperament]
        result_explanation_summary = explanation_dic[user_temperament_summary]



        ko_ex = en_ko[user_temperament]
        ko_im = image_dic_ko[user_temperament]
        subject = '당신은 ' + ko_ex + '(' + ko_im + ')' + ' 입니다.'
        print(v)
        print(k)
        print(user_result)
        print('33')
        print(user_temperament)


        '''
        print(user_result)      
        print(max(user_result.values()))       
        print(user_temperament)
        print(result_explanation)
        '''

    else:
        user_data = None
    return render_template('result.html',subject = subject,image = image, result_explanation=result_explanation, result_explanation_summary = result_explanation_summary)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
