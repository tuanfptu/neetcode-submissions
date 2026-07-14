class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            # Chiều cao của khối nước bị giới hạn bởi đường thấp hơn
            current_height = min(heights[left], heights[right])
            # Chiều rộng là khoảng cách giữa hai con trỏ
            current_width = right - left
            
            # Tính diện tích nước hiện tại và cập nhật giá trị lớn nhất
            current_water = current_height * current_width
            if current_water > max_water:
                max_water = current_water
                
            # Dịch chuyển con trỏ có chiều cao thấp hơn để tìm cơ hội có diện tích lớn hơn
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water