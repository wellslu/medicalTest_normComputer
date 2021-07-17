# coding: utf-8
from flask import Flask, request
from flask import render_template
import wms_measure
import benson_measure
import clock_drawing_measure
import TVLT_measure
import CTT_measure

app = Flask(__name__, template_folder='templates')
wm = wms_measure.WMN()
bn = benson_measure.Benson()
cd = clock_drawing_measure.Clock_Drawing()
tvlt = TVLT_measure.TVLT()
ctt = CTT_measure.CTT()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        html = str(render_template('temp.html'))
        try:
            return html
        except:
            return '出錯了，請重新整理或通知技術人員'

    if request.method == 'POST':
        age = request.values.get('age')
        gender = request.values.get('gender')
        edu = request.values.get('education')
        lm1_score = request.values.get('LM-1 score')
        lm2_score = request.values.get('LM-2 score')
        dsf_score = request.values.get('DSF score')
        dsb_score = request.values.get('DSB score')
        symbol_score = request.values.get('symbol score')
        bfc_score = request.values.get('BFC score')
        bfr_score = request.values.get('BFR score')
        cdt_score = request.values.get('CDT score')
        tvltir_score = request.values.get('TVLTIR score')
        tvltdr_score = request.values.get('TVLTDR score')
        tvltdi_score = request.values.get('TVLTDI score')
        ctt1_time_score = request.values.get('CTT1-time score')
        ctt1_error_score = request.values.get('CTT1-error score')
        ctt1_approach_error_score = request.values.get('CTT1-approach-error score')
        ctt1_hint_score = request.values.get('CTT1-hint score')
        ctt2_time_score = request.values.get('CTT2-time score')
        ctt2_color_error_score = request.values.get('CTT2-color-error score')
        ctt2_number_error_score = request.values.get('CTT2-number-error score')
        ctt2_approach_error_score = request.values.get('CTT2-approach-error score')
        ctt2_hint_score = request.values.get('CTT2-hint score')
        ctt_interference_index_score = request.values.get('CTT-interference-index score')

        # try:
        message = ''
        if age == '':
            message += '未輸入年齡'
        if gender == '':
            message += '未輸入性別'
        if edu == '':
            message += '未輸入教育程度'

        class_list = []
        lm1_z_score, lm1_percent, lm1_table_score = wm.measure(age, lm1_score, 'LM-1')
        lm2_z_score, lm2_percent, lm2_table_score = wm.measure(age, lm2_score, 'LM-2')
        dsf_z_score, dsf_percent, dsf_table_score = wm.measure(age, dsf_score, 'DSF')
        dsb_z_score, dsb_percent, dsb_table_score = wm.measure(age, dsb_score, 'DSB')
        symbol_z_score, symbol_percent, symbol_table_score = wm.measure(age, symbol_score, '符號替代')
        bfc_z_score, bfc_percent, bfc_class = bn.measure(age, bfc_score, edu, 'BFC')
        class_list.append(bfc_class)
        bfr_z_score, bfr_percent, bfr_class = bn.measure(age, bfr_score, edu, 'BFR')
        class_list.append(bfr_class)
        cdt_z_score, cdt_percent, cdt_class = cd.measure(age, cdt_score, edu)
        class_list.append(cdt_class)
        tvltir_z_score, tvltir_percent, tvltir_class = tvlt.measure(age, tvltir_score, 'TVLTIR')
        class_list.append(tvltir_class)
        tvltdr_z_score, tvltdr_percent, tvltdr_class = tvlt.measure(age, tvltdr_score, 'TVLTDR')
        class_list.append(tvltdr_class)
        tvltdi_z_score, tvltdi_percent, tvltdi_class = tvlt.measure(age, tvltdi_score, 'TVLTDI')
        class_list.append(tvltdi_class)
        ctt1_time_percent = ctt.measure(age, ctt1_time_score, edu, gender, 'CTT1-time')
        ctt1_error_percent = ctt.measure(age, ctt1_error_score, edu, gender, 'CTT1-error')
        ctt1_approach_error_percent = ctt.measure(age, ctt1_approach_error_score, edu, gender, 'CTT1-approach-error')
        ctt1_hint_percent = ctt.measure(age, ctt1_hint_score, edu, gender, 'CTT1-hint')
        ctt2_time_percent = ctt.measure(age, ctt2_time_score, edu, gender, 'CTT2-time')
        ctt2_color_error_percent = ctt.measure(age, ctt2_color_error_score, edu, gender, 'CTT2-color-error')
        ctt2_number_error_percent = ctt.measure(age, ctt2_number_error_score, edu, gender, 'CTT2-number-error')
        ctt2_approach_error_percent = ctt.measure(age, ctt2_approach_error_score, edu, gender, 'CTT2-approach-error')
        ctt2_hint_percent = ctt.measure(age, ctt2_hint_score, edu, gender, 'CTT2-hint')
        ctt_interference_index_percent = ctt.measure(age, ctt_interference_index_score, edu, gender, 'CTT-interference-index')

        html = render_template('temp.html', lm1zs=lm1_z_score, lm1100=lm1_percent, lm2zs=lm2_z_score,
                               lm2100=lm2_percent, bsfzs=dsf_z_score, bsf100=dsf_percent, dsbzs=dsb_z_score,
                               dsb100=dsb_percent, symbolzs=symbol_z_score, symbol100=symbol_percent,
                               BFCzs=bfc_z_score, BFC100=bfc_percent, BFRzs=bfr_z_score, BFR100=bfr_percent,
                               CDTzs=cdt_z_score, CDT100=cdt_percent, TVLTIRzs=tvltir_z_score, TVLTIR100=tvltir_percent,
                               TVLTDRzs=tvltdr_z_score, TVLTDR100=tvltdr_percent, TVLTDIzs=tvltdi_z_score,
                               TVLTDI100=tvltdi_percent, CTT1time100=ctt1_time_percent, CTT1error100=ctt1_error_percent,
                               CTT1approacherror100=ctt1_approach_error_percent, CTT1hint100=ctt1_hint_percent,
                               CTT2time100=ctt2_time_percent, CTT2colorerror100=ctt2_color_error_percent,
                               CTT2numbererror100=ctt2_number_error_percent,
                               CTT2approacherror100=ctt2_approach_error_percent, CTT2hint100=ctt2_hint_percent,
                               CTTinterferenceindex100=ctt_interference_index_percent, message=message)

        for each_class in class_list:
            if each_class != '':
                html = html.split(f"{each_class}'>")
                html = html[0] + f"{each_class}'>✓" + html[1]

        return html

        # except:
        #     return '出錯了，請重新整理或通知技術人員'


if __name__ == '__main__':
    print('main page: http://127.0.0.1:5000/')
    app.debut = True
    app.run()
