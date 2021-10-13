import sys 
from PyQt5 import QtGui,uic
from PyQt5.QtWidgets import *
import math


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self = uic.loadUi('bmi.ui',self)
        self.setWindowTitle('BMI Calculator')

        self.btn_cal.clicked.connect(self.cal_)

        self.rdg_bmi = QButtonGroup()
        self.rdg_bmi.addButton(self.rdg_m)
        self.rdg_bmi.addButton(self.rdg_g)

        self.show()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def cal_(self):
        weight_ = float(self.le_weight.text())
        heigt_ = (float(self.le_height.text())/100)

        bmi_result = math.ceil(weight_/(heigt_**2))

        self.le_result.setText(str(bmi_result))

        #*-------------------------------------------------------------------------------------------------------------------------------------------------------------

    
        if self.rdg_m.isChecked():  #!--- เลือกผู้ชาย

            if bmi_result <= 18.5:
                
                self.la_pix.setPixmap(QtGui.QPixmap('verythin.png'))                   #!----.setPixmap (QtGui.QPixmap ('..... . png))  เป็นการใส่รูปภาพให้เเสดงออกมา เมื่อตรงเงื่อนไข

                self.pix_ins.setPixmap(QtGui.QPixmap('under.png'))                     #!----.setPixmap (QtGui.QPixmap ('..... . png))  เป็นการใส่รูปภาพ indicator ให้เเสดง การเคลื่อนไหว

                self.la_tex.setText('Under Weight ไปหางานเเละซื้อข้าวเเดกซะ')

                self.te_edit.setText('น้ำหนักน้อยกว่ามาตรฐาน \nค่าดัชนีมวลกายมีค่าน้อยกว่า 18.50 \n   1. ควรกินอาหารให้หลากหลายครบ 5 หมู่ในสัดส่วนที่เหมาะสมและปริมาณมากขึ้น โดยเพิ่มอาหารประเภทที่ให้พลังงาน  \n   -2.ควรเคลื่อนไหวและออกกำลังกายไม่ให้เหนื่อยมากหรือหอบที่ง่ายที่สุดคือการเดิน ')

            elif bmi_result <= 24.90:
                self.la_pix.setPixmap(QtGui.QPixmap('normalm.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('normal.png'))
                self.la_tex.setText('หุ่นเเซ๊บกำลังดี ผอมเพรียว')

                self.te_edit.setText('น้ำหนักปกติ \nค่าดัชนีมวลกายปกติมี 18.50 - 24.90 \n   -1. ควรกินอาหารให้หลากหลายครบ 5 หมู่ในสัดส่วนที่เหมาะสม  \n   -2.ควรเคลื่อนไหวและออกกำลังกายอย่างสม่ำเสมอทุกวัน หรือเกือบทุกวัน อย่างน้อยให้เหนื่อยพอควร ')

            elif bmi_result <= 29.90:
                self.la_pix.setPixmap(QtGui.QPixmap('befatm.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('ov.png'))
                self.la_tex.setText('Over Weight เนื้อหนังเรื่มมา')

                self.te_edit.setText('ท้วม / อ้วนระดับ 1\nค่าดัชนีมวลกายมี 25 - 29.90 \n   1. ควรควบคุมอาหาร โดยลดปริมาณอาหารหรือปรับเปลี่ยนอาหารจากที่ให้พลังงานมากเป็นอาหารที่ให้พลังงานน้อย  \n   2. ควรเคลื่อนไหวและออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอทุกวัน หรือเกือบทุกวันอย่างน้อยให้เหนื่อยพอควร ')

            elif bmi_result <= 34.9:
                self.la_pix.setPixmap(QtGui.QPixmap('obesem.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('ob.png'))
                self.la_tex.setText('Obese เริ่มจะอ้วนระยะสุดท้าย')

                self.te_edit.setText('อ้วน / อ้วนระดับ 3\nค่าดัชนีมวลกายมีมากกว่า 35.0\n   1. ควรควบคุมอาหารโดยลดปริมาณอาหารหรือปรับเปลี่ยนอาหารจากที่ให้พลังงานมากเป็นอาหารที่ให้พลังงานน้อย\n   2.ควรเคลื่อนไหวและออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอทุกวันหรือเกือบทุกวันอย่างน้อยให้เหนื่อยพอควรโดยหายใจกระชั้นขึ้น\n   3.ควรฝึกความแข็งแรงของกล้ามเนื้อด้วยการฝึกกายบริหารหรือยกน้ำหนัก  \n  4.ควรปรึกษาแพทย์ในการลดและควบคุมน้ำหนัก ')    

                
            elif bmi_result > 35 :
                self.la_pix.setPixmap(QtGui.QPixmap('fatmm.png')) 
                self.pix_ins.setPixmap(QtGui.QPixmap('ex.png')) 
                self.la_tex.setText('มึงอ้วนมาก หยุดเเดก เเละไปวิ่งซะ')

                self.te_edit.setText('อ้วนมาก / อ้วนระดับ 3\nค่าดัชนีมวลกายมีมากกว่า 35.0\n   1. ควรควบคุมอาหารโดยลดปริมาณอาหารหรือปรับเปลี่ยนอาหารจากที่ให้พลังงานมากเป็นอาหารที่ให้พลังงานน้อย\n   2.ควรเคลื่อนไหวและออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอทุกวันหรือเกือบทุกวันอย่างน้อยให้เหนื่อยพอควรโดยหายใจกระชั้นขึ้น\n   3.ควรฝึกความแข็งแรงของกล้ามเนื้อด้วยการฝึกกายบริหารหรือยกน้ำหนัก  \n  4.ควรปรึกษาแพทย์ในการลดและควบคุมน้ำหนัก ')

                

        #*-------------------------------------------------------------------------------------------------------------------------------------------------------------

        if self.rdg_g.isChecked():   #!--- เลือกผู้หญิง

            if bmi_result < 18.5:
                self.la_pix.setPixmap(QtGui.QPixmap('ug.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('under.png'))
                self.la_tex.setText('Under Weight ผอมมาก หาข้าวเเดกซะ')

                self.te_edit.setText('น้ำหนักน้อยกว่ามาตรฐาน \nค่าดัชนีมวลกายมีค่าน้อยกว่า 18.50 \n   1. ควรกินอาหารให้หลากหลายครบ 5 หมู่ในสัดส่วนที่เหมาะสมและปริมาณมากขึ้น โดยเพิ่มอาหารประเภทที่ให้พลังงาน  \n   -2.ควรเคลื่อนไหวและออกกำลังกายไม่ให้เหนื่อยมากหรือหอบที่ง่ายที่สุดคือการเดิน ')

            elif bmi_result <= 25:
                self.la_pix.setPixmap(QtGui.QPixmap('normalg.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('normal.png'))
                self.la_tex.setText('หุ่นเเซ๊บกำลังดี ผอมเพรียว')

                self.te_edit.setText('น้ำหนักปกติ \nค่าดัชนีมวลกายปกติมี 18.50 - 24.90 \n   -1. ควรกินอาหารให้หลากหลายครบ 5 หมู่ในสัดส่วนที่เหมาะสม  \n   -2.ควรเคลื่อนไหวและออกกำลังกายอย่างสม่ำเสมอทุกวัน หรือเกือบทุกวัน อย่างน้อยให้เหนื่อยพอควร ')

    
            elif bmi_result <= 30:
                self.la_pix.setPixmap(QtGui.QPixmap('befatg.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('ov.png'))
                self.la_tex.setText('Over Weight เนื้อหนังเริ่มมา')

                self.te_edit.setText('ท้วม / อ้วนระดับ 1\nค่าดัชนีมวลกายมี 25 - 29.90 \n   1. ควรควบคุมอาหาร โดยลดปริมาณอาหารหรือปรับเปลี่ยนอาหารจากที่ให้พลังงานมากเป็นอาหารที่ให้พลังงานน้อย  \n   2. ควรเคลื่อนไหวและออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอทุกวัน หรือเกือบทุกวันอย่างน้อยให้เหนื่อยพอควร ')

            elif bmi_result <= 35:
                self.la_pix.setPixmap(QtGui.QPixmap('obeseg.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('ob.png'))
                self.la_tex.setText('Obese เริ่มจะอ้วนระยะสุดท้าย')

                self.te_edit.setText('อ้วน / อ้วนระดับ 3\nค่าดัชนีมวลกายมีมากกว่า 35.0\n   1. ควรควบคุมอาหารโดยลดปริมาณอาหารหรือปรับเปลี่ยนอาหารจากที่ให้พลังงานมากเป็นอาหารที่ให้พลังงานน้อย\n   2.ควรเคลื่อนไหวและออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอทุกวันหรือเกือบทุกวันอย่างน้อยให้เหนื่อยพอควรโดยหายใจกระชั้นขึ้น\n   3.ควรฝึกความแข็งแรงของกล้ามเนื้อด้วยการฝึกกายบริหารหรือยกน้ำหนัก  \n  4.ควรปรึกษาแพทย์ในการลดและควบคุมน้ำหนัก ')
      

            elif bmi_result > 35 :
                self.la_pix.setPixmap(QtGui.QPixmap('fatg.png'))  
                self.pix_ins.setPixmap(QtGui.QPixmap('ex.png')) 
                self.la_tex.setText('Extreme มึงอ้วนมาก หยุดเเดก เเละไปวิ่งซะ')

                self.te_edit.setText('อ้วนมาก / อ้วนระดับ 3\nค่าดัชนีมวลกายมีมากกว่า 35.0\n   1. ควรควบคุมอาหารโดยลดปริมาณอาหารหรือปรับเปลี่ยนอาหารจากที่ให้พลังงานมากเป็นอาหารที่ให้พลังงานน้อย\n   2.ควรเคลื่อนไหวและออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอทุกวันหรือเกือบทุกวันอย่างน้อยให้เหนื่อยพอควรโดยหายใจกระชั้นขึ้น\n   3.ควรฝึกความแข็งแรงของกล้ามเนื้อด้วยการฝึกกายบริหารหรือยกน้ำหนัก  \n  4.ควรปรึกษาแพทย์ในการลดและควบคุมน้ำหนัก ')

                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())