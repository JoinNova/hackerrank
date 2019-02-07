def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
from random import*
class TestDataEmptyArray(object): #1-1-2
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):
    data=[0,1]
    @staticmethod
    def get_array():
        # complete this function
        
        data=TestDataUniqueValues.data
        return data
        

    @staticmethod
    def get_expected_result():
        # complete this function
        data=TestDataUniqueValues.get_array()
        return data.index(min(data))
        

class TestDataExactlyTwoDifferentMinimums(object):
    data=[0,0]
    @staticmethod
    def get_array():
        # complete this function
        data=TestDataExactlyTwoDifferentMinimums.data
        return data
        

    @staticmethod
    def get_expected_result():
        # complete this function
        data=TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))


def TestWithEmptyArray():#1-1
    try:
        seq = TestDataEmptyArray.get_array() #1-1-1
        result = minimum_index(seq) #1-2-1
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():#2-1-1
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()#1-1
TestWithUniqueValues()#2-1
TestiWithExactyTwoDifferentMinimums()
print("OK")
