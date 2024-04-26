class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        while i < len(s) - 1:
            current_value = roman_dict[s[i]] 
            next_value = roman_dict[s[i + 1]]
            if current_value < next_value:
                total += next_value - current_value
                i += 1
            else:
                total += current_value
            i += 1
        if i == len(s) - 1:
            total += roman_dict[s[i]]
        return total