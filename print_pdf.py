import os
from playwright.sync_api import sync_playwright

def create_pdf():
    input_file = "index.html"
    output_pdf = "Final_Ramadan_Journal.pdf"
    file_path = f"file://{os.path.abspath(input_file)}"

    print("🚀 جاري الطباعة بأبعاد دقيقة...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_path)

        page.pdf(
            path=output_pdf,
            format="A5",            # حجم الورقة
            print_background=True,  # طباعة الألوان
            scale=0.99,                # الحجم الطبيعي 100%
            margin={                # هوامش صفرية
                "top": "0px",
                "bottom": "0px",
                "left": "0px",
                "right": "0px"
            },
            # هذا الخيار مهم: يفضل حجم الصفحة المحدد في CSS
            prefer_css_page_size=True 
        )

        browser.close()
        print(f"✅ تم! تفقد الملف: {output_pdf}")

if __name__ == "__main__":
    create_pdf()