class GarbageValueChecker:
    @staticmethod
    def check_garbage_val(val):
        if val == -999: 
            return 'X'
        elif val == "0xfc19": 
            return 'X'
        else:
            return val