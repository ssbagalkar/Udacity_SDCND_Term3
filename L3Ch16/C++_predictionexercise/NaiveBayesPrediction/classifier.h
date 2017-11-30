#ifndef CLASSIFIER_H
#define CLASSIFIER_H
#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include "Dense"

using namespace std;
using Eigen::ArrayXd;

class GNB {
public:

	vector<string> possible_labels = { "left","keep","right" };

	ArrayXd left_means;
	ArrayXd left_sds;

	ArrayXd keep_means;
	ArrayXd keep_sds;

	ArrayXd right_means; #pragma once
