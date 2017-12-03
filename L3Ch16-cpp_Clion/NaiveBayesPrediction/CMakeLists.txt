cmake_minimum_required(VERSION 3.9)
project(NaiveBayesPrediction)

set(CMAKE_CXX_STANDARD 11)

include_directories(lib/Eigen-3.3)
include_directories(/usr/local/include)
link_directories(/usr/local/lib)


add_executable(NaiveBayesPrediction main.cpp classifier.cpp classifier.h)