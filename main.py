import basics


def main():
    result_max = basics.maximum(2, 6)
    result_max_3 = basics.maximum_of_three(10, -5, 32)
    result_max_list = basics.max_of_list([3, 5, 9, 12, 45])
    print("result_max: %s" % result_max)
    print("result_max_3: %s" % result_max_3)
    print("result_max_list: %s" % result_max_list)
    basics.histogram([3, 15, 36])


if __name__ == "__main__":
    main()