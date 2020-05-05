#coding=gbk
import  os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, "../conf/local_config.ini")
print(cfgpath)


class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf=configparser.ConfigParser()  ##����˽��ʵ�����ԣ���������ڲ�ʹ�ã��ⲿ���ɷ��ʣ�Ҳ���ʹ�õļ���
        self.__conf.read(config_path, encoding="gbk")  #��Ϊ�༭�����õ���gbk,���������ļ���ȡ��ʱ������Ҳ��Ҫ����Ϊgbk

    def read_ini(self,sec,option):
        value=self.__conf.get(sec,option)
        return value

    @property    #�������ɽ����������������һ�������ԣ�ֱ�ӵ���������ԾͿ���
    def get_url(self):
        value=self.read_ini('default','url')
        return value


    @property    #�������ɽ����������������һ�������ԣ�ֱ�ӵ���������ԾͿ���
    def get_user_name(self):
        value=self.read_ini('user','user_name')
        return value

    @property
    def get_password(self):
        value = self.read_ini('user', 'password')
        return value

    @property
    def get_timeout(self):
        value = float(self.read_ini('default', 'timeout'))
        return value

    @property
    def screenshot_path(self):
        value = self.read_ini('default', 'screen_shot_path')
        return value


# #ֱ�Ӷ���һ�����������ⲿֱ�ӵ��ø÷����Ϳ��ԣ�����Ҫ��ÿ�ζ�����һ������
config=ConfigUtils()


if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    cfgpath = os.path.join(current_path, "../conf/local_config.ini")
    config_u=ConfigUtils()
    print(config_u.get_url)
    print(config_u.get_user_name)
    print(config_u.get_password)
    print(config_u.screenshot_path)

