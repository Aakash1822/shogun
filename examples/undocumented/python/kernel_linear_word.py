#!/usr/bin/env python
from tools.load import LoadMatrix
import numpy as np

lm=LoadMatrix()
traindat = np.ushort(lm.load_numbers('../data/fm_train_word.dat'))
testdat = np.ushort(lm.load_numbers('../data/fm_test_word.dat'))

parameter_list=[[traindat,testdat,1.2],[traindat,testdat,1.2]]

def kernel_linear_word (fm_train_word=traindat,fm_test_word=testdat,scale=1.2):

	from shogun import AvgDiagKernelNormalizer
	import shogun as sg

	feats_train=sg.features(fm_train_word)
	feats_test=sg.features(fm_test_word)

	kernel=sg.kernel("LinearKernel")
	kernel.init(feats_train, feats_train)
	kernel.set_normalizer(AvgDiagKernelNormalizer(scale))
	kernel.init(feats_train, feats_train)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()
	return kernel

if __name__=='__main__':
	print('LinearWord')
	kernel_linear_word(*parameter_list[0])
