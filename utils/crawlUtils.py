class CrawlUtils: 
    def splitKeywords(self, keywords: str):
        return keywords.split()
    
    def combineResult(self, data) -> str: 
        """
        Gom toàn bộ kết quả markdown từ danh sách data thành một chuỗi duy nhất.
        data: list chứa các dict dạng {"url": str, "content": str}
        """
        if not data:
            return ""

        combined_text = []

        for idx, item in enumerate(data, start=1):
            url = item.get("url", "Không rõ URL")
            content = item.get("content", "").strip()

            # Định dạng markdown cho từng trang
            section = (
                f"# KẾT QUẢ TRANG {idx}\n"
                f"**URL:** {url}\n\n"
                f"{content}\n"
                f"\n{'-'*80}\n"
            )
            combined_text.append(section)

        # Ghép tất cả thành một chuỗi duy nhất
        return "\n".join(combined_text)
    