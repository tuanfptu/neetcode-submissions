class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i != j:
                    # nhân nums[j] vào product
                    product *= nums[j]

            # thêm product vào result tại đây
            result.append(product)

        return result