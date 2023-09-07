FROM python:3

COPY . . 


#RUN pip install --upgrade pip
RUN pip3 install pymodbus==2.5.3
RUN pip3 install pyserial==3.5
RUN pip3 install six==1.16.0
RUN pip3 install tomli

EXPOSE 502
#RUN pip3 install time
CMD [ "python3", "/code/test_script.py"]
# CMD [ "python3", "/code/hobut_read_modbus.py"]