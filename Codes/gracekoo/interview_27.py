# -*- coding: utf-8 -*-
# @Time: 2020/6/27 14:35
# @Author: GraceKoo
# @File: interview_27.py
# @Desc: https://leetcode-cn.com/problems/
# zi-fu-chuan-de-pai-lie-lcof/
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []

        # nums存放需要继续遍历的字符，tmp存放当前遍历的结果
        def backtrack(nums, tmp):
            if not nums:
                result.add(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1 :], tmp + nums[i])

        result = set()
        backtrack(s, "")
        return list(result)


so = Solution()
print(so.permutation("ryawrowv"))
