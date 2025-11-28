import re
from config.logger import logger 
from urllib.parse import urlparse
class CrawlUtils: 
    def splitKeywords(self, keywords: str):
        return keywords.split()

    def clean_content(markdown: str) -> str:
        """
        Làm sạch markdown, loại bỏ links và content không cần thiết
        """
        # Loại bỏ markdown links [text](url)
        cleaned = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown)
        
        # Loại bỏ URLs đơn thuần
        cleaned = re.sub(r'https?://[^\s]+', '', cleaned)
        
        # Loại bỏ email
        cleaned = re.sub(r'\S+@\S+', '', cleaned)
        
        # Loại bỏ nhiều dòng trống liên tiếp
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
        
        # Loại bỏ các dòng chỉ chứa ký tự đặc biệt
        lines = [line for line in cleaned.split('\n') 
                if line.strip() and not re.match(r'^[\s\-_*#]+$', line)]
        
        return '\n'.join(lines).strip()


    def combineResultBase(self, data) -> str: 
        """
        Gom toàn bộ kết quả markdown từ danh sách data thành một chuỗi duy nhất.
        data: list chứa các dict dạng {"url": str, "content": str, "keyword": str (optional)}
        """
        if not data:
            return ""

        combined_text = []

        for idx, item in enumerate(data, start=1):
            url = item.get("url", "Không rõ URL")
            content = item.get("content", "").strip()
            keyword = item.get("keyword", "")

            # Định dạng markdown cho từng trang
            section = (
                f"# KẾT QUẢ TRANG {idx}\n"
                f"**Keyword:** {keyword}\n"
                f"**URL:** {url}\n\n"
                f"{content}\n"
                f"\n{'-'*80}\n"
            )
            combined_text.append(section)

        return "\n".join(combined_text)
    
    def combineResult(self, data) -> list:
        """
        Gom toàn bộ kết quả thành một mảng các object.
        data: list chứa các dict dạng {"url": str, "content": str, "title": str (optional)}
        """
        if not data:
            return []

        combined_results = []

        for item in data:
            url = item.get("url", "")
            content = item.get("content", "").strip()
            
            # Lấy title từ item nếu có, hoặc extract từ content
            raw_title = item.get("title", "")
            title = self._clean_title(raw_title, content, url)
            
            result_obj = {
                "title": title,
                "link": url,
                "data": content
            }
            combined_results.append(result_obj)

        return combined_results

    def _clean_title(self, raw_title: str, content: str, fallback_url: str) -> str:
        """
        Làm sạch title từ Crawl4AI.
        Xử lý markdown links, loại bỏ URLs, và format lại.
        """
        import re
        
        title = raw_title.strip() if raw_title else ""
        
        # Nếu không có title, thử extract từ content
        if not title and content:
            # Tìm heading đầu tiên (# hoặc ##)
            heading_match = re.search(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
            if heading_match:
                title = heading_match.group(1).strip()
            else:
                # Lấy dòng đầu tiên không rỗng
                lines = [line.strip() for line in content.split('\n') if line.strip()]
                title = lines[0] if lines else ""
        
        if not title:
            return fallback_url
        
        # Xử lý markdown links: [text](url) -> text
        title = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', title)
        
        # Loại bỏ các ký tự markdown còn lại
        title = re.sub(r'[#*_`]', '', title)
        
        # Loại bỏ URLs còn sót lại
        title = re.sub(r'https?://[^\s]+', '', title)
        
        # Loại bỏ khoảng trắng thừa
        title = ' '.join(title.split())
        
        # Giới hạn độ dài
        if len(title) > 150:
            title = title[:150] + '...'
        
        return title if title else fallback_url
    
    def removeSubWords(sentence: str):
        pass
    
    def is_valid_url(self, url: str) -> bool:
        """
        Kiểm tra URL có hợp lệ và không phải PDF
        """
        if not isinstance(url, str) or not url.startswith(("http://", "https://")):
            return False
        
        # Loại bỏ URLs có extension file không mong muốn
        parsed = urlparse(url.lower())
        path = parsed.path
        
        # Danh sách extensions cần bỏ qua
        skip_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', 
                          '.zip', '.rar', '.exe', '.dmg', '.pkg']
        
        if any(path.endswith(ext) for ext in skip_extensions):
            logger.info(f"Bỏ qua URL với file extension: {url}")
            return False
        
        return True