class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sắp xếp mảng để áp dụng kỹ thuật hai con trỏ và tránh trùng lặp
        
        for i in range(len(nums) - 2):
            # Nếu phần tử hiện tại lớn hơn 0, tổng của 3 số chắc chắn > 0 vì mảng đã sắp xếp
            if nums[i] > 0:
                break
                
            # Bỏ qua các phần tử trùng lặp cho vị trí số thứ nhất
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Khởi tạo hai con trỏ cho hai số còn lại
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < 0:
                    left += 1  # Cần tăng tổng lên -> dịch con trỏ trái sang phải
                elif three_sum > 0:
                    right -= 1  # Cần giảm tổng xuống -> dịch con trỏ phải sang trái
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Cập nhật con trỏ và bỏ qua các giá trị trùng lặp tiếp theo
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res