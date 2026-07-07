class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            #Sắp xếp các ký tự để tạo key chuẩn.
            # Các từ là anagram sẽ có cùng một key
            key = "".join(sorted(word))

            # Nếu key chưa tồn tại, tạo một nhóm rỗng
            if key not in groups:
                groups[key] = []

            # Thêm từ ban đầu vào nhóm tương ứn
            groups[key].append(word)

        # Chỉ trả về các nhóm từ cho nó đúng với cái đề bài
        return list(groups.values())