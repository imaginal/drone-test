FROM python:3.10-slim
ADD mavic /root/mavic
ADD setup.py /root/setup.py
WORKDIR /root
RUN python setup.py install
# && rm -rf build mavic setup.py
CMD ["python", "-m", "mavic"]
