FROM amazonlinux:latest

WORKDIR /usr
RUN yum -y groupinstall "Development tools" && \
    yum -y install gcc-c++ libcurl-devel cmake3 git openssl-devel&& \
    pip3 install awscli

# install aws-sdk-cpp
RUN set -ex;\
        git clone https://github.com/aws/aws-sdk-cpp.git && \
        cd aws-sdk-cpp && \
        mkdir build && \
        cd build && \
        cmake3 .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_INSTALL_PREFIX=/out -DCMAKE_CXX_COMPILER=g++ -DBUILD_ONLY="core" && \
        make && make install

# install aws-lambda-cpp
RUN git clone https://github.com/awslabs/aws-lambda-cpp.git && \
    cd aws-lambda-cpp && \
    mkdir build && \
    cd build && \
    cmake3 .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_INSTALL_PREFIX=/out -DCMAKE_CXX_COMPILER=g++ && \
    make && make install

COPY . /usr

ENV PROJECT_NAME "asapgo-suggest"

RUN cd asapgo-suggest && \
    mkdir build && \
    cd build && \
    cmake3 .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_PREFIX_PATH=/out -DCMAKE_CXX_COMPILER=g++
#     make && make aws-lambda-package-asapgo-suggest

# docker run

# docker run -it \
# -e AWS_DEFAULT_REGION= \
# -e AWS_ACCESS_KEY_ID= \
# -e AWS_SECRET_ACCESS_KEY= \
# aws_lambda_cpp /bin/bash

# deploy
# aws lambda update-function-code --function-name asapgo-suggest --zip-file fileb://asapgo-suggest/build/asapgo-suggest.zip


# invoke with log
# aws lambda invoke --function-name asapgo-suggest out --log-type Tail --query 'LogResult' --output text |  base64 -d


