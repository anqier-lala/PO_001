#coding=gbk
import  os
import xlrd
from common.config_utils import config

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/element_infos.xlsx')

class ElementdataUtils:
    def __init__(self,page_name,element_path=excel_path):
        self.element_path=element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.row_count=self.sheet.nrows

    def get_element_info(self,page_name):
        element_infos = {}
        for i in range(1, self.sheet.nrows):
            if self.sheet.cell_value(i, 2) == page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)  ##所属页面不要取值
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                timeout_value=self.sheet.cell_value(i, 5)   #先取出超时时间单元格的值
                #如果该单元格内没有浮点型的值的话，就取值默认配置中的值
                element_info['timeout'] = timeout_value if isinstance(timeout_value,float)else config.get_timeout
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos


if __name__ == '__main__':
    if __name__ == "__main__":
        # s = ElementdataUtils('login_page')
        elements = ElementdataUtils('login').get_element_info('login_page')
        # print(elements)
        for e in elements.values():
            print(e)




